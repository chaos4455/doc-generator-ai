**Manual de Melhores Práticas para Definir Políticas de Autorização Baseadas em Funções JWT**

<br>

## Introdução
<br>

Autorização baseada em funções (RBAC) é um mecanismo que permite atribuir um conjunto de permissões a uma função e, em seguida, vincular usuários a essas funções. Isso simplifica o gerenciamento de permissões, pois as permissões podem ser gerenciadas centralmente em funções em vez de vinculadas a cada usuário individualmente.

<br>

## Definição de Políticas de Autorização JWT
<br>

Os tokens JWT (JSON Web Token) são uma forma conveniente de implementar RBAC. Eles são compactos, fáceis de verificar e podem ser decodificados para extrair os dados de autorização.

Para definir políticas de autorização baseadas em funções usando JWTs, siga estas etapas:

<br>

**1. Identifique as Funções**
<br>

Comece identificando as diferentes funções em seu sistema e as permissões associadas a cada função.

<br>

**2. Crie uma Entidade Emissora**
<br>

Crie uma entidade emissora (EC) para emitir JWTs. A EC será responsável por assinar os JWTs e garantir sua integridade.

<br>

**3. Especifique as Reivindicações**
<br>

As reivindicações são pares nome-valor que contêm os dados de autorização. Inclua reivindicações para identificar o usuário, as funções do usuário e quaisquer permissões adicionais que possam ser necessárias.

<br>

**4. Assine os JWTs**
<br>

Assine os JWTs usando a chave privada da EC. Isso garante que os JWTs não possam ser alterados sem o conhecimento da EC.

<br>

**5. Distribua os JWTs**
<br>

Distribua os JWTs para os usuários. Isso pode ser feito por meio de cookies, cabeçalhos de solicitação ou outros mecanismos.

<br>

## Verificação de Políticas de Autorização
<br>

Para verificar as políticas de autorização, os servidores devem:

<br>

**1. Decodificar o JWT**
<br>

Use a chave pública da EC para decodificar o JWT e extrair as reivindicações.

<br>

**2. Validar o JWT**
<br>

Verifique se o JWT foi assinado pela EC e se a assinatura é válida.

<br>

**3. Autorizar o Usuário**
<br>

Compare as funções do usuário com as funções necessárias para a solicitação atual. Se o usuário tiver as funções necessárias, conceda acesso.

<br>

## Exemplos de Reivindicações de Função JWT
<br>

Aqui estão alguns exemplos de reivindicações de função JWT:

<br>

* **sub:** ID exclusivo do usuário
* **roles:** Uma lista de funções do usuário
* **permissions:** Uma lista de permissões específicas do usuário
* **exp:** Data de expiração do token

<br>

## Diagramas de Árvore
<br>

Os seguintes diagramas de árvore ilustram a hierarquia de funções e permissões:

<br>

[Diagrama de árvore de funções e permissões]

<br>

[Diagrama de árvore de verificação de autorização]

<br>

## Ícones e Emojis
<br>

🔑 **Chave:** Entidade Emissora
👤 **Usuário:** Usuário com função atribuída
📖 **JWT:** Token JWT assinado
✅ **Autorizado:** Acesso concedido
❌ **Não autorizado:** Acesso negado

<br>

## Conclusão
<br>

Definir políticas de autorização baseadas em funções usando JWTs é um processo eficiente e escalável que permite gerenciar facilmente as permissões do usuário. Ao seguir as práticas recomendadas descritas neste manual, você pode garantir que suas políticas de autorização sejam robustas e seguras.