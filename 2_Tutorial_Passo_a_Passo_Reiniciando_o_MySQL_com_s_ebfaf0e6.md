**Tutorial Passo a Passo: Reiniciando o MySQL com systemctl**

**Introdução**

Reiniciar o MySQL pode ser necessário para aplicar alterações de configuração ou resolver problemas. Este tutorial mostrará como reiniciar o MySQL usando o comando systemctl.

**Pré-requisitos**

* Servidor Linux com MySQL instalado
* Acesso de usuário root ou sudo

**Passos**

1. **Abra um terminal**

   Abra um terminal com privilégios de root ou sudo.

2. **Determine o nome do serviço MySQL**

   Execute o seguinte comando para determinar o nome do serviço MySQL:

   ```bash
   systemctl list-unit-files | grep mysql
   ```

   A saída retornará o nome do serviço MySQL, que normalmente é **mysql.service**.

3. **Reinicie o serviço MySQL**

   Para reiniciar o serviço MySQL, use o comando systemctl:

   ```bash
   systemctl restart <nome-do-servico>
   ```

   Substitua `<nome-do-servico>` pelo nome do serviço MySQL que você determinou na etapa anterior.

   Por exemplo, para reiniciar o serviço `mysql.service`:

   ```bash
   systemctl restart mysql.service
   ```

4. **Verifique o status do MySQL**

   Após reiniciar o MySQL, verifique seu status com o comando systemctl:

   ```bash
   systemctl status <nome-do-servico>
   ```

   A saída retornará o status atual do MySQL.

**Exemplo**

Veja um exemplo completo de como reiniciar o MySQL com systemctl:

1. Determine o nome do serviço MySQL:

   ```bash
   systemctl list-unit-files | grep mysql
   ```

   Saída:

   ```
   mysql.service loaded active running MySQL Community Server
   ```

2. Reinicie o serviço MySQL:

   ```bash
   systemctl restart mysql.service
   ```

3. Verifique o status do MySQL:

   ```bash
   systemctl status mysql.service
   ```

   Saída:

   ```
   ● mysql.service - MySQL Community Server
    Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
    Active: active (running) since Sat 2023-08-19 15:00:08 UTC; 1min 41s ago
    ...
   ```

**Diagrama de Árvore**

```
                                                                      +-----------------+
                                                                      | Reiniciando o     |
                                                                      | MySQL com        |
                                                                      +-----------------+
                                                                              |
                                                                              v
                                                                   +-----------------------------+
                                                                   | 1. Abra um terminal        |
                                                                   +-----------------------------+
                                                                              |
                                                                            +--+
                                                                            |  |
                                                                            v  v
                                                               +-----------------------------+  +-------------------------+
                                                               | 2. Determine o nome do    |  | 3. Reinicie o serviço  |
                                                               | serviço MySQL            |  | MySQL                 |
                                                               +-----------------------------+  +-------------------------+
                                                                              |
                                                                            +--+
                                                                            |  |
                                                                            v  v
                                    +-----------------------------+  +-----------------------------+
                                    | 4. Verifique o status do   |  | Exemplo                   |
                                    | MySQL                        |  |                             |
                                    +-----------------------------+  +-----------------------------+
```

**Conclusão**

Reiniciar o MySQL usando systemctl é uma tarefa simples que pode ser realizada em apenas alguns passos. Ao seguir as etapas descritas neste tutorial, você pode reiniciar o MySQL com sucesso e aplicar alterações ou resolver problemas.

**Ícones e Emojis**

* 💻 Terminal
* ⚙️ systemctl
* 🔄 Reiniciar
* ✅ Verificado