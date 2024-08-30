**Subtema 2: Proteção de APIs com JWT**

**Introdução**

Os Tokens Web JSON (JWTs) são um mecanismo padrão para proteger APIs transmitindo informações seguras entre partes confiáveis. Eles fornecem um método seguro e eficiente para autenticar e autorizar usuários, permitindo acesso controlado aos recursos da API.

**Como funcionam os JWTs**

Os JWTs são cadeias compactas assinadas que contêm três partes:

* **Cabeçalho:** Contém informações sobre o tipo e algoritmo de assinatura do JWT.
* **Carga útil:** Contém as informações de identidade do usuário, como ID de usuário, função e outros atributos.
* **Assinatura:** Verifica a integridade e autenticidade do JWT usando uma chave secreta.

**Etapas para proteger APIs com JWT**

**1. Crie uma chave secreta**

Gere uma chave secreta segura que será usada para assinar os JWTs. Esta chave deve ser mantida em segredo e armazenada com segurança.

**2. Configure o servidor de autorização**

Configure um servidor de autorização que emitirá JWTs quando os usuários forem autenticados. Este servidor deve verificar as credenciais do usuário e retornar um JWT se a autenticação for bem-sucedida.

**3. Integre JWTs no aplicativo cliente**

O aplicativo cliente deve enviar o JWT recebido do servidor de autorização como cabeçalho de autorização em cada solicitação de API.

**4. Verifique JWTs nas APIs**

As APIs devem verificar o JWT enviado no cabeçalho de autorização para garantir que ele seja válido e não tenha sido adulterado. Se o JWT for válido, o acesso ao recurso da API será concedido.

**Exemplo**

Considere o seguinte JWT:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

* **Cabeçalho:**
    * ```{"alg":"HS256","typ":"JWT"}```
* **Carga útil:**
    * ```{"sub":"1234567890","name":"John Doe","iat":1516239022}```
* **Assinatura:**
    * ```SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c```

**Diagrama de árvore**

![Diagrama de árvore JWT](https://cdn.diagrams.net/diagrams/6c8a2887-1f95-4bc5-87a8-6950b21d7a1c)

**Ícones e emojis**

* 🔒 JWT: Token Web JSON
* 🔑 Chave secreta
* ✅ Autenticado
* ❌ Não autenticado
* 🛡️ Protegido