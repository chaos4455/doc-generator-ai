## 📝 Manual de IP Tables: Guia Essencial para Iniciantes

**✨ Subtema 1: Introdução e Fundamentos das IP Tables**

---

### 📖 Introdução

**Definição:**

As IP Tables são um poderoso firewall no kernel do Linux usado para manipular e filtrar pacotes de rede com base em critérios específicos.

**Objetivos:**

* Bloquear e permitir acesso a serviços de rede
* Filtrar tráfego com base em endereços IP, portas e protocolos
* Proteger sistemas contra ataques de rede

### ⚡ Fundamentos das IP Tables

**Tabela do Kernel:**

As IP Tables consistem em três tabelas principais:

* **filter:** Filtra pacotes com base em critérios de origem, destino e protocolo
* **nat:** Traduz endereços IP e portas para permitir o encaminhamento de pacotes
* **mangle:** Modifica pacotes para alterar campos como TTL ou marcações

**Correntes:**

Cada tabela é dividida em correntes predefinidas que determinam o fluxo de processamento de pacotes:

* **INPUT:** Pacotes recebidos da interface
* **OUTPUT:** Pacotes enviados da interface
* **FORWARD:** Pacotes roteados pelo sistema

**Regras:**

As regras são usadas para especificar como os pacotes devem ser manipulados:

* **Target:** A ação a ser executada (por exemplo, ACCEPT, DROP, REJECT)
* **Critérios:** Os campos do pacote usados para corresponder (por exemplo, endereço IP, porta, protocolo)

### 🧩 Diagrama de Árvore

```
                    IP Tables
                         |
                         v
               +--------------+----------------+---------------+
               | filter table | nat table | mangle table |
               +--------------+----------------+---------------+
                    |               |                   |
                    v               v                   v
                 correntes    correntes        correntes
               +----+          +----+               +----+
               | IN |          | PREROUTING |          | PREROUTING |
               +----+          +----+               +----+
               | OUT |          | POSTROUTING |          | OUTPUT |
               +----+          +----+               +----+
               | FWD |          | OUTPUT |          | POSTROUTING |
               +----+          +----+               +----+
```

### 🛠️ Exemplos

**Bloquear tráfego de um endereço IP específico:**

```
iptables -A INPUT -s 192.168.0.10 -j DROP
```

**Permitir acesso à porta 80 (HTTP):**

```
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

**Encaminhar todo o tráfego de porta (NAT):**

```
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```

**Alterar o TTL de um pacote (mangle):**

```
iptables -t mangle -A OUTPUT -p tcp -j TTL --ttl-set 60
```

### 📚 Recursos Adicionais

* [Documentação do iptables](https://netfilter.org/projects/iptables/index.html)
* [Tutorial do iptables para iniciantes](https://www.digitalocean.com/community/tutorials/an-iptables-tutorial-for-beginners-part-1-understanding-iptables)
* [Guia de referência do iptables](https://www.kernel.org/doc/Documentation/networking/ip-tables/ip-tables.txt)