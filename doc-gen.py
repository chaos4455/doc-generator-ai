import os
import sys
import requests
import hashlib
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

# Chave da API para acesso à geração de conteúdo (substitua pela sua chave)
API_KEY = os.getenv('GOOGLEAPIKEY')

# Função para gerar um nome único baseado em uma hash SHA-256 do texto
def generate_unique_name(prompt_text):
    # Remove caracteres especiais e espaços
    clean_text = re.sub(r'[^\w\s]', '', prompt_text)
    hash_object = hashlib.sha256(clean_text.encode())
    hash_digest = hash_object.hexdigest()
    unique_name = f"{clean_text[:50].replace(' ', '_')}_{hash_digest[:8]}"
    return unique_name

# Função para enviar requisição à API de geração de conteúdo
def generate_content(prompt_text):
    content = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt_text
                    }
                ]
            }
        ]
    }

    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}'

    response = requests.post(url, json=content)

    if response.status_code == 200:
        json_response = response.json()
        response_text = json_response['candidates'][0]['content']['parts'][0]['text']
        return response_text
    else:
        print(f"Erro ao enviar requisição: {response.status_code} - {response.text}")
        return None

# Função para gerar uma lista de subtemas baseada no tema principal
def generate_subthemes(theme):
    prompt_text = f"Gere 2 subtemas baseados no tema '{theme}'."
    subthemes_text = generate_content(prompt_text)
    if subthemes_text:
        return [subtheme.strip() for subtheme in subthemes_text.split('\n') if subtheme.strip()]
    else:
        print("Falha ao gerar a lista de subtemas.")
        return []

# Função para gerar a lista de títulos dos manuais para um subtema
def generate_manual_titles(subtheme):
    prompt_text = f"Crie uma lista com 2 títulos de manuais que podem ser criados sobre o subtema '{subtheme}'."
    titles_text = generate_content(prompt_text)
    if titles_text:
        return [title.strip() for title in titles_text.split('\n') if title.strip()]
    else:
        print(f"Falha ao gerar a lista de títulos dos manuais para o subtema '{subtheme}'.")
        return []

# Função para processar os manuais em paralelo usando ThreadPoolExecutor
def process_manuals(subtheme, manual_titles):
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_title = {executor.submit(generate_manual_content, subtheme, title): title for title in manual_titles}
        for future in as_completed(future_to_title):
            title = future_to_title[future]
            try:
                generated_content = future.result()
                if generated_content:
                    unique_name = generate_unique_name(f"{title}_{subtheme}")
                    with open(f"{unique_name}.md", "w", encoding="utf-8") as md_file:
                        md_file.write(generated_content)
                    print(f"Manual gerado com sucesso para o subtema '{subtheme}': {unique_name}.md")
                else:
                    print(f"Falha ao gerar o Manual para o título: {title} no subtema '{subtheme}'")
            except Exception as exc:
                print(f"Erro ao processar o Manual para o título: {title} no subtema '{subtheme}': {exc}")

# Função para gerar o conteúdo de um manual específico
def generate_manual_content(subtheme, title):
    prompt = (
        f"{title}. Tema: {subtheme}. "
        "O manual deve ser pratico, operacional, ensinar o que fazer, como fazer, de que jeito fazer, em detalhes, exemplo, do começo ao fim, auto explicativo, nao pode ser apenas índice ou listas, tem que ser processos,  deve ser estilizado para o Notion, ser bem detalhado, estilizado, completo, ensinar tudo nos mínimos detalhes, não ser superficial, ser extremamente explicativo e prático, usar didatica técnica , usar muitos ícones e emojis nas respostas."
    )
    return generate_content(prompt)

# Função principal para gerar manuais
def create_manuals(theme):
    # Gera a lista de subtemas
    subthemes = generate_subthemes(theme)

    if subthemes:
        for subtheme in subthemes:
            # Gera a lista de títulos dos manuais para o subtema atual
            manual_titles = generate_manual_titles(subtheme)

            if manual_titles:
                process_manuals(subtheme, manual_titles)
            else:
                print(f"Falha ao gerar a lista de títulos dos manuais para o subtema '{subtheme}'.")
    else:
        print("Falha ao gerar a lista de subtemas.")

# Obtém o tema da variável de ambiente TEMA, se não definido, usa um tema padrão
tema = os.getenv("TEMA", "Tema Padrão")

# Cria os manuais com base no tema fornecido
create_manuals(tema)
