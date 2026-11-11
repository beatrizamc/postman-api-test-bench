from flask import Flask, jsonify, request
from datetime import date 

app = Flask(__name__)

contas = [
    {
        'id': 1234,
        'agência': 1,
        'titular': 'Maria',
        'saldo': 1500.00
    },
    {
        'id': 5678,
        'agência': 2,
        'titular': 'João',
        'saldo': 1000.00
    },
    {
        'id': 8910,
        'agência': 3,
        'titular': 'Ana',
        'saldo': 2100.00
    },
]

transacoes = [
    {
        'id': 1,
        'valor': 100,
        'data': date(2026, 11, 11)
    },
    {
        'id': 2,
        'valor': 200,
        'data': date(2026, 11, 10)
    },
    {
        'id': 3,
        'valor': 300,
        'data': date(2026, 11, 12)
    },
]

@app.route('/contas/<id>/depositar', methods=['POST'])
def realizar_deposito(id):
   novo_deposito = request.get_json()
   valor_deposito = novo_deposito.get('valor')
   if not valor_deposito or valor_deposito <= 0:
      return jsonify({'Erro! Valor para depósito inválido.'}), 400
   
   conta = next((c for c in contas if c['id'] == id), None)
   if not conta:
      return jsonify({'Erro! Conta não encontrada.'}), 404
   if valor_deposito > conta['saldo']:
      return jsonify({
         'erro': f'O valor do depósito (R$ {valor_deposito:.2f}) não pode ser maior que o saldo atual (R${conta["saldo"]: .2f})'
      }), 400
   
   conta['saldo'] += valor_deposito
   return jsonify({
      'mensagem': 'Depósito realizado com sucesso!',
      'titular': conta['titular'],
      'novo_saldo': conta['saldo']
   }), 200
      
    

app.run(port=5000, host='localhost', debug=True)
