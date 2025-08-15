import os
import sys
# Removido: import requests (não é mais necessário para a comunicação com a API Gemini)
import hashlib
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

# Importa a biblioteca oficial do Google Generative AI
import google.generativeai as genai
import google.api_core.exceptions # Para tratamento de erros da API

# Chave da API para acesso à geração de conteúdo
API_KEY = os.getenv('GOOGLEAPIKEY')

# --- Configuração da API do Google Gemini ---
if not API_KEY:
    print("Erro: A variável de ambiente GOOGLEAPIKEY não está definida.")
    print("Por favor, defina-a antes de executar o script.")
    sys.exit(1) # Sai do script se a chave não estiver configurada

genai.configure(api_key=API_KEY)

# Função para gerar um nome único baseado em uma hash SHA-256 do texto
def generate_unique_name(prompt_text):
    # Remove caracteres especiais e espaços
    # Limitando o texto para hash para evitar nomes de arquivo muito longos e garantir consistência
    clean_text = re.sub(r'[^\w\s]', '', prompt_text)[:100] # Limita a 100 caracteres antes de limpar
    hash_object = hashlib.sha256(clean_text.encode('utf-8'))
    hash_digest = hash_object.hexdigest()
    # Cria um nome de arquivo seguro, substituindo espaços e limitando a parte do texto
    unique_name = f"{re.sub(r'\s+', '_', clean_text)[:50]}_{hash_digest[:8]}"
    return unique_name.strip('_') # Remove underscore extra se o texto for curto

# Função para enviar requisição à API de geração de conteúdo (agora usando google-generativeai)
def generate_content(prompt_text):
    try:
        # Define o modelo que será utilizado
        # Usando 'gemini-1.5-flash' conforme você já havia ajustado no seu código requests
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Envia a requisição de geração de conteúdo
        response = model.generate_content(prompt_text)
        
        # Acessa o texto da resposta. A biblioteca lida com a estrutura complexa do JSON.
        # Verifica se há texto na resposta antes de retornar
        if response.parts and response.parts[0].text:
            return response.parts[0].text
        else:
            # Caso a resposta seja vazia ou incompleta (ex: devido a questões de segurança ou tokens)
            print(f"Aviso: A API retornou uma resposta vazia ou incompleta para o prompt.")
            print(f"Prompt: {prompt_text[:100]}...") # Mostra os primeiros 100 caracteres do prompt
            if hasattr(response, 'prompt_feedback') and response.prompt_feedback:
                print(f"Feedback do Prompt: {response.prompt_feedback}")
            return None

    except google.api_core.exceptions.GoogleAPIError as e:
        print(f"Erro da API do Google: {e}")
        # Detalhes adicionais podem ser úteis para depuração
        if hasattr(e, 'response'):
            print(f"Detalhes da Resposta de Erro: {e.response.text}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao gerar conteúdo: {e}")
        return None

# Função para gerar uma lista de subtemas baseada no tema principal
def generate_subthemes(theme):
    prompt_text = f"Gere uma lista de 2 subtemas detalhados, únicos e distintos sobre o tema principal: '{theme}'. Não inclua introdução ou conclusão, apenas a lista. Use um formato simples de lista."
    subthemes_text = generate_content(prompt_text)
    if subthemes_text:
        # Tenta parsear a resposta, assumindo que cada linha é um subtema
        # Remove marcadores de lista como "1. ", "- " etc.
        subthemes = [re.sub(r'^\s*[\d\.\-\*]+\s*', '', line).strip() for line in subthemes_text.split('\n') if line.strip()]
        return subthemes
    else:
        print("Falha ao gerar a lista de subtemas.")
        return []

# Função para gerar a lista de títulos dos manuais para um subtema
def generate_manual_titles(subtheme):
    prompt_text = f"Crie uma lista com 2 a 3 títulos de manuais *detalhados e completos* que podem ser criados sobre o subtema '{subtheme}'. Os títulos devem ser práticos e específicos. Não inclua introdução ou conclusão, apenas a lista. Use um formato simples de lista."
    titles_text = generate_content(prompt_text)
    if titles_text:
        # Tenta parsear a resposta, removendo marcadores de lista
        titles = [re.sub(r'^\s*[\d\.\-\*]+\s*', '', line).strip() for line in titles_text.split('\n') if line.strip()]
        return titles
    else:
        print(f"Falha ao gerar a lista de títulos dos manuais para o subtema '{subtheme}'.")
        return []

