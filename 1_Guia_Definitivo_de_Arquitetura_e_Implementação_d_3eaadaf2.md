**Guia Definitivo de Arquitetura e Implementação do Google Cloud VCP GKE**

## Tópicos

**1. Arquitetura e Implementação do Google Cloud VCP GKE**

### Seções

**1.1 Introdução**
**1.2 Arquitetura do GKE**
**1.3 Criação de um Cluster GKE**
**1.4 Gerenciamento de Clusters GKE**
**1.5 Implementação de Aplicações no GKE**
**1.6 Monitoramento e Registro em Log do GKE**
**1.7 Segurança do GKE**
**1.8 Melhores Práticas do GKE**
**1.9 Certificações do GKE**
**1.10 Recursos**

### Exemplos

**1.1.1 Arquitetura de um cluster GKE**
**1.1.2 Criação de um cluster GKE usando o Google Cloud Console**
**1.1.3 Gerenciamento de nós em um cluster GKE**
**1.1.4 Implementação de um aplicativo do Kubernetes em um cluster GKE**
**1.1.5 Monitoramento de métricas em um cluster GKE**
**1.1.6 Implementação de segurança em um cluster GKE**
**1.1.7 Melhores práticas para escalar clusters GKE**
**1.1.8 Certificações VCP GKE disponíveis**
**1.1.9 Recursos para preparação da certificação VCP GKE**

### Snippets

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: gcr.io/my-project/my-image
```

```bash
kubectl create deployment my-deployment --image=gcr.io/my-project/my-image
```

```json
{
  "kind": "Cluster",
  "apiVersion": "v1",
  "name": "my-cluster",
  "locations": ["us-central1-a"]
}
```

### Tabelas

| Recurso | Descrição |
|---|---|
| Nó | Uma máquina virtual que hospeda pods do Kubernetes |
| Pod | Um grupo de um ou mais containers que são executados juntos |
| Serviço | Uma abstração de um conjunto de pods |
| Implantação | Um conjunto de pods idênticos que são gerenciados como uma única entidade |
| ConfigMap | Um objeto que armazena dados de configuração |
| Secrets | Um objeto que armazena dados confidenciais |

### Diagramas de Árvore

**Diagrama de Árvore da Arquitetura do GKE**

```
                     GKE
                      |
               +-------+-------+
               |      |      |
            Kubernetes Kubernetes Kubernetes
                |         |
        +------+ +------+ +------+
        | Nó 01| | Nó 02| | Nó 03|
        |      | |      | |      |
      +-----+ +-----+ +-----+
      | Pod | | Pod | | Pod |
```

## Ícones e Emojis

**Ícones**

* 🌐 Google Cloud
* ☸️ Kubernetes
* 🛡️ Segurança
* 📊 Monitoramento

**Emojis**

* 👍 Melhor Prática
* 🎓 Certificação
* 📝 Recursos
* 💡 Dica