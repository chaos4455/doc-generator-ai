## Manual de Melhores Práticas: Gerenciamento de Clusters GKE para Arquitetos de Nuvem

### Tema 1: Melhores Práticas para Gerenciamento de Clusters GKE no Google Cloud

### Introdução

O Google Kubernetes Engine (GKE) é um serviço gerenciado que fornece uma plataforma para executar cargas de trabalho do Kubernetes no Google Cloud. Para garantir a operação eficiente e segura dos clusters GKE, é essencial seguir as melhores práticas de gerenciamento descritas neste manual.

### Seção 1: Criação e Configuração do Cluster

**Melhores Práticas:**

- Use o Console do Google Cloud ou o gcloud para criar clusters.
- Use uma versão suportada do Kubernetes e atualize-a regularmente.
- Configure a alta disponibilidade para nós mestres e de trabalho.
- Ative o monitoramento e o registro em log para rastrear a saúde do cluster.
- Use rótulos e anotações para organizar e identificar recursos de cluster.

**Exemplos:**

- Criar um cluster usando o Console do Google Cloud:
  ```
  gcloud container clusters create CLUSTER_NAME \
  --num-nodes=3 \
  --machine-type=e2-standard-4 \
  --location=us-central1
  ```

- Configurar alta disponibilidade para nós mestres:
  ```
  gcloud container clusters update CLUSTER_NAME \
  --update-master-authorized-networks=MASTER_NETWORK \
  --master-ipv4-cidr=CIDR_RANGE
  ```

### Seção 2: Gerenciamento de Nodes

**Melhores Práticas:**

- Escalonar automaticamente o número de nós para atender à demanda.
- Substituir nós com falha ou antigos automaticamente.
- Definir limites de recursos para nós para evitar uso excessivo.
- Aplicar patches de segurança e atualizações regularmente.
- Monitorar o uso de recursos e a saúde dos nós.

**Exemplos:**

- Escalonar automaticamente o número de nós:
  ```
  gcloud container clusters update CLUSTER_NAME \
  --autoscaling-min-nodes=2 \
  --autoscaling-max-nodes=5
  ```

- Aplicar patches de segurança:
  ```
  gcloud container clusters upgrade cluster CLUSTER_NAME
  ```

### Seção 3: Gerenciamento de Pods e Contêineres

**Melhores Práticas:**

- Use Agendamentos Automáticos para distribuir pods uniformemente pelos nós.
- Defina políticas de reinicialização e limite de recursos para pods.
- Monitorar o uso de recursos e o estado de integridade dos pods.
- Configurar recursos de rede como balanceamento de carga e políticas de firewall.
- Implementar estratégias de implantação como implantações contínuas e canárias.

**Exemplos:**

- Usar Agendamentos Automáticos:
  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: my-pod
    spec:
      affinity:
        podAntiAffinity:
          preferences:
          - weight: 100
            matchExpressions:
            - key: app
              operator: In
              values:
              - myapp
  ```

- Configurar balanceamento de carga:
  ```
  apiVersion: v1
  kind: Service
  metadata:
    name: my-service
  spec:
    type: LoadBalancer
    selector:
      app: myapp
    ports:
    - port: 80
      targetPort: 8080
  ```

### Seção 4: Gerenciamento de Armazenamento

**Melhores Práticas:**

- Use o PersistentVolumeClaims (PVCs) para provisionar armazenamento persistente para pods.
- Use tipos de volume apropriados, como discos gerenciados ou NFS.
- Implementar uma estratégia de backup e recuperação para dados persistentes.
- Monitorar o uso e a saúde do armazenamento.

**Exemplos:**

- Criar um PVC:
  ```
  apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
    name: my-pv-claim
  spec:
    accessModes:
    - ReadWriteOnce
    storageClassName: my-storage-class
    resources:
      requests:
        storage: 1Gi
  ```

- Implementar uma estratégia de backup:
  ```
  gcloud container clusters create my-cluster \
  --backup-enabled
  ```

### Seção 5: Gerenciamento de Segurança

**Melhores Práticas:**

- Habilitar o Kubernetes Role-Based Access Control (RBAC).
- Use secrets e ConfigMaps para gerenciar dados confidenciais.
- Implementar políticas de rede para restringir o acesso a recursos.
- Monitorar logs e alertas para identificar atividades suspeitas.
- Implementar práticas de segurança em camadas usando tecnologias como Network Policy e Pod Security Policy.

**Exemplos:**

- Criar uma função RBAC:
  ```
  apiVersion: rbac.authorization.k8s.io/v1
  kind: Role
  metadata:
    name: my-role
  rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create", "get", "list"]
  ```

- Usar Pod Security Policy:
  ```
  apiVersion: policy/v1beta1
  kind: PodSecurityPolicy
  metadata:
    name: my-psp
  spec:
    privileged: false
    seLinux:
      rule: RunAsAny
    runAsUser:
      rule: RunAsAny
  ```