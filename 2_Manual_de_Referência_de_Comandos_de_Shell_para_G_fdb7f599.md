**Manual de Referência de Comandos de Shell para Gerenciamento de Patches**

## 2. Gerenciamento de Patches no Solaris usando Shell

**Objetivo**

Este capítulo fornece uma visão geral dos comandos de shell para gerenciar patches no Solaris.

**Tópicos**

* Verificação de Status do Patch
* Instalação de Patches
* Aplicação de Patches
* Gerenciamento de Repositórios de Patches
* Scripting de Gerenciamento de Patches

## 2.1 Verificação de Status do Patch

**Comando: patch**

**Função:** Exibe informações sobre patches instalados e disponíveis.

**Opções:**

* **-e** ou **--effective**: Exibe patches aplicáveis até o momento.
* **-I** ou **--installed**: Exibe patches instalados.
* **-m** ou **--manifest-only**: Exibe apenas informações de manifesto do patch.
* **-p** ou **--patchid**: Exibe uma lista de IDs de patch.

**Exemplo:**

```shell
patch -e
```

**Resultado:**

Lista os patches aplicáveis.

## 2.2 Instalação de Patches

**Comando: pkg install**

**Função:** Instala pacotes de patch.

**Opções:**

* **-g** ou **--group**: Instala todos os patches disponíveis para um determinado grupo.
* **-n** ou **--nodeps**: Não instala dependências para um patch.
* **-y** ou **--assume-yes**: Responde "sim" a todas as perguntas.

**Exemplo:**

```shell
pkg install su-5.11.1.0.0.71.4-sol11.8
```

**Resultado:**

Instala o patch para o pacote "su".

## 2.3 Aplicação de Patches

**Comando: patchadd**

**Função:** Aplica patches instalados.

**Opções:**

* **-e** ou **--exec**: Executa scripts de shell ou comandos personalizados.
* **-f** ou **--force**: Aplica o patch mesmo que haja conflitos.
* **-l** ou **--log**: Registra informações de patch em um arquivo.

**Exemplo:**

```shell
patchadd -l /tmp/patch.log su-5.11.1.0.0.71.4-sol11.8
```

**Resultado:**

Aplica o patch do pacote "su" e registra informações em "/tmp/patch.log".

## 2.4 Gerenciamento de Repositórios de Patches

**Comando: pkgrepo**

**Função:** Gerencia repositórios de patches.

**Opções:**

* **-a** ou **--add**: Adiciona um repositório.
* **-d** ou **--delete**: Remove um repositório.
* **-e** ou **--enable**: Habilita um repositório.
* **-l** ou **--list**: Lista repositórios.

**Exemplo:**

```shell
pkgrepo -a http://pkg.sun.com/solaris/release/ sol11.8
```

**Resultado:**

Adiciona o repositório de patches para o Solaris 11.8.

## 2.5 Scripting de Gerenciamento de Patches

**Shell Scripting:**

* **Exemplo 1:** Script para verificar e instalar todos os patches aplicáveis.

```shell
#!/bin/sh

# Verificar patches aplicáveis
patches=$(patch -e)

# Instalar patches
for patch in $patches; do
  pkg install -g $patch
done
```

* **Exemplo 2:** Script para aplicar um patch e reiniciar o sistema.

```shell
#!/bin/sh

# Aplicar patch
patchadd -f su-5.11.1.0.0.71.4-sol11.8

# Reiniciar o sistema
reboot
```