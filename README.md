# API de Gerenciamento de Livros

Esta é uma API simples desenvolvida em Flask para gerenciar livros para doação, com uma interface web amigável.

## Estrutura do Projeto

```
.
├── app.py              # Arquivo principal da aplicação Flask
├── database.db         # Banco de dados SQLite
├── requirements.txt    # Dependências do projeto
└── templates/         # Pasta com os templates HTML
    └── index.html     # Interface web da aplicação
```

## Requisitos

- Python 
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone este repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Crie um ambiente virtual (recomendado):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a Aplicação

1. Ative o ambiente virtual (se estiver usando):
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

2. Inicie a aplicação:
```bash
python app.py
```

3. Acesse a aplicação no navegador:
```
http://localhost:5000
```

## Interface Web

A API possui uma interface web amigável que permite:

1. Cadastrar novos livros através de um formulário intuitivo
2. Visualizar todos os livros cadastrados em um layout de cards
3. Atualizar a lista de livros em tempo real

### Funcionalidades da Interface

- **Formulário de Cadastro**: Permite inserir todos os dados do livro de forma simples
- **Visualização em Cards**: Os livros são exibidos em um layout moderno com imagens
- **Atualização em Tempo Real**: A lista de livros é atualizada automaticamente após cada cadastro
- **Design Responsivo**: A interface se adapta a diferentes tamanhos de tela

## Endpoints da API

### GET /
- **Descrição**: Retorna a interface web da aplicação
- **URL**: `http://localhost:5000/`
- **Método**: GET

### POST /doar
- **Descrição**: Cadastra um novo livro no banco de dados
- **URL**: `http://localhost:5000/doar`
- **Método**: POST
- **Corpo da Requisição**:
```json
{
    "titulo": "O Senhor dos Anéis",
    "categoria": "Fantasia",
    "autor": "J.R.R. Tolkien",
    "imagem_url": "https://exemplo.com/imagem.jpg"
}
```
- **Resposta de Sucesso**: Status 201
- **Resposta de Erro**: Status 400 ou 500

### GET /livros
- **Descrição**: Retorna a lista de todos os livros cadastrados
- **URL**: `http://localhost:5000/livros`
- **Método**: GET
- **Resposta**: Lista de livros em formato JSON

## Estrutura do Banco de Dados

A tabela `LIVROS` possui os seguintes campos:
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT): Identificador único do livro
- `titulo` (TEXT NOT NULL): Título do livro
- `categoria` (TEXT NOT NULL): Categoria do livro
- `autor` (TEXT NOT NULL): Nome do autor
- `imagem_url` (TEXT NOT NULL): URL da imagem de capa do livro

## Exemplos de Uso

### Usando a Interface Web

1. Acesse `http://localhost:5000` no navegador
2. Use o formulário à esquerda para cadastrar um novo livro
3. A lista de livros será atualizada automaticamente
4. Use o botão "Atualizar Lista" para recarregar os livros manualmente

### Usando a API via curl

1. Cadastrar um livro:
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

2. Listar todos os livros:
```bash
curl http://localhost:5000/livros
```

### Usando a API via Postman

1. **Configurando o Postman**:
   - Baixe e instale o [Postman](https://www.postman.com/downloads/)
   - Crie uma nova coleção para a API de Livros

2. **Cadastrando um Livro**:
   - Crie uma nova requisição
   - Selecione o método `POST`
   - Digite a URL: `http://localhost:5000/doar`
   - Selecione a aba "Body"
   - Selecione "raw" e escolha "JSON"
   - Cole o seguinte JSON:
   ```json
   {
       "titulo": "O Senhor dos Anéis",
       "categoria": "Fantasia",
       "autor": "J.R.R. Tolkien",
       "imagem_url": "https://exemplo.com/imagem.jpg"
   }
   ```
   - Clique em "Send"
   - Você receberá uma resposta com status 201 se o cadastro for bem-sucedido

3. **Listando Livros**:
   - Crie uma nova requisição
   - Selecione o método `GET`
   - Digite a URL: `http://localhost:5000/livros`
   - Clique em "Send"
   - A resposta será uma lista JSON com todos os livros cadastrados

4. **Acessando a Interface Web**:
   - Crie uma nova requisição
   - Selecione o método `GET`
   - Digite a URL: `http://localhost:5000`
   - Clique em "Send"

## Dependências

O projeto utiliza as seguintes bibliotecas principais:
- Flask==3.0.2: Framework web
- Flask-CORS==4.0.0: Suporte a CORS
- Werkzeug==3.0.1: Utilitários WSGI
- Jinja2==3.1.3: Motor de templates

Para ver todas as dependências, consulte o arquivo `requirements.txt`.

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. 
