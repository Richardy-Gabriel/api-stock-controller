# API Rest with Python and Django Rest Framework

API Rest desenvolvida utilizando a linguagem de programação Python junto com o Django Rest Framework.

## Documentação da API

#### Retorna todos os produtos

```http
  GET /api/products
```

| Parâmetro        | Tipo     | Descrição                                           |
| :--------------- | :------- | :-------------------------------------------------- |
| `api_auth_basic` | `string` | **Obrigatório**. Usuário e senha para realizar POST |

#### Retorna um produto

```http
  GET /api/products/${id}
```

| Parâmetro | Tipo  | Descrição                                      |
| :-------- | :---- | :--------------------------------------------- |
| `id`      | `int` | **Obrigatório**. O ID do produto que você quer |

#### Baixa no estoque do produto

```http
  GET /api/products/${id}/reduce-stock/
```

| Parâmetro | Tipo  | Descrição                                                           |
| :-------- | :---- | :------------------------------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do produto que você quer dar baixa no estoque |

#### Incluir estoque do produto

```http
  GET /api/products/${id}/increase-stock/
```

| Parâmetro | Tipo  | Descrição                                              |
| :-------- | :---- | :----------------------------------------------------- |
| `id`      | `int` | **Obrigatório**. O ID do produto que você quer incluir |
