**Manual de Gerenciamento de Patches com `pkg list -g`**

**Seção 1: Introdução**

Este manual fornece instruções detalhadas sobre como usar o comando `pkg list -g` para listar patches disponíveis por grupo no sistema operacional FreeBSD.

**Seção 2: Pré-requisitos**

Antes de usar o comando `pkg list -g`, você deve garantir que:

- O sistema FreeBSD está atualizado
- Os repositórios de pacotes estão configurados corretamente

**Seção 3: Sintaxe do Comando**

```
pkg list -g [opções] [grupo]
```

**Seção 4: Opções de Comando**

| Opção | Descrição |
|---|---|
| `-a` | Listar todos os patches disponíveis |
| `-c` | Listar patches instalados |
| `-v` | Mostrar informações detalhadas sobre patches |
| `-w` | Mostrar informações sobre patches aguardando instalação |

**Seção 5: Exemplos de Uso**

**Exemplo 1: Listar todos os patches disponíveis**

```
pkg list -g -a
```

**Exemplo 2: Listar patches instalados**

```
pkg list -g -c
```

**Exemplo 3: Listar patches detalhados**

```
pkg list -g -v
```

**Exemplo 4: Listar patches aguardando instalação**

```
pkg list -g -w
```

**Exemplo 5: Listar patches disponíveis para um grupo específico**

```
pkg list -g security
```

**Diagrama de Árvore do Fluxo de Trabalho do Comando `pkg list -g`**

![Diagrama de Árvore do Fluxo de Trabalho do Comando `pkg list -g`](https://i.imgur.com/example_tree_diagram.png)

**Seção 6: Resolução de Problemas**

Se você encontrar algum problema ao usar o comando `pkg list -g`, tente as seguintes etapas de solução de problemas:

- Verifique se o sistema está atualizado
- Verifique se os repositórios de pacotes estão configurados corretamente
- Execute o comando `pkg update` para atualizar o banco de dados de pacotes
- Execute o comando `pkg upgrade` para instalar os patches disponíveis