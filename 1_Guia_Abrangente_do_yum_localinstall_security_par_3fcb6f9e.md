## Guia Abrangente do `yum localinstall --security` para Gerentes de Pacotes

**Introdução**

O `yum localinstall --security` é um comando poderoso para instalar pacotes locais com segurança em sistemas baseados em RPM. Ele garante a integridade do pacote e protege contra alterações não autorizadas antes da instalação. Estabelecerá uma conexão segura, verificará as assinaturas dos pacotes e usará políticas de segurança para controlar as instalações.

**Sintaxe**

```
yum localinstall --security <opcoes> <pacote>
```

**Opções**

| Opção | Descrição |
|---|---|
| `--security` | Habilita verificações de segurança para a instalação do pacote |
| `--nogpgcheck` | Desabilita a verificação de assinaturas GPG|
| `--metadata-only` | Recupera metadados do pacote sem instalar |
| `--skippkgs` | Pula pacotes específicos da instalação |
| `--justdb` | Atualiza apenas o banco de dados de pacotes |
| `--downloadonly` | Baixa o pacote mas não instala |
| `--installroot` | Especifica o diretório raiz de instalação |
| `--releasever=<versão>` | Especifica a versão do lançamento a ser usada |

**Diagrama de Árvore**

```
                                      yum localinstall --security
                                            |
                                            |
                                            |
                                     +---------+--------------+
                                    /         /              |
                                   /         /               |
                                  +---------+                |
                           --nogpgcheck  --metadata-only --skippkgs
                           |     |     |            |        |
                           |     |     |            |        |
                         +------+-------+-----------+------------+
                        /     / |     |  |   /        / |     | /
                       /     /  |     |  |  /         /  |     | /
                      +-----+   +-----+  | +----------+   +-----+
                 --justdb   --downloadonly   --installroot   --releasever

```

**Exemplos**

**1. Instalar um pacote local com verificações de segurança:**

```
yum localinstall --security pacote-local.rpm
```

**2. Instalar um pacote local sem verificações de segurança:**

```
yum localinstall --security --nogpgcheck pacote-local.rpm
```

**3. Recuperar metadados do pacote sem instalar:**

```
yum localinstall --security --metadata-only pacote-local.rpm
```

**4. Pular um pacote específico da instalação:**

```
yum localinstall --security --skippkgs pacote-pular pacote-local.rpm
```

**5. Atualizar apenas o banco de dados de pacotes:**

```
yum localinstall --security --justdb pacote-local.rpm
```

**6. Baixar o pacote mas não instalar:**

```
yum localinstall --security --downloadonly pacote-local.rpm
```

**7. Especificar o diretório raiz de instalação:**

```
yum localinstall --security --installroot /opt/pacotes pacote-local.rpm
```

**8. Especificar a versão do lançamento a ser usada:**

```
yum localinstall --security --releasever 8 pacote-local.rpm
```

**9. Instalar vários pacotes locais de uma vez:**

```
yum localinstall --security pacote-local1.rpm pacote-local2.rpm pacote-local3.rpm
```

**10. Criar um alias para o comando:**

```
alias yumlocalinstall='yum localinstall --security'
```

**Verificação de Assinaturas**

O yum verificará as assinaturas GPG dos pacotes para garantir sua autenticidade. Se um pacote não puder ser verificado, a instalação será abortada. Para verificar as assinaturas manualmente, use o comando `rpm --checksig <pacote>.rpm`.

**Considerações de Segurança**

* Somente execute o `yum localinstall --security` em pacotes de fontes confiáveis.
* Verifique cuidadosamente as assinaturas dos pacotes antes de instalá-los.
* Use políticas de segurança para restringir as instalações de pacotes não autorizados.
* Mantenha o yum atualizado com as últimas correções de segurança.

**Conclusão**

O `yum localinstall --security` é uma ferramenta poderosa para instalar pacotes locais com segurança. Ao habilitar verificações de segurança, você pode garantir a integridade do pacote e proteger seu sistema contra alterações não autorizadas. Siga as práticas recomendadas de segurança e use o comando com cuidado para manter seu sistema seguro.