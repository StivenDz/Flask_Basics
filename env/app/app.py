from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__,template_folder="templates")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12594995'
app.config['MYSQL_DB'] = './db/Datos_Flask.db'

conexion = MySQL(app)

@app.route('/cursos')
def listar_cursos():
    data={}
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT Languagues ,Age,Creator, Courses, Cost FROM Programming_Languagues ORDER BY Age ASC"
        cursor.excecute(sql)
        cursos=cursor.fetchall()
        print(cursos)
        data['cursos']=cursos
        data['mensaje']='Exito'
    except Exception as ex:
        data['mensaje']='Error ...'
    return jsonify(data)

@app.before_request
def before_request():
    print('Antes de la peticion...')

@app.after_request
def bafter_request(response):
    print('Despues de la peticion...')
    return response

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

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "ok"

def pagina_no_encontrada(error):
    data={
        'titulo':'Página no Encontrada'
    }
    #return render_template('404.html',data=data),404
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=9999)