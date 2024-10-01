**Guia Passo a Passo para Atualizações de Segurança em Sistemas Linux Usando Yum**

**1. Verificar Atualizações Pendentes**

* Execute o seguinte comando para verificar atualizações de segurança disponíveis:
```text
yum check-update --security
```

**2. Baixar Atualizações de Segurança**

* Execute o seguinte comando para baixar as atualizações de segurança:
```text
yum download-only --security
```

**3. Instalar Atualizações**

* Execute o seguinte comando para instalar as atualizações de segurança baixadas:
```text
yum localinstall --security
```

**4. Reiniciar Serviços (Opcional)**

* Se necessário, reinicie os serviços que podem ter sido afetados pelas atualizações.

**5. Verificar Instalação**

* Para verificar se as atualizações de segurança foram instaladas com sucesso, execute o seguinte comando:
```text
yum list installed | grep -i "security"
```

**Diagrama de Fluxo de Atualizações de Segurança Yum**

[Diagrama de Fluxo](URL do Diagrama)

**Exemplo de Comando**

```text
# Verificar atualizações de segurança
yum check-update --security

# Baixar atualizações de segurança
yum download-only --security

# Instalar atualizações de segurança
yum localinstall --security

# Reiniciar serviços afetados (opcional)
service <nome-do-servico> restart

# Verificar instalação
yum list installed | grep -i "security"
```