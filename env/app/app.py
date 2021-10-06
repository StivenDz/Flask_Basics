from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Beinvenidos a Flask, estamos trabajando en ello</h1>'
    cursos= ['PHP' ,'Python','Java','Kotlin','Dart','JavaScript']
    numeros =[1,2,3,4,5,6]
    data={
        'titulo':'Drums School',
        'Bienvenida':'¡Saludos!',
        'cursos':cursos,
        'numeros':numeros,
        'numero_cursos':len(cursos),
        'git config --global user.name':'StivenDz',
        'git config --global user.email':'stivendiazh@gmail.com'
    }
    return render_template('index.html',data=data)


@app.route('/contacto/<nombre>')
def contacto(nombre):
    data={
        'titulo': 'contacto',
        'nombre':nombre
    }
    return render_template('contacto.html',data=data)


if __name__ == '__main__':
    app.run(debug=True, port=9999)