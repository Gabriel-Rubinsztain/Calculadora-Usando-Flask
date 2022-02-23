from ast import operator
from crypt import methods
import os
from flask import Flask, jsonify, request, render_template, abort
from math import sqrt
import Calculadora_fun as calcular

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('Calculadora.html')


@app.route('/calculadora', methods=['POST', 'GET'])
def calculadora():

    v1 = request.form['valor1']
    v2 = request.form['valor2']
    operacao = request.form['operacao']

    try:
        v1 = int(v1)
    except ValueError:
        abort(404)

    try:
        v2 = int(v2)
    except ValueError:
        abort(404)

    if(operacao == 'somar'):
        resultado = calcular.somar(v1, v2)
    elif(operacao == 'subtrair'):
        resultado = calcular.subtrair(v1, v2)
    elif(operacao == 'multiplicar'):
        resultado = calcular.multiplicar(v1, v2)
    elif(operacao == 'dividir'):
        if(v2 == 0):
            abort(422)
        else:
            resultado = calcular.dividir(v1, v2)
    else:
        abort(404)

    return str(resultado)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
