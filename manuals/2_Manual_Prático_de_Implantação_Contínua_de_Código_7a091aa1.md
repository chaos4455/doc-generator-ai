**Manual Prático de Implantação Contínua de Código Python em Servidores Linux Usando GitHub Actions**

**Tema: Implantação Contínua de Código Python em Servidores Linux com GitHub Actions**

**Introdução**

A implantação contínua (CI/CD) automatiza o processo de desenvolvimento de software, permitindo que os desenvolvedores integrem com mais frequência e implantem atualizações mais rapidamente. Este manual fornecerá um guia passo a passo sobre como configurar uma implantação contínua de código Python em servidores Linux usando o GitHub Actions.

**Diagrama de Fluxo de Implantação Contínua**

[Image of CI/CD flowchart]

**Pré-requisitos**

* Servidor Linux com Python 3.6 ou superior instalado
* Conta GitHub
* Gerenciador de pacotes Pip

**Configuração do Repositório GitHub**

1. Crie um novo repositório GitHub para o seu projeto Python.
2. Navegue até o arquivo `.github/workflows` e crie um novo arquivo de fluxo de trabalho YAML.
3. Adicione o seguinte conteúdo ao arquivo de fluxo de trabalho:

```yaml
name: CI/CD Python

on:
  push:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip wheel
          pip install -r requirements.txt
      - name: Test code
        run: |
          python -m unittest discover -v
```

**Configuração do Servidor Linux**

1. Instale o GitHub Actions Runner no servidor:
   ```bash
   curl -sSfL https://get.github.com/actions/runner/linux/latest | sh
   ```
2. Registre o Runner com o repositório:
   ```bash
   ./config.sh --url https://github.com/<username>/<repo-name>.git
   ```
3. Inicie o Runner:
   ```bash
   ./run.sh
   ```

**Testando o Fluxo de Trabalho de CI/CD**

1. Faça push do seu código para o repositório GitHub.
2. O fluxo de trabalho será acionado automaticamente.
3. Aguarde a conclusão da execução e verifique os resultados no GitHub.

**Implantação no Servidor Linux**

1. Adicione um novo job ao arquivo de fluxo de trabalho:

```yaml
  deploy:
    runs-on: ubuntu-latest
    needs: build-and-test
    steps:
      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USERNAME }}
          password: ${{ secrets.SERVER_PASSWORD }}
          script: |
            cd /var/www/my_app
            rm -rf *
            cp -r /tmp/artifact/* .
            sudo systemctl restart my_app
```

2. Crie segredos no GitHub para seu host, nome de usuário e senha do servidor.
3. Faça push das alterações para o GitHub.
4. Após a conclusão bem-sucedida do fluxo de trabalho, seu código será implantado no servidor Linux.

**Conclusão**

Seguir este manual permitirá que você configure uma implantação contínua eficiente para seu código Python em servidores Linux usando GitHub Actions. Ao automatizar o processo de integração e implantação, você pode acelerar o desenvolvimento e fornecer atualizações de aplicativos com mais frequência.