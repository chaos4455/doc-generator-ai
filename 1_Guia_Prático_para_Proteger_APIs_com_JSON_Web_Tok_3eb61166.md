## 📚 Guia Prático para Proteger APIs com JSON Web Tokens (JWT)

### 🔒 Subtema 2: Proteção de APIs com JWT

**Introdução 🌍**

Os JSON Web Tokens (JWT) são um mecanismo poderoso para proteger APIs, fornecendo autenticação e autorização sem estado. Neste subtema, exploraremos como proteger APIs com JWT, do início ao fim.

**🔗 Diagrama de Proteção de API com JWT 🔗**

```
                              JWT
                               ↓
                ╭──────────────╮
                │ Autenticação │
                ╰──────────────╯
                               ↓
                ╭──────────────╮
                │ Autorização │
                ╰──────────────╯
                               ↓
                               API
```

**Passos para Proteger uma API com JWT**

**1. Gere o Segredo JWT**

 gere um segredo JWT exclusivo e seguro. Este segredo será usado para assinar e verificar os tokens JWT.

**2. Crie o Endpoint de Token**

Crie um endpoint de API que gerará e retornará tokens JWT para clientes autenticados. Este endpoint deve ser protegido com um mecanismo de autenticação, como Autenticação Básica ou OAuth2.

**3. Autentique os Usuários**

No endpoint de token, autentique os usuários comparando suas credenciais (por exemplo, nome de usuário e senha) com os dados do usuário armazenados.

**4. Gere o Token JWT**

Após a autenticação bem-sucedida, gere um token JWT que contenha claims como o ID do usuário e o horário de expiração. O token deve ser assinado com o segredo JWT.

**5. Proteja os Endpoints de API**

Proteja os endpoints da API adicionando um middleware de autenticação que verifique se as solicitações recebidas contêm um token JWT válido.

**6. Verifique o Token JWT**

O middleware de autenticação deve verificar a assinatura do token JWT, garantir que ele não tenha expirado e que seja emitido por uma fonte confiável.

**7. Extraia as Claims**

Se o token JWT for válido, extraia as claims do token, como o ID do usuário e as permissões.

**8. Autorize o Acesso**

Use as claims extraídas para autorizar o acesso ao endpoint da API. Os usuários só têm permissão para acessar recursos para os quais têm permissão.

**🎨 Exemplos Práticos 🎨**

* Criação de um token JWT em Node.js:
```
const jwt = require("jsonwebtoken");

const token = jwt.sign({ userId: "user1" }, "my-secret-key");
```

* Validação de um token JWT em Python:
```
import jwt

def validate_token(token):
    return jwt.decode(token, "my-secret-key", "HS256")
```

* Protegendo uma rota da API com JWT em Java:
```java
@RequestMapping(method = RequestMethod.GET, value = "/api/users")
public List<User> getUsers(@RequestHeader("Authorization") String token) {
    // Valida o token JWT
    Jwts.parser().setSigningKey("my-secret-key").parseClaimsJws(token);

    // Recupera os usuários do banco de dados
    return userService.findAll();
}
```

**Conclusão 🏁**

Usar JWT para proteger APIs é uma prática essencial para manter a segurança dos dados e a privacidade do usuário. Seguindo as etapas descritas neste subtema, você pode implementar efetivamente a proteção por JWT em suas APIs e garantir a integridade e a confidencialidade dos seus dados.