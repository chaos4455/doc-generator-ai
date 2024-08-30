**Guia Prático para Implementação de CORS: Dominando o Compartilhamento de Recursos de Origem Cruzada**

**Introdução**

CORS (Compartilhamento de Recursos de Origem Cruzada) permite que recursos de uma origem (por exemplo, um site) sejam solicitados por uma origem diferente. Isso é crucial para permitir interações entre sites de domínios diferentes.

**Implementação de CORS no Servidor**

**Etapa 1: Configurar Cabeçalhos de Resposta HTTP**

Os cabeçalhos de resposta HTTP devem incluir:

* `Access-Control-Allow-Origin`: Especifique as origens permitidas para acessar o recurso.
* `Access-Control-Allow-Methods`: Liste os métodos HTTP permitidos (por exemplo, `GET`, `POST`).
* `Access-Control-Allow-Headers`: Indique quais cabeçalhos de solicitação de origem cruzada são permitidos.

**Exemplo de Cabeçalhos CORS:**

```
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

**Etapa 2: Lidar com Solicitações Preflight (Pré-voo)**

Para solicitações específicas do CORS, como aquelas que usam métodos HTTP além de `GET`, as solicitações de pré-voo são enviadas primeiro. O servidor deve responder a essas solicitações com os cabeçalhos CORS apropriados.

**Etapa 3: Habilitar Credenciais (Opcional)**

Para permitir que credenciais (por exemplo, cookies, cabeçalhos de autorização) sejam enviadas com solicitações de origem cruzada, adicione o seguinte cabeçalho:

```
Access-Control-Allow-Credentials: true
```

**Implementação de CORS no Cliente**

**Etapa 1: Verificar a Presença de Cabeçalhos CORS**

Antes de fazer uma solicitação de origem cruzada, verifique se os cabeçalhos CORS apropriados estão presentes na resposta do servidor.

**Etapa 2: Configurar Opções de Solicitação**

Configure as seguintes opções de solicitação para habilitar o CORS:

* `mode`: Defina como `'cors'` para permitir solicitações de origem cruzada.
* `credentials`: Defina como `'include'` para permitir o envio de credenciais.

**Exemplo de Solicitação CORS no Cliente:**

```javascript
fetch('https://example.com/api/data', {
  mode: 'cors',
  credentials: 'include'
});
```

**Tabela de Exemplos de Implementação**

| Linguagem/Tecnologia | Exemplo |
|---|---|
| **JavaScript (Fetch API)** | `fetch('https://example.com/api/data', { mode: 'cors', credentials: 'include' });` |
| **Python (Flask)** | `@app.route('/api/data', methods=['GET', 'POST']) \n def data_api(): \n   return Response(headers={'Access-Control-Allow-Origin': '*'})` |
| **Node.js (Express.js)** | `app.use(cors({origin: 'https://example.com'}));` |
| **PHP (Slim Framework)** | `$app->options('/api/data', function ($request, $response, $args) { \n   return $response->withHeader('Access-Control-Allow-Origin', '*'); \n});` |
| **Java (Spring Boot)** | `@CrossOrigin(origins = "https://example.com") \n @GetMapping("/api/data") \n public List<Data> getData() { ... }` |
| **C# (ASP.NET Core)** | `[EnableCors(origins: "https://example.com", methods: ["GET", "POST"], headers: ["Content-Type", "Authorization"])] \n public IActionResult GetData() { ... }` |
| **Go (Gin Framework)** | `router.GET("/api/data", gin.WrapH(func(c *gin.Context) { \n   c.Writer.Header().Set("Access-Control-Allow-Origin", "*") \n   ... \n }))` |
| **Ruby (Rails)** | `class Api::V1::DataController < ApplicationController \n   skip_before_action :verify_authenticity_token \n   def index \n     @data = Data.all \n     render json: @data \n   end \n end` |

**Diagrama de Árvore da Implementação de CORS**

```
                            +----------------+
                            | Implementação de |
                            |     CORS      |
                            +----------------+
                                    |
                                    V
               +---------------------+
               | Implementação no    |
               |      Servidor      |
               +---------------------+
                                    |
                                    V
                    +--------------------------+
                    | Configurar Cabeçalhos    |
                    |       de Resposta       |
                    +--------------------------+
                                    |
                                    V
                 +-----------------------------+
                 | Lidar com Solicitações     |
                 |       Preflight (Pré-voo)   |
                 +-----------------------------+
                                    |
                                    V
              +---------------------------------+
              | Habilitar Credenciais (Opcional) |
              +---------------------------------+
                                    |
                                    V
          +---------------------------+
          | Implementação no Cliente  |
          +---------------------------+
                                    |
                                    V
  +-------------------------------+
  | Verificar Presença de       |
  |   Cabeçalhos CORS           |
  +-------------------------------+
                                    |
                                    V
     +-----------------------------------+
     | Configurar Opções de Solicitação  |
     +-----------------------------------+
```