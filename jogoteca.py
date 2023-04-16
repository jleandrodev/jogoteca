from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        pass

app = Flask(__name__)


@app.route('/inicio')
def ola():
    lista = ['Tetris', 'Skyrim', 'God of War']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()