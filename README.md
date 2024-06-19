# 📚 Doc Generator AI 🚀

![GitHub repo size](https://img.shields.io/github/repo-size/chaos4455/doc-generator-ai)
![GitHub stars](https://img.shields.io/github/stars/chaos4455/doc-generator-ai?style=social)
![GitHub forks](https://img.shields.io/github/forks/chaos4455/doc-generator-ai?style=social)
![GitHub issues](https://img.shields.io/github/issues/chaos4455/doc-generator-ai)
![GitHub license](https://img.shields.io/github/license/chaos4455/doc-generator-ai)

## 🌟 Visão Geral

O **Doc Generator AI** é uma aplicação avançada que automatiza a geração de manuais técnicos detalhados utilizando inteligência artificial. Este projeto faz parte do meu portfólio pessoal de DevOps e exemplifica a implementação completa do ciclo CI/CD e automação de DevOps.

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
