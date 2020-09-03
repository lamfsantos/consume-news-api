from flask import Flask, request
from flask_cors import CORS
from app.index_route import index_blueprint

app = Flask(__name__)
CORS(app)
app.register_blueprint(index_blueprint)

if __name__ == "__main__":
    app.run()
