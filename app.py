from flask import Flask
from models import db, User, Follow, FollowerCount
from routes import api_bp
from flask_swagger_ui import get_swaggerui_blueprint
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()

SWAGGER_URL = config.SWAGGER_URL
API_URL = config.API_URL

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Following System API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Following System API! Go to /swagger for the API documentation."

if __name__ == "__main__":
    app.run(debug=True)
