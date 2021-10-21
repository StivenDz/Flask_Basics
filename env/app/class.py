from flask import Flask, render_template, request, url_for, redirect, jsonify, abort
from flask_mysqldb import MySQL


app = Flask(__name__,template_folder="templates")

@app.route('/')
def index():
    #return '<h1>Beinvenidos a Flask, estamos trabajando en ello</h1>'
    cursos= ['PHP' ,'Python','Java','Kotlin','Dart','JavaScript']
    numeros =[1,2,3,4,5,6]
    data={

        'titulo':'Fundamentos Flask',
        'Bienvenida':'¡Saludos!',
        'cursos':cursos,
        'numeros':numeros,
        'numero_cursos':len(cursos),
        'git config --global user.name':'StivenDz',
        'git config --global user.email':'stivendiazh@gmail.com'
    }
    return render_template('index.html',data=data)

# url personalizada, especialmente para usuarios, entre otras cosas, url dinamica
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre,edad):
    data={
        'titulo': 'contacto',
        'nombre':nombre,
        'edad':edad
    }
    return render_template('contacto.html',data=data)

@app.route("/params1/")
@app.route("/params1/<nombre_>")
@app.route("/params1/<nombre_>/<apellido_>")
def parametros(nombre_="no tiene nombre", apellido_="no tiene apellido"):
    return 'su nombre es: {} {}'.format(nombre_,apellido_)


@app.route("/params/<string:nombre_>/<int:edad>")
def parametros2(nombre_="no tiene nombre", edad="no tiene apellido"):
    return 'su nombre es: {} y tienes {}'.format(nombre_,edad)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "ok"


#def pagina_no_encontrada(error):
#    data={
#        'titulo':'Página no Encontrada'
#    }
    #return render_template('404.html',data=data),404
#    return redirect(url_for('index'))

@app.route("/suma/<n1>/<n2>")
def smar(n1,n2):
    
    try:
        result=int(n1) + int(n2)
        
    except:
        abort(404)

    data={
        "titulo":"Suma",
        "numero1":n1,
        "numero2":n2,
        "resultado":result
    }
    
    return render_template("plantilla.html",data=data)


def page_not_found(error):
    data={
        "titulo":"Página No Encontrada"
    }
    return render_template("404.html",data=data),404

if __name__ == '__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=8999)