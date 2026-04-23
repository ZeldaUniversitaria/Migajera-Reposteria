from flask import Flask, render_template
from server.db import listar_usuarios

app = Flask(__name__, template_folder='client/templates')

@app.route('/')
def home():
    usuarios = nolistar_usuarios()
    return render_template('index.html', usuarios=usuarios)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)


