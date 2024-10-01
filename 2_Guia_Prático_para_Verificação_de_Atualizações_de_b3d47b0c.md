## 📝 Guia Prático de Verificação de Atualizações de Segurança com Yum

**Objetivo:** Verificar e instalar atualizações de segurança para manter seu sistema seguro e protegido.

**Ferramenta:** Yum (Yellowdog Update Manager)

### Etapas:

**1. Verificar Atualizações:**

* Execute o comando `yum check-update`:

```
$ yum check-update
```

* O Yum listará todas as atualizações disponíveis, incluindo atualizações de segurança.

**2. Exibir Atualizações de Segurança:**

* Para filtrar apenas atualizações de segurança, use o comando `yum check-update --security`:

```
$ yum check-update --security
```

**3. Instalar Atualizações:**

* Para instalar todas as atualizações disponíveis, incluindo atualizações de segurança, execute:

```
$ sudo yum update
```

* Para instalar apenas atualizações de segurança, execute:

```
$ sudo yum update --security
```

### Exemplos:

**1. Verificar Todas as Atualizações:**

```
$ yum check-update
```

**Resultado:**

```
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirror.yourhost.com
 * extras: mirror.yourhost.com
 * updates: mirror.yourhost.com
Updates Available:
Name               Arch            Version       Repository      Size
postfix            x86_64          3.4.13-1.el7    updates        162 k
...
```

**2. Verificar Atualizações de Segurança:**

```
$ yum check-update --security
```

**Resultado:**

```
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirror.yourhost.com
 * extras: mirror.yourhost.com
 * updates: mirror.yourhost.com
Security Updates Available:
Name               Arch            Version       Repository      Size
kernel-headers      x86_64          2.6.32-504.3.1.el6_9  updates        1.5 M
...
```

**3. Instalar Todas as Atualizações:**

```
$ sudo yum update
```

**4. Instalar Apenas Atualizações de Segurança:**

```
$ sudo yum update --security
```

### Ícones e Emojis:

* 🛡️ Atualização de segurança
* 🛠️ Yum
* 🔎 Verificação
* ✅ Instalação
* 🚫 Não instalado