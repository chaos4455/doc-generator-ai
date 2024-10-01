**Manual do Usuário para Instalação de Atualizações de Segurança Isoladas no Red Hat Enterprise Linux**

**Seção 1: Introdução**
- **Ícone de Cadeado:** O que são atualizações de segurança isoladas?
- **Ícone de Relógio:** Por que é importante instalá-las?

**Seção 2: Pré-requisitos**
- **Ícone de Terminal:** Verificando a versão do yum
- **Ícone de Chave:** Configurando repositórios de segurança

**Seção 3: Instalação de Atualizações de Segurança Isoladas**
- **Ícone de Download:** Comando `yum download-only --security`
- **Ícone de Histórico:** Opções de linha de comando adicionais
- **Ícone de Salvando:** Salvando o pacote baixado

**Seção 4: Verificação das Atualizações**
- **Ícone de Lupa:** Comando `yum list updates`
- **Ícone de Diferenças:** Diferenças entre a versão atual e a atualizada

**Seção 5: Aplicação das Atualizações**
- **Ícone de Instalador:** Comando `yum install`
- **Ícone de Confirmação:** Confirmando a instalação
- **Ícone de Reiniciar:** Reinicializando o sistema para aplicar as atualizações

**Seção 6: Exemplos**
- **Diagrama de Árvore:** Fluxo de trabalho de instalação de atualizações de segurança isoladas
- **Tabela:** Opções de linha de comando para `yum download-only --security`

**Seção 7: Troubleshooting**
- **Ícone de Erro:** Erros comuns e suas soluções
- **Ícone de Perguntas:** Recursos adicionais para suporte

**Apêndice**
- Glossário de termos
- Referências para leitura adicional

**Diagrama de Árvore: Fluxo de Trabalho de Instalação de Atualizações de Segurança Isoladas**

```
                                        Verificar versão do yum
                                                 ↓
                                      Configurar repositórios de segurança
                                                 ↓
                                     Baixar atualizações de segurança isoladas (yum download-only --security)
                                                 ↓
                                          Verificar atualizações (yum list updates)
                                                 ↓
                                            Aplicar atualizações (yum install)
                                                 ↓
                                                Reinicializar sistema
```

**Ícones e Emojis Usados**

- 🔐 Cadeado: Segurança
- 🕒 Relógio: Tempo
- 💻 Terminal: Comando
- 🔑 Chave: Configuração
- 📥 Download: Baixar
- 📜 Histórico: Opções
- 💾 Salvando: Salvar
- 👀 Lupa: Verificar
- ↔️ Diferenças: Comparar
- 🔧 Instalador: Instalar
- ✔️ Confirmação: Confirmar
- ♻️ Reiniciar: Reinicializar
- ⚠️ Erro: Problema
- ❓ Perguntas: Suporte
- 📚 Glossário: Definições
- 🔗 Referências: Leitura adicional