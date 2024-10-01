**Como Baixar Atualizações sem Instalar Imediatamente Usando o Yum**

**Introdução**

O Yum é um gerenciador de pacotes para sistemas Linux que permite atualizar, instalar e remover pacotes de software. Ele pode ser usado para baixar atualizações de software sem instalá-las imediatamente. Isso pode ser útil se você quiser baixar as atualizações em um momento diferente ou se quiser inspecionar os pacotes antes de instalá-los.

**Passos**

1. **Abra o Terminal**

Abra o Terminal em seu sistema Linux.

2. **Use o Comando `yum download-only --security`**

Digite o seguinte comando para baixar todos os pacotes de patch de segurança disponíveis:

```bash
yum download-only --security
```

**Opções:**

* **--security:** Esta opção limita o download aos pacotes de patch de segurança.
* **--allowerasing:** Esta opção permite que o Yum exclua pacotes antigos para liberar espaço.

3. **Inspecione os Pacotes Baixados**

Os pacotes baixados serão armazenados no diretório `/var/cache/yum`. Você pode inspecioná-los usando o seguinte comando:

```bash
ls /var/cache/yum
```

**Exemplo:**

```bash
ls /var/cache/yum
cobbler-core-2.5.0-45.el7.x86_64.rpm
cobbler-dns-2.5.0-45.el7.x86_64.rpm
cobbler-ks-2.5.0-45.el7.x86_64.rpm
```

**Instalação das Atualizações**

Para instalar as atualizações baixadas, execute o seguinte comando como root:

```bash
yum install /var/cache/yum/*
```

**Conclusão**

Usando o comando `yum download-only --security`, você pode baixar atualizações de software sem instalá-las imediatamente. Isso pode ser útil para gerenciar atualizações em um cronograma diferente ou para inspecionar os pacotes antes da instalação.