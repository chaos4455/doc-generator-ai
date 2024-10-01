**Guia Passo a Passo para Baixar Atualizações com Segurança no Yum**

**Introdução 🔗**

O Yum (Yellowdog Updater, Modified) é um gerenciador de pacotes usado em distribuições Linux baseadas em Red Hat, como Red Hat Enterprise Linux (RHEL), CentOS e Fedora. O Yum permite que os usuários instalem, atualizem e removam pacotes de software com segurança e eficiência.

**Tópicos**

- [Baixar Atualizações](#baixar-atualizações)
- [Executar Atualizações de Segurança](#executar-atualizações-de-segurança)
- [Verificar Pacotes Instalados](#verificar-pacotes-instalados)
- [Dicas Adicionais para Segurança](#dicas-adicionais-para-segurança)

**Baixar Atualizações 📥**

Para baixar as atualizações de segurança mais recentes, execute o seguinte comando:

```
yum download-only --security
```

Isso baixará os pacotes de patch, mas não os instalará.

**Executar Atualizações de Segurança 🛡️**

Após baixar as atualizações, você pode instalá-las executando o seguinte comando:

```
yum update --security
```

Ele instalará os pacotes de patch baixados e aplicará as atualizações de segurança.

**Verificar Pacotes Instalados 🔎**

Para verificar os pacotes instalados no seu sistema, execute o seguinte comando:

```
yum list installed
```

Isso exibirá uma lista de todos os pacotes instalados, incluindo os pacotes de segurança.

**Dicas Adicionais para Segurança 🔒**

- Configure o Yum para verificar automaticamente as atualizações de segurança usando o comando `yum-cron`.
- Assine as atualizações do repositório usando o comando `yum-security-subscription`.
- Mantenha seu sistema atualizado com as atualizações de segurança mais recentes.
- Use um firewall para proteger seu sistema de acesso não autorizado.
- Implemente medidas de segurança adicionais, como antivírus e software anti-malware.