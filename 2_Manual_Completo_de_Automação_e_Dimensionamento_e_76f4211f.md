## 2. Automação e Dimensionamento de Aplicativos em Contêineres no GKE

### Tópicos

- Configuração do Cluster para dimensionamento automático
- Configuração de dimensionamento horizontal automático (HPA)
- Configuração de dimensionamento vertical automático (VPA)
- Automação de implantações com GitOps

### Seções

#### 2.1 Configuração do Cluster para Dimensionamento Automático

**Objetivo:** Preparar o cluster GKE para dimensionamento automático.

**Passos:**

1. Crie um cluster GKE com a opção de "Provisionamento de Node" habilitado.
   - 💻 Comando:
     ```
     gcloud container clusters create CLUSTER_NAME \
       --node-pool=default-pool \
       --num-nodes=3 \
       --provisioning-model=PROVISIONING_MODEL
     ```

2. Instale o [Cluster Autoscaler](https://cluster-autoscaler.sigs.k8s.io/).
   - 💻 Comando:
     ```
     kubectl apply -f https://raw.githubusercontent.com/kubernetes/autoscaler/master/cluster-autoscaler/cloud/gke/gke-autoscaler-ksa.yaml
     ```

#### 2.2 Configuração de Dimensionamento Horizontal Automático (HPA)

**Objetivo:** Dimensionar automaticamente o número de réplicas do Pod com base na carga.

**Passos:**

1. Crie um HPA para um determinado Deployment ou StatefulSet.
   - 💻 Comando:
     ```
     kubectl autoscale deployment DEPLOYMENT_NAME --cpu-percent=TARGET_CPU_PERCENTAGE --min=MIN_REPLICAS --max=MAX_REPLICAS
     ```

2. Ajuste os parâmetros de dimensionamento, como porcentagem de CPU, limite mínimo e máximo de réplicas.

#### 2.3 Configuração de Dimensionamento Vertical Automático (VPA)

**Objetivo:** Dimensionar automaticamente os recursos (por exemplo, CPU, memória) alocados para um Pod com base na carga.

**Passos:**

1. Instale o [Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler).
   - 💻 Comando:
     ```
     kubectl apply -f https://raw.githubusercontent.com/kubernetes/autoscaler/master/vertical-pod-autoscaler/deploy/vpa-stereotype.yaml
     ```

2. Crie um VPA para um determinado Pod.
   - 💻 Comando:
     ```
     kubectl autoscale vpa POD_NAME --cpu=TARGET_CPU_LIMIT --memory=TARGET_MEMORY_LIMIT
     ```

#### 2.4 Automação de Implantações com GitOps

**Objetivo:** Automatizar implantações atualizando um repositório Git.

**Passos:**

1. Crie um repositório Git para o código e os manifestos do Kubernetes.
2. Instale o [Flux CD](https://fluxcd.io/) em seu cluster GKE.
   - 💻 Comando:
     ```
     flux install
     ```
3. Configure o Flux CD para observar o repositório Git.
   - 💻 Comando:
     ```
     flux create source GIT_URL
     ```

4. Crie um Pipeline para implantar automaticamente o código e os manifestos do Kubernetes.
   - 💻 Comando:
     ```
     flux create helmrelease DEPLOYMENT_NAME --chart=CHART_NAME
     ```

### Exemplos

- **HPA para um aplicativo da Web:**
  - Dimensiona automaticamente o número de réplicas do Pod com base no tráfego da web.

- **VPA para um banco de dados PostgreSQL:**
  - Dimensiona automaticamente os recursos do Pod de banco de dados com base na carga do banco de dados.

- **GitOps para uma implantação multicluster:**
  - Automatiza implantações em vários clusters GKE atualizando um repositório Git central.

### Diagramas de Árvore

**Árvore de Dimensionamento Automático**

```
Dimensionamento Automático
    ├── Horizontal (HPA)
    │   ├── CPU Percentual
    │   ├── Limite Mínimo de Réplicas
    │   └── Limite Máximo de Réplicas
    └── Vertical (VPA)
        ├── Limite de CPU
        └── Limite de Memória
```

**Árvore de Automação de Implantação**

```
Automação de Implantação
    ├── GitOps
    │   ├── Repositório Git
    │   ├── Flux CD
    │   └── Pipeline de Implantação
    └── Outros Métodos
        ├── Jenkins
        ├── CircleCI
        └── Azure DevOps
```

### Ícones e Emojis

- ⚙️ Cluster Autoscaler
- 📈 HPA
- ⚖️ VPA
- 💾 GitOps
- 🔮 Flux CD