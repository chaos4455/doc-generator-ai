## Guia Prático para Listagem de Patches com `pkg list -g`

**Objetivo:** Mostrar como listar patches disponíveis para grupos específicos no sistema de gerenciamento de pacotes.

### Etapas:

1. Abra um terminal.
2. Execute o comando:

```
pkg list -g <grupo>
```

Onde `<grupo>` é o nome do grupo para o qual deseja listar os patches.

### Exemplos:

**Listar patches para o grupo "security":**

```
pkg list -g security
```

**Listar patches para o grupo "base":**

```
pkg list -g base
```

**Listar patches para todos os grupos:**

```
pkg list -g all
```

### Saída:

O comando produzirá uma lista de patches disponíveis para o grupo especificado, com as seguintes informações:

- **Name:** Nome do patch
- **Origin:** Origem do patch (por exemplo, "openindiana" ou "upstream")
- **Version:** Versão do patch
- **Summary:** Breve descrição do patch

### Opções adicionais:

- **-v:** Exibir informações adicionais, como dependências e checksums.
- **--only-installed:** Listar apenas os patches instalados.
- **--format=json:** Exibir a saída em formato JSON.

### Gráfico de Árvore:

```
               pkg list -g
                  |
                  |
         ┌───────────┴───────────┐
         │                         │
         │      Listar patches      │
         │                         │
         └───────────┬───────────┘
                        |
                    ┌──>──┐
              ┌─────│      │─────┐
              │     │ L I S T A │     │
              └─────│      │─────┘
                    └──>──┘
                        |
                    ┌───────┐
            ┌───────│       │───────┐
            │       │Patches │       │
            │       │        │       │
            │       └───────┘       │
            │                         │
            └───────────────────────┘
```

### Ícones e Emojis:

- 📦 Pacote
- ⚙️ Patch
- 🔍 Pesquisa