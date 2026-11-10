from flask import Flask, jsonify, request
from datetime import date

app = Flask(__name__)

tarefas = [
    {
        'prioridade': 1,
        'to-do': 'Relatório SQL',
        'data': date(2026, 11, 15)
    },
    {
        'prioridade': 2,
        'to-do': 'Entrega protótipo interface',
        'data': date(2026, 11, 18)
    },
    {
        'prioridade': 3,
        'to-do': 'Prova álgebra linear',
        'data': date(2026, 11, 20)
    },
]

@app.route('/tarefas/<int:id>', methods=['GET'])
def visualizar_tarefa_por_prioridade(id):
    for tarefa in tarefas:
        if tarefa.get('id') == id:
            return jsonify(tarefa)

@app.route('/tarefas', methods=['GET'])
def visualizar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas/<int:id>', methods=['PUT'])
def editar_tarefa_por_id(id):
    tarefa_alterada = request.get_json()
    for indice, tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            tarefas[indice].update(tarefa_alterada)
            return jsonify(tarefas[indice])

@app.route('/tarefas', methods=['POST'])
def adicionar_tareda():
    nova_tarefa = request.get_json()
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa)

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def concluir_tarefa(id):
    for indice, tarefa in enumerate (tarefas):
        if tarefa.get('id') == id:
            del tarefas[indice]
    return jsonify(tarefas)

app.run(port=5001, host='localhost', debug=True)