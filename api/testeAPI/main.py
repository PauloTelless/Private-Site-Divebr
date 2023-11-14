from flask import Flask
from establishment_blueprint import establishment_blueprint
from database import Session

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(establishment_blueprint, url_prefix='/establishment')

@app.route("/")
def home():
    return "Landing Page"

if __name__ == "__main__":
    app.run(debug=True)