## Manual de Referência da Arquitetura e Glossário de Termos do IP Tables

## Terminologia e Arquitetura Básicas das IP Tables

### Terminologia

- **Cadeia (chain):** Uma cadeia é uma coleção de regras de filtro que são aplicadas a um pacote.
- **Regra (rule):** Uma regra é uma instrução que especifica como um pacote deve ser tratado.
- **Tabela (table):** Uma tabela é uma coleção de cadeias.
- **Alvo (target):** Um alvo é uma ação que é realizada em um pacote que corresponde a uma regra.
- **Correspondência (match):** Uma correspondência é um critério que determina se um pacote corresponde a uma regra.
- **Módulo (module):** Um módulo é um complemento que adiciona funcionalidade às IP Tables.

### Arquitetura

As IP Tables são compostas por três componentes principais:

- **Módulo do Núcleo:** O módulo do núcleo é responsável por implementar a funcionalidade básica das IP Tables.
- **Tabela Mangle:** A tabela Mangle é usada para alterar os cabeçalhos dos pacotes.
- **Tabela Nat:** A tabela Nat é usada para traduzir endereços de rede.
- **Tabela Filter:** A tabela Filter é usada para filtrar pacotes.

## Glossário de Termos das IP Tables

| Termo | Definição |
|---|---|
| **ACCEPT:** Aceita o pacote. | 👀✅ |
| **DROP:** Ignora o pacote. | 🚫❌ |
| **REJECT:** Ignora o pacote e envia uma mensagem de erro. | 🚫❌ |
| **LOG:** Registra o pacote. | 📝📜 |
| **MASQUERADE:** Traduz o endereço IP de origem do pacote para o endereço IP da interface de saída. | 🎭↔️ |
| **REDIRECT:** Redireciona o pacote para uma porta ou endereço IP diferente. | 🔄🚀 |
| **SNAT:** Traduz o endereço IP de origem do pacote. | 🌐🌍 |
| **DNAT:** Traduz o endereço IP de destino do pacote. | 🌐🌍 |
| **tcp:** Corresponde a pacotes TCP. | 🌐 |
| **udp:** Corresponde a pacotes UDP. | 🌐 |
| **icmp:** Corresponde a pacotes ICMP. | 🌐 |
| **state:** Corresponde ao estado de uma conexão. | 💡 |
| **-A:** Adiciona uma regra à cadeia. | ➕ |
| **-D:** Exclui uma regra da cadeia. | ➖ |
| **-I:** Insere uma regra na cadeia. | 📥 |
| **-R:** Substitui uma regra na cadeia. | 🔄 |
| **-L:** Lista as regras na cadeia. | 📜 |
| **-v:** Mostra informações detalhadas sobre as regras na cadeia. | 💡 |