**📘Capítulo 2: Domine a Automação de Execução de Código Python com GitHub Actions no Linux**

**✨Introdução**

Automatize a execução de seu código Python em ambientes Linux usando o GitHub Actions, um serviço de automação de fluxo de trabalho contínuo da GitHub. Com este guia passo a passo, você aprenderá a criar e executar ações personalizadas para testar, construir e implantar seus projetos Python.

**🚀 Pré-requisitos**

- Conta GitHub
- Projeto Python
- Ambiente Linux

**🎯 Objetivos**

- Criar e configurar ações personalizadas do GitHub
- Automatizar a execução de testes Python
- Construir e implantar projetos Python

**📝 Seções**

**1. Criação de uma Ação Personalizada**

**🌱 Etapa 1: Inicializar o Repositório de Ação**

- Crie um novo repositório no GitHub chamado "my-python-action".
- Adicione um arquivo `action.yml` ao diretório `.github/workflows`.

**🌱 Etapa 2: Definir a Ação**

- Defina uma tarefa chamada `run-python-tests` no arquivo `action.yml`:

```yaml
name: Run Python Tests
on: [push]
jobs:
  test-python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: my-python-action/run-python-tests@v1
```

**🌱 Etapa 3: Publicar a Ação**

- Publique sua ação no GitHub Marketplace usando o comando:

```
gh release create v1
```

**2. Automatizando Testes Python**

**🌱 Etapa 1: Usar a Ação Personalizada**

- Adicione o uso da ação ao pipeline do seu projeto Python no arquivo `.github/workflows/ci.yml`:

```yaml
name: CI Pipeline
on: [push]
jobs:
  test-python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: my-python-action/run-python-tests@v1
```

**🌱 Etapa 2: Executar Testes**

- Faça push das alterações para o seu repositório e os testes serão executados automaticamente.

**3. Construindo e Implantando Projetos Python**

**🌱 Etapa 1: Personalizar a Ação**

- Modifique o arquivo `action.yml` da ação para adicionar tarefas de construção e implantação:

```yaml
name: Build and Deploy Python Project
on: [push]
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: my-python-action/build-python-project@v1
      - uses: my-python-action/deploy-python-project@v1
```

**🌱 Etapa 2: Usar a Ação Atualizada**

- Substitua a ação `run-python-tests` pela ação `build-deploy` no pipeline do seu projeto.

**🌱 Etapa 3: Construir e Implantar**

- Faça push das alterações e o projeto Python será construído e implantado automaticamente.

**🎉 Conclusão**

Parabéns! Você dominou a automação de execução de código Python usando GitHub Actions no Linux. Com este guia, você pode automatizar seus fluxos de trabalho de teste, construção e implantação, economizando tempo e esforço.