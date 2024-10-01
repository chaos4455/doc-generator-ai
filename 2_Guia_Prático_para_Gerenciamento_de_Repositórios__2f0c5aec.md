**Guia Prático para Gerenciamento de Repositórios Yum**

**Verificando o Arquivo `/etc/yum.conf` para Segurança do Repositório**

**Objetivo:** Verificar se o repositório de segurança está habilitado no arquivo de configuração do Yum.

**Pré-requisitos:**

* Acesso ao terminal ou shell como usuário root ou com privilégios sudo

**Etapas:**

1. **Abra o arquivo `/etc/yum.conf`.**

```
sudo vim /etc/yum.conf
```

2. **Localize a linha que contém `security`.**

3. **Verifique o valor do seguinte parâmetro:**

```
installonly_limit=
```

4. **Certifique-se de que o valor esteja definido como `1` ou `yes`.**

* Se estiver definido como `0` ou `no`, o repositório de segurança não está habilitado.

**Exemplo:**

```
installonly_limit=1
```

5. **Salve e feche o arquivo.**

**Conclusão:**

Após verificar e, se necessário, habilitar o repositório de segurança, você pode prosseguir com outras tarefas de gerenciamento de repositório Yum com confiança de que os pacotes baixados de repositórios não confiáveis serão bloqueados.