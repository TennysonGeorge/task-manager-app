from flask import Flask
from api.routes import api
from api.models import db
import os

app = Flask(__name__)

# Configure SQLite database using environment variable or default path
database_path = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///tasks.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Register the blueprint with a URL prefix
app.register_blueprint(api, url_prefix='')  # Empty prefix to serve from root

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Use environment variable for host to allow connections from outside the container
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5001))
    debug = True  # Set debug to True for development
    
    app.run(host=host, port=port, debug=debug)