## 📚 Guia Prático para Integrar Bibliotecas JWT em APIs .NET Core

### 🗝️ Visão Geral

JSON Web Tokens (JWTs) são um padrão amplamente utilizado para autenticar e autorizar usuários em aplicativos web. Ao integrar bibliotecas JWT em APIs .NET Core, você pode proteger eficazmente seus endpoints e gerenciar o acesso do usuário.

### 🔦 Bibliotecas Recomendadas

Existem várias bibliotecas JWT disponíveis para .NET Core, incluindo:

- 🔮 [Microsoft.IdentityModel.Tokens](https://www.nuget.org/packages/Microsoft.IdentityModel.Tokens)
- 🔑 [Jwt.Net](https://www.nuget.org/packages/Jwt.Net)
- 🕶️ [JsonWebToken](https://www.nuget.org/packages/JsonWebToken)

### 🛠️ Integração Passo a Passo

**1. Instalação da Biblioteca**

```
PM> Install-Package Microsoft.IdentityModel.Tokens
```

**2. Geração de Chaves**

Crie um par de chaves RSA para assinar e verificar JWTs.

```csharp
RSACryptoServiceProvider rsa = new RSACryptoServiceProvider(2048);
```

**3. Criação de um Token**

Use a chave privada para assinar um novo JWT.

```csharp
JwtSecurityTokenHandler handler = new JwtSecurityTokenHandler();
SecurityTokenDescriptor descriptor = new SecurityTokenDescriptor
{
    Issuer = "MeuAplicativo",
    Audience = "MinhaAplicacao",
    Subject = new ClaimsIdentity(new List<Claim> { new Claim("usuario", "fulano") }),
    SigningCredentials = new SigningCredentials(new RsaSecurityKey(rsa.ExportParameters(true)), SecurityAlgorithms.RsaSha256)
};

JwtSecurityToken token = handler.CreateToken(descriptor);

var tokenString = handler.WriteToken(token);
```

**4. Validação de um Token**

Use a chave pública para validar um JWT recebido.

```csharp
JwtSecurityTokenHandler handler = new JwtSecurityTokenHandler();
TokenValidationParameters validationParameters = new TokenValidationParameters
{
    IssuerSigningKey = new RsaSecurityKey(rsa.ExportParameters(false)),
    ValidIssuer = "MeuAplicativo",
    ValidAudience = "MinhaAplicacao"
};

SecurityToken validatedToken;
handler.ValidateToken(tokenString, validationParameters, out validatedToken);
```

**5. Proteção de Endpoints**

Use o atributo `[Authorize]` para proteger endpoints específicos.

```csharp
[Authorize]
public IActionResult GetProtegido() { ... }
```

### 🏆 Exemplos

1. **Gerando um token JWT com expiração:**
```csharp
descriptor.Expires = DateTime.UtcNow.AddMinutes(30);
```

2. **Adicionando reivindicações personalizadas:**
```csharp
descriptor.Subject.AddClaim(new Claim("role", "admin"));
```

3. **Usando um algoritmo diferente de assinatura:**
```csharp
SigningCredentials = new SigningCredentials(new RsaSecurityKey(rsa.ExportParameters(true)), SecurityAlgorithms.RsaSha384)
```

4. **Validando um token com um emissor diferente:**
```csharp
validationParameters.ValidIssuer = "OutroAplicativo";
```

5. **Usando um provedor de autorização personalizado:**
```csharp
public class MeuAuthorizeAttribute : AuthorizeAttribute
{
    protected override bool AuthorizeCore(HttpContext context) { ... }
}
```

6. **Configurando tamanhos de chave RSA estendidos:**
```csharp
rsa = new RSACryptoServiceProvider(2048, new CspParameters { KeySizeInBits = 4096 });
```

7. **Usando um token de atualização:**
```csharp
public TokenModel RefreshToken(string refreshToken) { ... }
```

8. **Lidando com tokens expirados:**
```csharp
public IActionResult OnTokenExpired() { ... }
```

9. **Armazenando tokens JWT em cookies:**
```csharp
Response.Cookies.Append("access_token", tokenString);
```

10. **Usando injeção de dependência para JWT:**
```csharp
public class MeuControlador
{
    private IJwtService jwtService;

    public MeuControlador(IJwtService jwtService) { ... }
}
```

### 📚 Recursos Adicionais

- [Documentação do Microsoft.IdentityModel.Tokens](https://docs.microsoft.com/pt-br/dotnet/api/microsoft.identitymodel.tokens?view=netcore-3.1)
- [Documentação do JWT.Net](https://jwt.io/)
- [Documentação do JsonWebToken](https://github.com/auth0/jwt)