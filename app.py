from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Função para criar a tabela no banco de dados


def criar_tabela():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS LIVROS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            autor TEXT NOT NULL,
            imagem_url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Criar a tabela ao iniciar a aplicação
criar_tabela()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/doar', methods=['POST'])
def cadastrar_livro():
    dados = request.get_json()

    if not dados or not all(k in dados for k in ['titulo', 'categoria', 'autor', 'imagem_url']):
        return jsonify({"erro": "Dados incompletos"}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO LIVROS (titulo, categoria, autor, imagem_url)
            VALUES (?, ?, ?, ?)
        ''', (dados['titulo'], dados['categoria'], dados['autor'], dados['imagem_url']))

        conn.commit()
        livro_id = cursor.lastrowid

        return jsonify({
            "mensagem": "Livro cadastrado com sucesso",
            "id": livro_id,
            "titulo": dados['titulo'],
            "categoria": dados['categoria'],
            "autor": dados['autor'],
            "imagem_url": dados['imagem_url']
        }), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        conn.close()


@app.route('/livros', methods=['GET'])
def listar_livros():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM LIVROS')
        livros = cursor.fetchall()

        livros_json = [{
            "id": livro[0],
            "titulo": livro[1],
            "categoria": livro[2],
            "autor": livro[3],
            "imagem_url": livro[4]
        } for livro in livros]

        return jsonify(livros_json)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
