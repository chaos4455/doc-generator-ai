**Manual de Instalação de Atualizações de Segurança no Linux com Yum**

**Seção 3: Instalar Atualizações**

### 3.1 Instalar Atualizações de Segurança com `yum localinstall --security`

**Objetivo:** Instalar exclusivamente atualizações de segurança baixadas anteriormente usando o comando `yum`.

**Pré-requisitos:**

- Atualizações de segurança baixadas com `yum downloadonly --security`

**Passos:**

1. Abra um terminal como usuário root ou com privilégios sudo.
   - 🤖 Terminal: 💻
2. Execute o seguinte comando para instalar as atualizações de segurança baixadas:

   ```
   yum localinstall --security
   ```

   - 📥 Atualizações: 🛡️
   - 📦 Gerenciador de Pacotes: 📦

3. Pressione Enter e insira a senha root ou sudo quando solicitado.
4. Aguarde a conclusão da instalação, que pode levar vários minutos.
5. Verifique se as atualizações foram instaladas com sucesso executando o seguinte comando:
   - 🔍 Verificação: ✅

   ```
   yum updateinfo list security
   ```

**Exemplo:**

```
$ sudo yum localinstall --security
[sudo] Senha para fulano:
Baixando pacotes:
total 2,4 kB/s | 1,2 kB 00:00
Instalando:
Instalando: bind-utils.x86_64 1:9.13.6-6.el8                  
Transações concluídas
```

### 3.2 Gerenciar Atualizações de Segurança

Além da instalação, o Yum oferece vários comandos para gerenciar atualizações de segurança:

- **listar atualizações de segurança:**
   - 📃 Lista: 📋

   ```
   yum updateinfo list security
   ```

- **exibir informações sobre uma atualização de segurança específica:**
   - 🔎 Detalhes: ℹ️

   ```
   yum updateinfo info <nome_do_pacote>
   ```

- **excluir uma atualização de segurança específica:**
   - 🗑️ Excluir: ❌

   ```
   yum updateinfo remove <nome_do_pacote>
   ```

- **definir a política de atualização de segurança:**
   - ⚙️ Configuração: 🔧

   ```
   yum updateinfo set-security-policy <política>
   ```

   Onde `<política>` pode ser:

   - **moderate:** Instalar atualizações de segurança apenas quando disponíveis
   - **low:** Instalar atualizações de segurança apenas quando elas corrigirem vulnerabilidades críticas

**Conclusão:**

Seguindo as etapas descritas acima, você pode instalar e gerenciar atualizações de segurança no Linux de forma eficiente e segura usando o Yum. Lembre-se de verificar regularmente se há novas atualizações de segurança e aplicá-las prontamente para manter seu sistema atualizado e protegido.