**Manual Essencial de Configuração e Gerenciamento de IP Tables**

**Tema:** Operações básicas de gerenciamento de IP Tables

**Diagrama de Árvore**

```
Operações Básicas de IP Tables
    ↳ Visualização de regras de IP Tables
    ↳ Adição de novas regras
    ↳ Remoção de regras existentes
    ↳ Substituição de regras
    ↳ Limpeza de todas as regras
    ↳ Ativar/Desativar IP Tables
```

**Seção 1: Visualização de Regras de IP Tables**

**Comando:** `iptables -L`

**Exemplo:**

```
$ iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     tcp  --  anywhere             anywhere             state NEW,ESTABLISHED 
ACCEPT     udp  --  anywhere             anywhere             state NEW,ESTABLISHED 

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             anywhere            
```

**Seção 2: Adição de Novas Regras**

**Comando:** `iptables -A <cadeia> <regra>`

**Exemplo:**

```
$ iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

**Seção 3: Remoção de Regras Existentes**

**Comando:** `iptables -D <cadeia> <regra>`

**Exemplo:**

```
$ iptables -D INPUT -p tcp --dport 22 -j ACCEPT
```

**Seção 4: Substituição de Regras**

**Comando:** `iptables -R <cadeia> <número da regra> <regra>`

**Exemplo:**

```
$ iptables -R INPUT 1 -p tcp --dport 80 -j ACCEPT
```

**Seção 5: Limpeza de Todas as Regras**

**Comando:** `iptables -F <cadeia>`

**Exemplo:**

```
$ iptables -F INPUT
```

**Seção 6: Ativar/Desativar IP Tables**

**Comando:** `service iptables {start|stop}`

**Exemplo:**

```
$ service iptables start
```