from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1, 
        'título': 'Melting Point',
        'autor': 'Pibi'
    },
    {
        'id': 2,
        'título': 'Low Tide in Twilight',
        'autor': 'Euja'
    },
    {
        'id': 3,
        'título': 'Honey Trouble',
        'autor': 'Morak'
    },
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5001, host='localhost', debug=True)

