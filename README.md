# API de Gerenciamento de Livros

Esta é uma API simples desenvolvida em Flask para gerenciar livros para doação.

## Requisitos

- Python 
- Flask
- Flask-CORS

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a API

Para iniciar a API, execute:
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## Interface Web

A API possui uma interface web amigável que permite:

1. Cadastrar novos livros através de um formulário intuitivo
2. Visualizar todos os livros cadastrados em um layout de cards
3. Atualizar a lista de livros em tempo real

Para acessar a interface web, basta abrir seu navegador e acessar:
```
http://localhost:5000
```

### Funcionalidades da Interface

- **Formulário de Cadastro**: Permite inserir todos os dados do livro de forma simples
- **Visualização em Cards**: Os livros são exibidos em um layout moderno com imagens
- **Atualização em Tempo Real**: A lista de livros é atualizada automaticamente após cada cadastro
- **Design Responsivo**: A interface se adapta a diferentes tamanhos de tela

## Exemplos Rápidos de Uso

### Cadastrar um Livro:
Faça uma requisição POST para `/doar` com o seguinte JSON:
```json
{
    "titulo": "Dom Quixote",
    "categoria": "Literatura Clássica",
    "autor": "Miguel de Cervantes",
    "imagem_url": "https://exemplo.com/imagem.jpg"
}
```

### Listar Livros:
Faça uma requisição GET para `/livros` para ver todos os livros cadastrados.

### Rota Inicial:
Acesse a rota `/` para ver a mensagem de boas-vindas e as instruções.

## Como Usar a API

### 1. Acessando a Página Inicial (GET /)

Para ver a mensagem de boas-vindas, você pode:

**Usando o navegador:**
- Abra seu navegador e acesse: `http://localhost:5000`

**Usando o curl:**
```bash
curl http://localhost:5000
```

**Usando o Postman:**
1. Crie uma nova requisição
2. Selecione o método GET
3. Digite a URL: `http://localhost:5000`
4. Clique em "Send"

### 2. Cadastrando um Novo Livro (POST /doar)

**Usando o curl:**
```bash
curl -X POST http://localhost:5000/doar \
-H "Content-Type: application/json" \
-d '{
    "titulo": "O Senhor dos Anéis",
    "categoria": "Fantasia",
    "autor": "J.R.R. Tolkien",
    "imagem_url": "https://exemplo.com/imagem.jpg"
}'
```

**Usando o Postman:**
1. Crie uma nova requisição
2. Selecione o método POST
3. Digite a URL: `http://localhost:5000/doar`
4. Selecione a aba "Body"
5. Selecione "raw" e "JSON"
6. Cole o seguinte JSON:
```json
{
    "titulo": "O Senhor dos Anéis",
    "categoria": "Fantasia",
    "autor": "J.R.R. Tolkien",
    "imagem_url": "https://exemplo.com/imagem.jpg"
}
```
7. Clique em "Send"

### 3. Listando Todos os Livros (GET /livros)

**Usando o navegador:**
- Acesse: `http://localhost:5000/livros`

**Usando o curl:**
```bash
curl http://localhost:5000/livros
```

**Usando o Postman:**
1. Crie uma nova requisição
2. Selecione o método GET
3. Digite a URL: `http://localhost:5000/livros`
4. Clique em "Send"

## Endpoints

### GET /
Retorna uma mensagem de boas-vindas

### POST /doar
Cadastra um novo livro no banco de dados.

Exemplo de requisição:
```json
{
    "titulo": "O Senhor dos Anéis",
    "categoria": "Fantasia",
    "autor": "J.R.R. Tolkien",
    "imagem_url": "https://exemplo.com/imagem.jpg"
}
```

### GET /livros
Retorna a lista de todos os livros cadastrados.

## Estrutura do Banco de Dados

A tabela `LIVROS` possui os seguintes campos:
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- titulo (TEXT NOT NULL)
- categoria (TEXT NOT NULL)
- autor (TEXT NOT NULL)
- imagem_url (TEXT NOT NULL) 