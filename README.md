# 📚 Doc Generator AI 🚀

![GitHub repo size](https://img.shields.io/github/repo-size/chaos4455/doc-generator-ai)
![GitHub stars](https://img.shields.io/github/stars/chaos4455/doc-generator-ai?style=social)
![GitHub forks](https://img.shields.io/github/forks/chaos4455/doc-generator-ai?style=social)
![GitHub issues](https://img.shields.io/github/issues/chaos4455/doc-generator-ai)
![GitHub license](https://img.shields.io/github/license/chaos4455/doc-generator-ai)

## 🌟 Visão Geral

O **Doc Generator AI** é uma aplicação avançada que automatiza a geração de manuais técnicos detalhados utilizando inteligência artificial. Este projeto faz parte do meu portfólio pessoal de DevOps e exemplifica a implementação completa do ciclo CI/CD e automação de DevOps, integrado com soluções de IA.

Este projeto demonstra um exemplo prático de automação de CI/CD para geração de documentação usando GitHub Actions, destacando minha habilidade em desenvolvimento de automação, integração contínua e entrega contínua (CI/CD), e uso de ferramentas de automação para melhorar eficiência e consistência no ciclo de desenvolvimento de software.

## 📌 Funcionalidades

- 📝 **Geração de Conteúdo**: Utiliza APIs avançadas de linguagem para gerar conteúdo técnico detalhado e estilizado.
- ⚙️ **Automação de Tarefas**: Geração automática de manuais baseados em temas fornecidos, com subdivisão em subtemas e criação de títulos específicos.
- 💾 **Armazenamento de Artefatos**: Os manuais gerados são salvos como arquivos `.md` para fácil acesso e leitura.
- 🛠️ **Pipeline CI/CD Completo**: Implementação de workflows GitHub Actions para automação de testes, build e deploy.
- 📈 **Integração Contínua**: Verificação automática de dependências e integridade do código.
- 🚀 **Entrega Contínua**: Deploy automatizado de atualizações e novas versões dos manuais.

## 🚀 Tecnologias Utilizadas

- **Python** 🐍: Linguagem principal utilizada para desenvolvimento do script de geração de conteúdo.
- **GitHub Actions** 🛠️: Ferramenta de CI/CD para automação do ciclo de vida do software.
- **API de Linguagem** 🌐: Utilizada para gerar o conteúdo dos manuais.
- **Markdown** 📄: Formato utilizado para salvar os manuais gerados.

## 🤖 Automatização de Geração e Commit de Manuais

Este repositório contém um fluxo de trabalho automatizado para gerar e commitar manuais automaticamente no GitHub. Utiliza GitHub Actions para executar o script `doc-gen.py`, que gera manuais baseados em temas específicos fornecidos como variáveis de ambiente.

### Funcionalidades Principais

- **Automação de Geração de Manuais**: Utiliza Python 3.11 para executar o script `doc-gen.py`, que interage com a API de geração de conteúdo do Google Gemini.
  
- **CI/CD Automatizado**: Configurado para rodar no evento de push para a branch `main`, garantindo a geração automática de manuais sempre que há atualizações no código.

- **Verificação e Commit**: Após a geração dos manuais, verifica se os artefatos foram gerados corretamente e realiza um commit com as alterações no repositório.

- **Configuração do Git**: Configura o Git dentro do ambiente de execução para permitir commits automatizados.

### Passos Detalhados

1. **Checkout do Repositório**:
   - Utiliza `actions/checkout` para clonar o repositório no ambiente de execução do GitHub Actions.

2. **Configuração do Ambiente Python**:
   - Usa `actions/setup-python` para configurar a versão 3.11 do Python, necessária para executar o script `doc-gen.py`.

3. **Instalação da Biblioteca Requests**:
   - Garante que a biblioteca `requests` esteja instalada para fazer requisições HTTP necessárias no script.

4. **Verificação e Permissão do Script**:
   - Verifica se o script `doc-gen.py` existe e o torna executável usando `chmod +x`.

5. **Execução do Script de Geração de Manuais**:
   - Define variáveis de ambiente, como `GOOGLEAPIKEY` e `TEMA`, necessárias para a execução do script, e executa-o passando o tema como argumento.

6. **Verificação dos Artefatos Gerados**:
   - Após a execução do script, lista os artefatos gerados para verificar se foram criados corretamente.

7. **Configuração do Git para Commit Automático**:
   - Configura o nome e e-mail do usuário Git para permitir commits automáticos usando o GitHub Actions.

8. **Commit Automático das Alterações**:
   - Adiciona as alterações feitas (os manuais gerados) ao índice do Git e realiza um commit com uma mensagem padronizada contendo o tema dos manuais gerados.

9. **Push das Mudanças de Volta para o Repositório**:
   - Empurra as alterações com os novos manuais gerados de volta para a branch `main` do repositório remoto.

### Configuração Adicional

Certifique-se de configurar a variável de ambiente `GOOGLEAPIKEY` como um segredo no GitHub para garantir a segurança da chave de API utilizada na integração com o Google Gemini.

### Referência ao Fluxo de Trabalho Completo

Para ver o fluxo de trabalho completo configurado em YAML, consulte [`.github/workflows/generate-docs.yaml`](https://github.com/chaos4455/doc-generator-ai/blob/main/.github/workflows/generate-docs.yaml).

---

### Geração Automatizada de Manuais 📘🤖

Este projeto utiliza um script Python chamado `doc-gen.py` para automatizar a geração de manuais de forma inteligente e eficiente. A seguir, detalhamos como esse script é integrado em um fluxo de trabalho automatizado de CI/CD e DevOps.

#### **Script Python: `doc-gen.py`**

O arquivo `doc-gen.py` é o núcleo deste projeto, responsável por integrar a lógica de geração de conteúdo utilizando a API Google Gemini para criar manuais detalhados com base em temas específicos.

**Funcionalidades Principais:**

- **Geração de Nome Único:** Utiliza hash SHA-256 para gerar nomes únicos para os manuais, garantindo identificação única.
  
- **Requisição à API Gemini:** Envia requisições à API Google Gemini para gerar conteúdo textual baseado em prompts específicos.

- **Processamento em Paralelo:** Utiliza `ThreadPoolExecutor` para processar múltiplos manuais simultaneamente, otimizando o tempo de geração.

#### **Uso no Fluxo de Trabalho**

No fluxo de trabalho de automação CI/CD, o `doc-gen.py` é acionado por meio de GitHub Actions, configurado para executar as seguintes etapas:

1. **Instalação e Configuração:**
   - Configura o ambiente Python 3.11.
   - Instala a biblioteca `requests` para comunicação com a API.

2. **Verificação e Preparação:**
   - Verifica a existência do script `doc-gen.py`.
   - Torna o script executável caso necessário.

3. **Geração de Manuais:**
   - Define o tema dos manuais através de variáveis de ambiente.
   - Utiliza o script para gerar manuais com base no tema especificado.

4. **Verificação de Artefatos:**
   - Verifica os manuais gerados no diretório de artefatos para garantir a conclusão bem-sucedida.

5. **Commit e Push Automatizados:**
   - Configura o Git para commit e push das alterações feitas pelos manuais gerados de volta para o repositório principal.

#### **Referências Adicionais**

- [Código Python `doc-gen.py` no repositório](https://github.com/chaos4455/doc-generator-ai/blob/main/doc-gen.py)
- [Arquivo YAML de configuração no GitHub Actions](https://github.com/chaos4455/doc-generator-ai/blob/main/.github/workflows/generate-docs.yaml)

Este projeto demonstra minha habilidade em integrar IA com práticas DevOps para automação de processos, proporcionando eficiência e qualidade na entrega de documentação técnica avançada. 🚀✨


## 🔧 Configuração e Uso

### 1. Clonar o Repositório

```bash
git clone https://github.com/chaos4455/doc-generator-ai.git
cd doc-generator-ai
```

2. Configurar Variáveis de Ambiente
Certifique-se de definir a chave da API para a geração de conteúdo:

```bash

export GOOGLEAPIKEY="sua_chave_api_aqui"
export TEMA="itil v3 e service management no ambiente windows"  # Defina o tema desejado

```
3. Executar o Script

```bash

python doc-gen.py "$TEMA"
```
4. Verificar os Artefatos Gerados
Os manuais gerados serão armazenados no diretório artifacts.

🛠️ Estrutura do Projeto
bash
Copiar código
.
├── doc-gen.py          # Script principal de geração de conteúdo
├── README.md           # Documentação do projeto
├── .github
│   └── workflows
│       └── generate-manuals.yml  # Workflow do GitHub Actions
└── artifacts           # Diretório para armazenar os manuais gerados

🌍 Ciclo DevOps

Integração Contínua (CI)

GitHub Actions: Workflows configurados para testar, construir e verificar o código automaticamente em cada push para a branch principal.

Entrega Contínua (CD)

Automação de Deploy: Os manuais gerados são automaticamente commitados e pushados para o repositório, garantindo que a documentação esteja sempre atualizada.

Monitoramento e Feedback

Notificações: Alertas e logs configurados para monitorar o sucesso das execuções dos workflows e identificar rapidamente qualquer falha.

🤖 Automatização Inteligente

IA na Geração de Conteúdo: Uso de APIs avançadas de processamento de linguagem natural para criar manuais ricos em detalhes, bem estruturados e visualmente agradáveis.

🏆 Destaques do Projeto

Escalabilidade: Capaz de gerar dezenas de manuais simultaneamente usando processamento paralelo.

Personalização: Fácil configuração para diferentes temas e subtemas.

Eficiência: Reduz o tempo de criação de documentação técnica, permitindo que os profissionais de TI se concentrem em tarefas mais críticas.

🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades. Basta seguir os passos abaixo:

Faça um fork deste repositório.
Crie uma nova branch (git checkout -b feature/nova-funcionalidade).
Faça commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').
Faça push para a branch (git push origin feature/nova-funcionalidade).
Abra um Pull Request (PR).
Configurando o Fork
Para executar corretamente o workflow, siga os passos abaixo:

Cadastre a API Key do Google Gemini como um Secret:

Vá para a aba Settings do seu repositório fork.
Clique em Secrets e depois em Actions.
Adicione um novo secret chamado GOOGLEAPIKEY com sua chave da API do Google Gemini.
Dê Permissões para a Action Executar Commits:

Vá para a aba Settings do seu repositório fork.
Clique em Actions e depois em General.
Em Workflow permissions, selecione Read and write permissions.
Aprovando Pull Requests
Para aprovar um Pull Request:

Vá para a aba Pull requests do repositório.
Clique no PR que deseja revisar.
Revise as mudanças propostas e, se estiverem de acordo, clique em Merge pull request.

📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
