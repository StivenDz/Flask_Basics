from flask import Flask, render_template

app = Flask(__name__,template_folder="templates")


@app.route("/Login")
def login():
    return render_template("Login.html")



if __name__ == "__main__":
    app.run(debug=True,port=7999)

