## 📘 Guia Prático para Gerenciamento de Métodos HTTP e Códigos de Status em Operações CRUD

### 📚 Tópicos

- Entendendo Métodos HTTP
- Dominando Códigos de Status
- Implementando Operações CRUD com Métodos HTTP e Códigos de Status

### ⚡ Métodos HTTP

| Método | Descrição |
|---|---|
| GET | Recupera dados de um recurso |
| POST | Cria um novo recurso |
| PUT | Atualiza um recurso existente |
| PATCH | Atualiza parcialmente um recurso existente |
| DELETE | Exclui um recurso |

### 🟢 Códigos de Status

| Código | Descrição |
|---|---|
| 200 | OK |
| 201 | Criado |
| 204 | Sem Conteúdo |
| 400 | Solicitação Inválida |
| 401 | Não Autorizado |
| 403 | Proibido |
| 404 | Não Encontrado |
| 500 | Erro Interno do Servidor |

### 🛠️ Operações CRUD

| Operação | Método HTTP | Código de Status |
|---|---|---|
| Criar | POST | 201 |
| Recuperar | GET | 200 |
| Atualizar | PUT | 200 |
| Atualizar Parcialmente | PATCH | 200 |
| Excluir | DELETE | 204 |

### 🔗 Diagrama de Árvore

```
                               Métodos HTTP
                                 |
                                 +-----+-----+-----+-----+-----+
                                 |  GET | POST | PUT | PATCH | DELETE |
                                 +-----+-----+-----+-----+-----+
                                       |
                                       +-----+-----+-----+-----+-----+
                                       |  200 | 201 | 204 | 400 | 500 |
                                       +-----+-----+-----+-----+-----+
                                             |
                                             +-----+
                                             | CRUD |
                                             +-----+
                                                   |
                                                   +-----+-----+-----+-----+-----+
                                                   | Criar | Recuperar | Atualizar | Atualizar | Excluir |
                                                   +-----+-----+-----+-----+-----+
```

### 📚 Exemplos

**Criar um novo usuário:**

- Método HTTP: POST
- Código de status: 201

**Recuperar todos os usuários:**

- Método HTTP: GET
- Código de status: 200

**Atualizar um usuário:**

- Método HTTP: PUT
- Código de status: 200

**Atualizar parcialmente um nome de usuário:**

- Método HTTP: PATCH
- Código de status: 200

**Excluir um usuário:**

- Método HTTP: DELETE
- Código de status: 204

### 📝 Conclusão

O gerenciamento adequado de métodos HTTP e códigos de status é essencial para APIs RESTful eficientes e eficazes. Com uma compreensão sólida desses conceitos, os desenvolvedores podem criar e consumir APIs que se comunicam de forma clara e consistente.