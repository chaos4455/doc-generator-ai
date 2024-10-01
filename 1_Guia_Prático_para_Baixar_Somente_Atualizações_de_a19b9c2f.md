# Guia Prático para Baixar Somente Atualizações de Segurança no CentOS
Usando o comando `yum download-only --security`

## Visão Geral

O comando `yum download-only --security` permite que você baixe apenas as atualizações de segurança para o seu sistema CentOS, sem realmente instalá-las. Isso pode ser útil se você quiser inspecionar as atualizações antes de instalá-las ou se você tiver uma quantidade limitada de espaço em disco e quiser economizar espaço.

## Pré-requisitos

Para usar o comando `yum download-only --security`, você precisará dos seguintes pré-requisitos:

- Um sistema CentOS com o yum instalado.
- Acesso a um repositório de software do CentOS que contenha atualizações de segurança.

## Como usar o comando `yum download-only --security`

Para baixar somente as atualizações de segurança usando o comando `yum download-only --security`, siga estas etapas:

1. Abra um terminal.
2. Execute o seguinte comando:

```
sudo yum download-only --security
```

3. O comando `yum` irá baixar todas as atualizações de segurança disponíveis para o seu sistema. O progresso do download será exibido no terminal.
4. Depois que o download for concluído, você pode encontrar os arquivos de atualização no diretório `/var/cache/yum`.

## Exemplos

Aqui estão alguns exemplos de como usar o comando `yum download-only --security`:

- Para baixar todas as atualizações de segurança disponíveis, execute o seguinte comando:

```
sudo yum download-only --security
```

- Para baixar apenas as atualizações de segurança para um pacote específico, execute o seguinte comando:

```
sudo yum download-only --security pacote-nome
```

- Para baixar todas as atualizações de segurança para um conjunto específico de pacotes, execute o seguinte comando:

```
sudo yum download-only --security pacote1 pacote2 pacote3
```

## Ícones e Emojis

Aqui estão alguns ícones e emojis que podem ser usados para estilizar este manual:

- 💻 Ícone de computador para representar o sistema CentOS
- 📥 Ícone de download para representar o processo de download
- 🔒 Ícone de cadeado para representar atualizações de segurança
- 🔍 Ícone de lupa para representar inspeção
- 💾 Ícone de disco para representar espaço em disco

## Diagrama de Árvore

O seguinte diagrama de árvore mostra o processo de download de atualizações de segurança usando o comando `yum download-only --security`:

```
                  Download de Atualizações de Segurança
                                 |
                                 V
                   +---------------------+
                   | yum download-only --security |
                   +---------------------+
                                 |
                                 V
                       +--------------+
                       | Baixar arquivos |
                       +--------------+
                                 |
                                 V
                       +---------------+
                       | Inspecionar arquivos |
                       +---------------+  
```