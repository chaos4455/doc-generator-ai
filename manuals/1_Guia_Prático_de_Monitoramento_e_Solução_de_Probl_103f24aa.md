**Guia Prático de Monitoramento e Solução de Problemas do GKE no Google Cloud VCP**

## 📊 Monitoramento

**Seção 1: Configuração do Monitoramento**

* Ative o **Cloud Monitoring** para clusters GKE:
    * Usando o **gcloud** CLI:
    ```console
    gcloud container clusters update CLUSTER_NAME --monitoring=CLUSTER_LOCATION
    ```
    * No Cloud Console:
    * Acesse o Cluster GKE
    * Role para baixo e ative "Monitoramento"

* Crie **Alertas:**
    * Defina limites e ações para eventos de monitoramento:
    * No Cloud Console: Acesse "Alertas" no menu de navegação
    * No Google Cloud CLI: Use o comando `gcloud monitoring alerts create`

**Seção 2: Coleta de Métricas**

* Use **Metrics Explorer:**
    * Explore e visualize métricas de cluster e nó:
    * No Cloud Console: Acesse "Métricas Explorer" no menu de navegação
* Use **Stackdriver Logging:**
    * Examine logs do Kubernetes e do sistema GKE:
    * No Cloud Console: Acesse "Logs Explorer" no menu de navegação
* Utilize **APIs do Google Cloud:**
    * Colete métricas por meio das APIs:
    * Documentação: [Google Cloud Monitoring API](https://cloud.google.com/monitoring/api/ref_v3)

## 🔧 Solução de Problemas

**Seção 1: Resolução de Problemas do Cluster**

* Verifique o **status do cluster:**
    * Use o comando `kubectl get nodes -o wide` para verificar o status dos nós
* Inspecione **logs:**
    * Examine logs de cluster e nó usando o Stackdriver Logging
* Analise **eventos:**
    * Use o comando `kubectl get events` para verificar eventos e avisos
* **Reinicie nós problemáticos:**
    * Use o comando `kubectl cordon NODE_NAME` para isolar um nó
    * Em seguida, execute `kubectl uncordon NODE_NAME` para reiniciá-lo

**Seção 2: Resolução de Problemas de Pod**

* Verifique o **status do pod:**
    * Use o comando `kubectl get pods -o wide` para verificar o status dos pods
* Examine **logs de contêiner:**
    * Use o comando `kubectl logs POD_NAME` para exibir logs de contêiner
* Verifique **recursos:**
    * Use o comando `kubectl top pods -o wide` para verificar o uso de recursos
* Reimplantar ou **reiniciar pods:**
    * Use os comandos `kubectl delete pod POD_NAME` e `kubectl create ...` para reimplantar
    * Ou use `kubectl rollout restart deployment DEPLOYMENT_NAME` para reiniciar

**Seção 3: Resolução de Problemas de Serviço**

* Verifique o **status do serviço:**
    * Use o comando `kubectl get svc` para verificar o status dos serviços
* Inspecione **endereço IP externo:**
    * Use o comando `kubectl get svc -o yaml SERVICE_NAME` para obter o endereço IP externo
* Teste a **conectividade:**
    * Use ferramentas como cURL ou ping para testar a conectividade com o serviço
* Reimplantar ou **reiniciar serviços:**
    * Use os comandos `kubectl delete svc SERVICE_NAME` e `kubectl create ...` para reimplantar
    * Ou use `kubectl rollout restart deployments SVC_NAME` para reiniciar

**Seção 4: Resolução de Problemas de Rede**

* Verifique **políticas de rede:**
    * Examine as políticas de rede usando o comando `kubectl get networkpolicies`
* Inspecione **roteamento:**
    * Use o comando `kubectl exec -it POD_NAME -- nslookup SERVICE_NAME` para verificar o roteamento
* **Teste a conectividade:**
    * Use ferramentas como traceroute ou ping para testar a conectividade de rede
* Reimplantar ou **reiniciar pods e serviços:**
    * Reimplantar ou reiniciar pods e serviços afetados, conforme necessário

**Seção 5: Resolução de Problemas de Armazenamento**

* Verifique **volumes persistentes:**
    * Use o comando `kubectl get pv,pvc` para verificar o status dos volumes
* Inspecione **logs de nó e pod:**
    * Examine logs em busca de erros relacionados a armazenamento
* Verifique **reivindicações:**
    * Use o comando `kubectl get pvc` para verificar o status das reivindicações
* Reimplantar ou **reiniciar pods e serviços:**
    * Reimplantar ou reiniciar pods e serviços afetados, conforme necessário