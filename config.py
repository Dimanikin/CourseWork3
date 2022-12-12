from api.api import api_bp
from flask import Flask
from main.main import main_bp


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(api_bp)
app.register_blueprint(main_bp)


@app.errorhandler(404)
def error_404(e):
    return "Такой страницы нет"


@app.errorhandler(500)
def error_500(e):
    return "Сервер отдыхает"


if __name__ == "__main__":
    app.run()
