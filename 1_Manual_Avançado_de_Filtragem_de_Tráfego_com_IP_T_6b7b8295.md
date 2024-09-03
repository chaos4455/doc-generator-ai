## 📚 Manual Avançado de Filtragem de Tráfego com IP Tables: Subtema 2 - Filtragem de Tráfego Avançada com IP Tables

### 📊 Introdução

Esta seção abrange recursos avançados do IP Tables, permitindo que você configure regras de filtragem mais complexas e aprimoradas.

### 🛠️ Recursos Avançados de Filtragem

#### 🌐 Filtragem baseada em estados de conexão

O IP Tables permite filtrar o tráfego com base no estado da conexão. Os estados de conexão incluem:

- NEW: Nova conexão
- ESTABLISHED: Conexão estabelecida
- RELATED: Conexão relacionada (por exemplo, FTP de dados)

**Sintaxe:**

```
iptables -m state --state [estado] [opções]
```

**Exemplo:**

Permitir apenas novas conexões:
```
iptables -A INPUT -m state --state NEW -j ACCEPT
```

#### 🌐 Filtragem por fragmentos

Você pode filtrar fragmentos de pacotes, que são pacotes incompletos. Isso é útil para detectar ataques de fragmentação.

**Sintaxe:**

```
iptables -m fragment [opções]
```

**Exemplo:**

Dropar todos os fragmentos de pacotes:
```
iptables -A INPUT -m fragment -j DROP
```

#### 🌐 Filtragem por marcação de pacotes

As marcas de pacotes podem ser usadas para identificar e controlar pacotes específicos. Você pode marcar pacotes usando o argumento `-m mark`.

**Sintaxe:**

```
iptables -m mark --mark [marca] [opções]
```

**Exemplo:**

Marcar todos os pacotes de uma interface específica:
```
iptables -A INPUT -i eth0 -j MARK --set-mark 0x123
```

#### 🌐 Filtragem por tempo

Você pode filtrar o tráfego com base na hora do dia ou da semana. Isso é útil para implementar políticas de controle de acesso ou bloquear ataques durante determinados horários.

**Sintaxe:**

```
iptables -m time [opções]
```

**Exemplo:**

Bloquear o tráfego entre 23h e 7h:
```
iptables -A INPUT -m time --timestart 23:00 --timestop 07:00 -j DROP
```

#### 🌐 Filtragem por MAC

Você pode filtrar o tráfego com base no endereço MAC do dispositivo de origem ou destino. Isso é útil para controlar o acesso de dispositivos específicos.

**Sintaxe:**

```
iptables -m mac --mac-source [endereço MAC]
iptables -m mac --mac-destination [endereço MAC]
```

**Exemplo:**

Permitir tráfego apenas do dispositivo com MAC 00:11:22:33:44:55:
```
iptables -A INPUT -m mac --mac-source 00:11:22:33:44:55 -j ACCEPT
```

#### 🌐 Filtragem por interfaces

Você pode filtrar o tráfego com base na interface de rede em que ele chega ou sai. Isso é útil para isolar o tráfego em interfaces específicas.

**Sintaxe:**

```
iptables -i [interface]
iptables -o [interface]
```

**Exemplo:**

Bloquear o tráfego na interface `eth1`:
```
iptables -A INPUT -i eth1 -j DROP
```

#### 🌐 Filtragem por protocolos

Você pode filtrar o tráfego com base no protocolo de rede, como TCP, UDP ou ICMP. Isso é útil para implementar políticas de segurança ou bloquear protocolos específicos.

**Sintaxe:**

```
iptables -p [protocolo]
```

**Exemplo:**

Permitir apenas tráfego TCP:
```
iptables -A INPUT -p tcp -j ACCEPT
```

#### 🌐 Filtragem por portas

Você pode filtrar o tráfego com base na porta de origem ou destino. Isso é útil para bloquear portas específicas ou controlar o acesso a serviços específicos.

**Sintaxe:**

```
iptables -m tcp --dport [porta]
iptables -m udp --dport [porta]
```

**Exemplo:**

Bloquear o tráfego na porta 80 (HTTP):
```
iptables -A INPUT -p tcp --dport 80 -j DROP
```

#### 🌐 Filtragem por faixa de endereços

Você pode filtrar o tráfego com base em uma faixa de endereços IP de origem ou destino. Isso é útil para bloquear ou permitir o tráfego de faixas específicas de endereços IP.

**Sintaxe:**

```
iptables -s [endereço IP inicial]-[endereço IP final]
iptables -d [endereço IP inicial]-[endereço IP final]
```

**Exemplo:**

Bloquear o tráfego da faixa de endereços IP 10.0.0.0-10.0.0.255:
```
iptables -A INPUT -s 10.0.0.0-10.0.0.255 -j DROP
```

#### 🌐 Filtragem por máscaras de sub-rede

Você pode filtrar o tráfego com base na máscara de sub-rede de origem ou destino. Isso é útil para controlar o tráfego de sub-redes específicas.

**Sintaxe:**

```
iptables -s [endereço IP]/[máscara de sub-rede]
iptables -d [endereço IP]/[máscara de sub-rede]
```

**Exemplo:**

Permitir o tráfego da sub-rede 192.168.1.0/24:
```
iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT
```