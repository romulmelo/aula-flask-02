from flask import Flask, request, make_response, redirect, abort;
app = Flask(__name__);

@app.route('/')
def index():
    return '<h1>Avaliação contínua: Aula 030</h1><ul><li><a href="/">Home</a></li><li><a href="/user/Romulo%20Melo/PT3020487/IFSP">Identificação</a></li><li><a href="/contextorequisicao">Contexto da requisição</a></li></ul>'

@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return f'<h1>Avaliação contínua: Aula 030</h1><h2>Aluno: {name}</h2><h2>Prontuário: {prontuario}</h2><h2>Instituição: {instituicao}</h2><p><a href="/">Voltar</a></p>'