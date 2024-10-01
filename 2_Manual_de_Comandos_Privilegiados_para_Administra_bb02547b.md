**Manual de Comandos Privilegiados para Administração Avançada**

**Introdução:**

Este manual fornece instruções detalhadas sobre como executar comandos privilegiados como usuário root ou com privilégios elevados. Esses comandos são essenciais para executar tarefas avançadas de administração do sistema, como gerenciamento de usuários, configuração de rede e solução de problemas.

**Pré-requisitos:**

* Acesso root ou privilégios elevados
* Familiaridade com a linha de comando

**Comandos Privilegiados Comuns:**

**Gerenciamento de Usuários:**

- `useradd`: Cria um novo usuário
- `userdel`: Exclui um usuário
- `passwd`: Altera a senha de um usuário
- `chage`: Altera as opções de expiração e envelhecimento da senha de um usuário

**Configuração da Rede:**

- `ifconfig`: Exibe e configura as interfaces de rede
- `route`: Gerencia rotas de rede
- `netstat`: Exibe estatísticas e conexões de rede
- `firewalld`: Gerencia o firewall do sistema

**Gerenciamento do Sistema:**

- `systemctl`: Gerencia serviços e unidades do sistema
- `yum`: Instala, remove e atualiza pacotes de software
- `df`: Exibe o uso do espaço em disco
- `du`: Exibe o espaço em disco usado por arquivos e diretórios

**Solução de Problemas:**

- `top`: Exibe os processos em execução e o uso de recursos
- `ps`: Exibe informações sobre os processos em execução
- `dmesg`: Exibe mensagens do kernel
- `journalctl`: Exibe registros do sistema

**Diagramas de Árvore:**

**Gerenciamento de Usuários**

```
├─useradd
├─userdel
├─passwd
└─chage
```

**Configuração da Rede**

```
├─ifconfig
├─route
├─netstat
└─firewalld
```

**Gerenciamento do Sistema**

```
├─systemctl
├─yum
├─df
└─du
```

**Solução de Problemas**

```
├─top
├─ps
├─dmesg
└─journalctl
```

**Exemplos de Uso:**

**Cria um novo usuário:**

```bash
useradd novo_usuario
```

**Altera a senha de um usuário:**

```bash
passwd usuario_existente
```

**Exibe as interfaces de rede:**

```bash
ifconfig
```

**Gerencia rotas de rede:**

```bash
route add default gw 192.168.1.1
```

**Reinicia um serviço:**

```bash
systemctl restart serviço_servidor
```

**Instala um pacote:**

```bash
yum install pacote
```

**Exibe o uso do espaço em disco:**

```bash
df -h
```

**Exibe o espaço em disco usado por um diretório:**

```bash
du -sh diretório
```

**Exibe os processos em execução:**

```bash
top
```

**Exibe mensagens do kernel:**

```bash
dmesg
```

**Exibe registros do sistema:**

```bash
journalctl -xe
```