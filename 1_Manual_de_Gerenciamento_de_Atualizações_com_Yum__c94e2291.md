**Manual de Gerenciamento de Atualizações com Yum**

**Introdução**

O gerenciamento de atualizações é crucial para manter os sistemas seguros e atualizados. O Yum (Yellowdog Updater Modified) é uma ferramenta poderosa para gerenciar atualizações no Red Hat Enterprise Linux (RHEL) e distribuições derivadas. Este manual fornece instruções detalhadas sobre como verificar, instalar e gerenciar atualizações usando o Yum.

**Verificação de Atualizações**

**1. Comando `yum check-update`**

Este comando verifica os repositórios configurados para atualizações disponíveis. Ele exibe uma lista de pacotes que possuem atualizações disponíveis.

```
$ yum check-update
```

**2. Opção `--security`**

Use esta opção para verificar apenas as atualizações de segurança.

```
$ yum check-update --security
```

**3. Opção `--show-duplicates`**

Esta opção exibe o número de pacotes duplicados disponíveis.

```
$ yum check-update --show-duplicates
```

**Instalação de Atualizações**

**1. Comando `yum update`**

Este comando instala todas as atualizações disponíveis.

```
$ yum update
```

**2. Opção `-y`**

Use esta opção para responder "sim" a todas as alterações e evitar prompts de confirmação.

```
$ yum update -y
```

**3. Opção `--exclude`**

Esta opção exclui pacotes específicos da atualização.

```
$ yum update --exclude package1 package2
```

**Gerenciamento de Atualizações**

**1. Opção `yum history list`**

Este comando exibe o histórico de atualizações instaladas.

```
$ yum history list
```

**2. Opção `yum history info`**

Fornece detalhes sobre uma atualização específica.

```
$ yum history info transaction-id
```

**3. Opção `yum rollback`**

Este comando reverte um pacote para sua versão anterior.

```
$ yum rollback package-name
```

**Diagramas de Árvore**

**Verificação de Atualizações**

```
      Verificar Atualizações
           |
          / \
         /   \
       /     \
      /       \
     /         \
    /           \
  check-update    check-update --security
```

**Instalação de Atualizações**

```
      Instalar Atualizações
           |
          / \
         /   \
       /     \
      /       \
     /         \
    /           \
  update           update -y
```

**Gerenciamento de Atualizações**

```
      Gerenciar Atualizações
           |
          / \
         /   \
       /     \
      /       \
     /         \
    /           \
history list   history info   rollback
```