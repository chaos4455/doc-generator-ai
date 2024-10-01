**Guia Prático de Gerenciamento de Patches no Solaris usando Shell**

![Ícone de patch do Solaris](https://cdn-icons-png.flaticon.com/512/1876/1876938.png)

## 2. Gerenciamento de Patches no Solaris usando Shell

### 2.1 Pré-requisitos

- Acesso root ao sistema Solaris
- Shell bash ou equivalente
- Conectividade com a Internet

### 2.2 Diretórios e Arquivos de Patches

| Diretório/Arquivo | Descrição |
|---|---|
| `/var/sadm/patch` | Diretório que contém os arquivos de patch baixados |
| `/usr/sadm/install` | Diretório que contém os arquivos de patch instalados |
| `solaris_update.xml` | Arquivo XML que contém informações sobre os patches disponíveis |
| `solaris_patch.conf` | Arquivo de configuração que especifica as opções de gerenciamento de patches |

### 2.3 Baixando Patches

Para baixar os patches, execute o seguinte comando:

```bash
sdadm update
```

Este comando irá buscar a lista de patches disponíveis a partir do repositório de patches do Solaris. Você será solicitado a aceitar o acordo de licença.

### 2.4 Instalando Patches

Para instalar os patches baixados, execute o seguinte comando:

```bash
sdadm install-patch -c
```

O sinalizador `-c` irá verificar e corrigir automaticamente as dependências de patch.

### 2.5 Listando Patches Instalados

Para listar os patches instalados, execute o seguinte comando:

```bash
sdadm list-patch
```

### 2.6 Desinstalando Patches

Para desinstalar um patch, execute o seguinte comando:

```bash
sdadm uninstall-patch <nome_do_patch>
```

### 2.7 Automatizando o Gerenciamento de Patches

Você pode automatizar o gerenciamento de patches usando o recurso `autopatch` do Solaris. Para ativá-lo, execute o seguinte comando:

```bash
/usr/lib/autopatch/bin/autopatchadmin start
```

O `autopatch` irá verificar e instalar patches automaticamente em intervalos regulares.

### 2.8 Exemplos

**Exemplos de comandos:**

- Baixar todos os patches disponíveis:
  ```bash
  sdadm update -a
  ```

- Instalar um patch específico:
  ```bash
  sdadm install-patch <nome_do_patch>
  ```

- Desinstalar um patch específico:
  ```bash
  sdadm uninstall-patch <nome_do_patch>
  ```

- Verificar atualizações de patch pendentes:
  ```bash
  sdadm check-update
  ```

- Ativar o `autopatch`:
  ```bash
  /usr/lib/autopatch/bin/autopatchadmin start
  ```

### 2.9 Fluxograma de Gerenciamento de Patches

![Fluxograma de gerenciamento de patches](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Gerenciamento%20de%20Patches%20no%20Solaris%20usando%20Shell#R1.2z63GYq2-MWJ2G5ZcDf76C_FxVhAaXgBJ1ucfS_K9lZNsW6jaSJ_pWEx5n0wZg99jAup31vcGNyAoBDA_u-X80wYiD7SFOo39BkiWJ8B6YTNwup45G7qh6qDmW5Evr2xtpO0L7K-S_4p2pcA_X8M)

### 2.10 Recursos Adicionais

- [Documentação do Solaris 11 Patch Management](https://docs.oracle.com/cd/E53394_01/html/E54764/index.html)
- [Página de manual do SDADM(1M)](https://man.openbsd.org/sdadm.1m)
- [Autopatch no Solaris](https://www.oracle.com/technetwork/server-storage/solaris/documentation/patching.html)