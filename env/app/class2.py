from flask import Flask, render_template,request

app = Flask(__name__,template_folder="templates")


@app.route("/")
def main():
    return render_template("Login.html")

@app.route("/Formulario")
def form():
    return render_template("cp.html")

@app.route("/Login/get", methods=["GET" , "POST"])
def login():
    if request.method=="GET":
        user1 = request.args.get("user") #name=user   no es el id
        pass1 = request.args.get("pass")

        if user1 == "Stiven" and pass1 == "12594995":
            return(form())
        else:
            return("No has Iniciado Sesión")

@app.route("/Login/post", methods=["GET" , "POST"])
def login_post():
    if request.method=="POST":
        user1=request.form["user"] #name=user  no es el id
        pass1=request.form["pass"]

        if user1 == "Stiven" and pass1 == "12594995":
            return(form())
        else:
            return("No has Iniciado Sesión")
    
    return render_template("Login-post.html")

if __name__ == "__main__":
    app.run(debug=True,port=7999)