# Função para processar os manuais em paralelo usando ThreadPoolExecutor
def process_manuals(subtheme, manual_titles):
    print(f"\n--- Gerando manuais para o subtema: '{subtheme}' ---")
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_title = {executor.submit(generate_manual_content, subtheme, title): title for title in manual_titles}
        for future in as_completed(future_to_title):
            title = future_to_title[future]
            try:
                generated_content = future.result()
                if generated_content:
                    # Garante que o nome do arquivo seja seguro e único
                    unique_name = generate_unique_name(f"{title}") 
                    file_path = f"{unique_name}.md"
                    with open(file_path, "w", encoding="utf-8") as md_file:
                        md_file.write(generated_content)
                    print(f"✅ Manual gerado com sucesso: '{file_path}' (Título: '{title}')")
                else:
                    print(f"❌ Falha ao gerar o conteúdo do Manual para o título: '{title}' no subtema '{subtheme}' (conteúdo vazio ou erro prévio)")
            except Exception as exc:
                print(f"❌ Erro crítico ao processar o Manual para o título: '{title}' no subtema '{subtheme}': {exc}")

# Função para gerar o conteúdo de um manual específico
def generate_manual_content(subtheme, title):
    prompt = (
        f"Crie um manual completo e detalhado sobre o tópico '{title}', considerando o subtema maior de '{subtheme}'. "
        "O manual deve ser altamente rico, estilizado e didático. "
        "Use muitos tópicos, seções, exemplos práticos, snippets de código (especialmente para bash/shell e Red Hat/Solaris), tabelas (se aplicável), diagramas de árvore para ilustrar hierarquias ou fluxos de processo. "
        "Gere respostas longas e exaustivas. Para cada exemplo, forneça no mínimo 5-10 exemplos práticos. "
        "**Obrigatório**: Use inúmeros ícones e emojis (unicode) ao longo do texto para representar conceitos, tecnologias, ações, ferramentas, práticas e para estilizar o manual. "
        "O manual deve ser prático, operacional, ensinar o que fazer, como fazer e de que jeito fazer, em detalhes, do começo ao fim, sendo auto explicativo. Não deve ser apenas um índice ou uma lista de tópicos, mas sim um guia de processos passo a passo. "
        "O conteúdo deve ser estilizado para o Notion (mas com markdown padrão), ser extremamente detalhado, completo, e não superficial. Deve ser explicativo e prático, utilizando uma didática técnica acessível."
        "\n\n🚨 Dica: Pense como um engenheiro que precisa documentar cada detalhe para que alguém sem experiência possa replicar."
    )
    print(f"Gerando conteúdo para: '{title}' (Subtema: '{subtheme}')")
    return generate_content(prompt)

# Função principal para gerar manuais
def create_manuals(theme):
    print(f"Iniciando a geração de manuais para o tema principal: '{theme}'")
    # Gera a lista de subtemas
    subthemes = generate_subthemes(theme)

    if subthemes:
        print(f"Subtemas gerados: {subthemes}")
        for subtheme in subthemes:
            # Gera a lista de títulos dos manuais para o subtema atual
            manual_titles = generate_manual_titles(subtheme)

            if manual_titles:
                print(f"Títulos de manuais para '{subtheme}': {manual_titles}")
                process_manuals(subtheme, manual_titles)
            else:
                print(f"❗ Nenhum título de manual gerado para o subtema '{subtheme}'. Pulando este subtema.")
    else:
        print("❗ Nenhuma lista de subtemas foi gerada. Encerrando o processo.")

# Obtém o tema da variável de ambiente TEMA
# Use um tema padrão ou saia se TEMA não for fornecido e você quiser que seja obrigatório
if __name__ == "__main__":
    tema = os.getenv("TEMA")
    if not tema:
        print("Erro: A variável de ambiente 'TEMA' não foi definida.")
        print("Uso: export TEMA=\"seu tema\" && python doc-gen.py")
        sys.exit(1)

    create_manuals(tema)
    print("\nProcesso de geração de manuais concluído.")
