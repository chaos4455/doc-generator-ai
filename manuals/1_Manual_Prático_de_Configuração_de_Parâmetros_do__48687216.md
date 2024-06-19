## 📘 Manual Prático de Configuração de Parâmetros do GKE no Google Cloud VCP

**Parte 1: Parâmetros de Configuração Básicos**

**Tópico 1: Criando um Cluster do GKE**

**Seção 1: Pré-requisitos**

* Conta do Google Cloud
* Projeto do Google Cloud
* Região do Google Cloud

**Seção 2: Passos**

1. Acesse o [Console do Google Cloud](https://console.cloud.google.com/).
2. Selecione o projeto do Google Cloud.
3. Na barra de navegação lateral, clique em "Kubernetes Engine".
4. Clique no botão "Criar cluster".
5. Preencha os campos com as seguintes informações:
    * Nome do cluster
    * Região
    * Número de nós
    * Versão do Kubernetes

6. Clique no botão "Criar".

**Seção 3: Verificando o Cluster**

1. Clique no nome do cluster.
2. Verifique se o status do cluster é "Executando".
3. Clique em "Nós" para visualizar os nós do cluster.

**Tópico 2: Configurando Autoescalonamento**

**Seção 1: Visão Geral**

O autoescalonamento ajusta automaticamente o número de nós em um cluster com base na carga de trabalho.

**Seção 2: Passos**

1. Clique no nome do cluster.
2. Clique na guia "Autoescalonamento".
3. Ative o autoescalonamento.
4. Configure as políticas de dimensionamento mínimo e máximo.
5. Clique em "Salvar".

**Parte 2: Parâmetros de Configuração Avançados**

**Tópico 3: Configurando o balanceamento de carga**

**Seção 1: Visão Geral**

O balanceamento de carga distribui o tráfego entre os nós do cluster.

**Seção 2: Passos**

1. Clique no nome do cluster.
2. Clique na guia "Balanceamento de carga".
3. Defina o tipo de balanceamento de carga.
4. Configure os certificados SSL (se necessário).
5. Configure os IPs estáticos (se necessário).
6. Clique em "Salvar".

**Tópico 4: Configurando o registro em log**

**Seção 1: Visão Geral**

O registro em log registra os eventos do cluster para fins de depuração e auditoria.

**Seção 2: Passos**

1. Clique no nome do cluster.
2. Clique na guia "Registro em log".
3. Selecione o nível de registro em log.
4. Selecione o destino do registro em log (por exemplo, Cloud Logging).
5. Clique em "Salvar".

**Tópico 5: Gerenciando Role Binding**

**Seção 1: Visão Geral**

As role bindings atribuem permissões a usuários, grupos e contas de serviço.

**Seção 2: Passos**

1. Clique no nome do cluster.
2. Clique na guia "Identidade e autorização".
3. Clique em "Role Bindings".
4. Crie uma nova role binding e atribua as permissões necessárias.
5. Clique em "Salvar".