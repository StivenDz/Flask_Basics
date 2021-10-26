import os

import yagmail as yagmail
from flask import Flask, render_template, flash, request, redirect, url_for
import utils

app = Flask(__name__,template_folder='templates')
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('cp.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')

@app.route('/Register', methods=('GET', 'POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['correo']
            error = None

            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash(error)
                return render_template('cp.html')

            if not utils.isPasswordValid(password):
                error = 'La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('cp.html')

            if not utils.isEmailValid(email):
                error = 'Correo invalido'
                flash(error)
                return render_template('cp.html')
                
            #modificar la siguiente linea con tu informacion personal
            yag = yagmail.SMTP('pruebamintic2022', 'Jmd12345678') 
            yag.send(to=email, subject='Activa tu cuenta',
                     contents='Bienvenido, usa este link para activar tu cuenta ')
            flash('Revisa tu correo para activar tu cuenta')
            return render_template('Login.html')
        
        #print("Llego al final")
        return render_template('cp.html')
    except:
        return render_template('cp.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
