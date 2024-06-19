## Manual Técnico de Gerenciamento de Cluster do GKE

**2. Gerenciamento de Cluster do GKE**

### Introdução

O Google Kubernetes Engine (GKE) é um serviço gerenciado que permite implantar e gerenciar clusters do Kubernetes no Google Cloud Platform (GCP). Este manual fornece instruções detalhadas sobre como gerenciar clusters do GKE, incluindo criação, exclusão, atualização e dimensionamento.

### Criação de um Cluster

**Pré-requisitos:**

* Uma conta do GCP
* Projeto do GCP
* Zona ou região do GCP

**Passos:**

1. **Crie um cluster:** Use o Google Cloud Console ou a CLI do gcloud para criar um cluster. Forneça um nome, zona ou região e os parâmetros de máquina virtual desejados.
2. **Defina as configurações avançadas:** Ajuste as configurações avançadas do cluster, como o número de nós, o tipo de nó, as políticas de rede e as configurações de segurança.
3. **Aguarde a criação do cluster:** O GKE leva alguns minutos para criar o cluster.

#### Diagrama de Fluxo de Criação de Cluster

[Diagrama de Fluxo de Criação de Cluster](diagrama-criacao-cluster.png)

### Exclusão de um Cluster

**Passos:**

1. **Excluir o cluster:** Use o Google Cloud Console ou a CLI do gcloud para excluir o cluster.
2. **Confirme a exclusão:** O GKE solicitará que você confirme a exclusão do cluster.
3. **Aguarde a exclusão do cluster:** O GKE leva alguns minutos para excluir o cluster.

### Atualização de um Cluster

**Pré-requisitos:**

* Um cluster do GKE existente

**Passos:**

1. **Verificar a disponibilidade:** Verifique se há atualizações disponíveis para o cluster.
2. **Atualizar o cluster:** Use o Google Cloud Console ou a CLI do gcloud para atualizar o cluster.
3. **Aguarde a atualização do cluster:** O GKE leva algum tempo para atualizar o cluster.

### Dimensionamento de um Cluster

**Passos:**

1. **Escalonar horizontalmente:** Aumente ou diminua o número de nós no cluster para atender à demanda.
2. **Escalonar verticalmente:** Ajuste o tipo de nó para aumentar ou diminuir a capacidade dos nós.
3. **Aguarde a escala do cluster:** O GKE leva algum tempo para dimensionar o cluster.

### Exemplos

**Criação de um Cluster usando o Google Cloud Console:**

1. Acesse o Google Cloud Console.
2. Selecione **Kubernetes Engine** no menu de navegação.
3. Clique em **Criar Cluster**.
4. Forneça as configurações do cluster e clique em **Criar**.

**Exclusão de um Cluster usando a CLI do gcloud:**

1. Abra um terminal.
2. Execute o seguinte comando:
```
gcloud container clusters delete CLUSTER-NAME
```

**Atualização de um Cluster usando o Google Cloud Console:**

1. Acesse o Google Cloud Console.
2. Selecione o cluster que deseja atualizar.
3. Clique na guia **Atualizações**.
4. Verifique se há atualizações disponíveis e clique em **Atualizar**.

**Dimensionamento de um Cluster usando a CLI do gcloud:**

1. Abra um terminal.
2. Execute o seguinte comando para escalonar horizontalmente:
```
gcloud container clusters resize CLUSTER-NAME --num-nodes=NEW-NODE-COUNT
```
3. Execute o seguinte comando para escalonar verticalmente:
```
gcloud container clusters resize CLUSTER-NAME --node-pool=NODE-POOL-NAME --machine-type=NEW-MACHINE-TYPE
```

### Ícones e Emojis

- 🛠️ Criar Cluster
- 🗑️ Excluir Cluster
- ⏫ Atualizar Cluster
- ↕️ Dimensionar Cluster