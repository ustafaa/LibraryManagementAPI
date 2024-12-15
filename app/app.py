from flask import Flask, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from .routes import api
import os 

app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Library Management API"}
)
@app.route('/')
def index():
    return redirect('/api-docs')

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
