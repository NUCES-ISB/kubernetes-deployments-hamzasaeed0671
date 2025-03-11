from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database connection settings
postgres_user = os.environ.get('POSTGRES_USER', 'postgresuser')
postgres_password = os.environ.get('POSTGRES_PASSWORD', 'postgrespassword')
postgres_host = os.environ.get('POSTGRES_HOST', 'postgres')
postgres_port = os.environ.get('POSTGRES_PORT', '5432')
postgres_db = os.environ.get('POSTGRES_DB', 'flaskapp')

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to Flask Kubernetes App',
        'database_connection': 'Connected' if db_connection_status() else 'Failed'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'database': db_connection_status()
    })

def db_connection_status():
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        return True
    except Exception as e:
        print(f"Database connection error: {e}")
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
