from flask import Flask
from database import db
from routes import register_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

register_routes(app)

@app.route('/')
def home():
    return "Welcome to Flask Backend Project"

if __name__ == '__main__':
    app.run(debug=True)

