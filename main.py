import pickle
from flask import Flask
from model import predict


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='\xe0\xcd\xac#\x06\xd9\xe4\x00\xa5\xf2\x88\xc3\xef$\xa5\x05n\x97\xd8\x1269i\xd3'
)
from flask import (
    redirect, render_template, request, session, url_for
)


with open('./static/model250k.pkl', 'rb') as input_file:
    model = pickle.load(input_file)


with open('./static/corpus250k.pkl', 'rb') as input_file:
    corpus = pickle.load(input_file)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        message = request.form['message']
        if message is not None:
            session.clear()
            session['message'] = message
            return redirect(url_for('result'))
    return render_template("base.html")


@app.route('/result', methods=('GET', 'POST'))
def result():
    message = session.get('message')
    sentiment = predict(model=model, corpus=corpus, text=message)
    if request.method == 'POST':
        message = request.form['message']
        if message is not None:
            session.clear()
            session['message'] = message
            return redirect(url_for('result'))
    return render_template("result.html", message=message, sentiment=sentiment)