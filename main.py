import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Колонизация')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def professions(list):
    with open("professions.json", "rt", encoding="utf8") as f:
        professions_list = json.loads(f.read())
    return render_template('professions.html', list=list, professions=professions_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')