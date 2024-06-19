**Subtema 2: Usando Serviços VCP GKE**

**Introdução**

Os serviços VCP GKE são recursos gerenciados pelo Google Cloud que fornecem funcionalidade avançada para clusters GKE. Eles simplificam o gerenciamento de cluster, fornecem recursos adicionais e aprimoram a segurança.

**Serviços VCP GKE**

**Cluster Autoscaler:**

* Ajusta automaticamente o número de nós em um cluster com base na carga de trabalho.
* Reduz custos provisionando menos nós quando a carga de trabalho é baixa.

**Config Sync:**

* Aplica configurações consistentes a todos os nós do cluster.
* Centraliza o gerenciamento de configuração e reduz o risco de erros de configuração.

**Private Cloud:**

* Cria um cluster GKE isolado em seu próprio projeto VPC.
* Fornece isolamento de rede aprimorado e controle de acesso.

**Resource Metrics Explorer:**

* Fornece insights detalhados sobre o uso de recursos do cluster.
* Ajuda na otimização do desempenho e na redução de custos.

**Advogados de Segurança:**

* Monitora constantemente clusters GKE em busca de vulnerabilidades e ameaças.
* Detecta e alerta sobre atividades suspeitas, permitindo uma resposta rápida.

**Usando Serviços VCP GKE**

**Habilite o Cluster Autoscaler**

1. Crie um objeto de configuração `ClusterAutoscaler` em seu cluster:
```
kubectl apply -f https://gist.githubusercontent.com/claudioed/45da780d5a1986c7a8e7e30b1343204d/raw/cluster-autoscaler-config.yaml
```

2. Verifique o status do autoscaler:
```
kubectl get clusterautoscaler -o yaml
```

**Habilite o Config Sync**

1. Instale o plug-in Config Sync:
```
kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-config-sync/master/deploy/manifests/gke/config-sync-crd.yaml
kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-config-sync/master/deploy/manifests/gke/config-sync-daemonset.yaml
```

2. Crie um recurso de Config Sync:
```
kubectl apply -f https://gist.githubusercontent.com/claudioed/45da780d5a1986c7a8e7e30b1343204d/raw/config-sync-config.yaml
```

**Crie um Cluster Private Cloud**

1. Crie uma rede VPC e sub-redes:
   - Rede VPC: `gcloud compute networks create my-vpc --subnet-mode custom`
   - Sub-redes: `gcloud compute networks subnets create my-subnet --network my-vpc --region us-central1`

2. Crie um cluster GKE em um projeto privado:
```
gcloud container clusters create my-cluster --cluster-version latest --zone us-central1-a --project my-project --network my-vpc --subnetwork my-subnet --private-cluster
```

**Use o Resource Metrics Explorer**

1. Navegue para **Menu de Navegação** > **GKE Hub** > **Resource Metrics Explorer**.
2. Selecione seu cluster na lista suspensa.
3. Explore métricas de utilização de CPU, memória e armazenamento.

**Use Defensores de Segurança**

1. Instale o plug-in Security Defenders:
```
kubectl apply -f https://g.co/cloud/container-security-scanner-agent
```

2. Monitore alertas de segurança em **Menu de Navegação** > **GKE Hub** > **Security Defenders**.