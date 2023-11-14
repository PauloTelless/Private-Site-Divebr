from flask import Flask, render_template
from establishment_blueprint import establishment_blueprint

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(establishment_blueprint, url_prefix='/establishment')

@app.route("/")
def home():
    return render_template('landingPage.html')

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)