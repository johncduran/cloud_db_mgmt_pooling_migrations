from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy for Azure MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://john:migrationsWolf897@migrationstest.mysql.database.azure.com/john'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create SQLAlchemy instance
db = SQLAlchemy(app)

# Define a model (replace with your actual model)
class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def index():
    return render_template('base.html')

# Routes to retrieve and display data from both databases
@app.route('/azure_data')
def get_azure_data():
    azure_data = Patient.query.filter_by().all()
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
