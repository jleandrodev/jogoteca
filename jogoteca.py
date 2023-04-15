from flask import Flask

app = Flask(__name__)


@app.route('/inicio')
def ola():
    return '<h1>Hello</h1>'

app.run()