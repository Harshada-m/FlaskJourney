from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_delete = db.Column(db.Boolean, default=False, nullable=True)
    created_on = db.Column(db.String(80), nullable=True)
    updated_on = db.Column(db.String(80), nullable=True)
    def __repr__(self):
        return 'User : %r' % self.first_name

@app.route('/<first_name>/<last_name>/<email>/<password>/<created_on>/<updated_on>')
def index(first_name,last_name,email,password,created_on,updated_on):
    user = Users(first_name=first_name, last_name=last_name, email=email, password=password, created_on=created_on, updated_on=updated_on)
    db.session.add(user)
    db.session.commit()
    return '<h1>ADDED A NEW USER!</h1>'

@app.route('/<first_name>')
def get_user(first_name):
    user = Users.query.filter_by(first_name=first_name).first()

    return f'<h1>The User is having an email-id of : { user.email }</h1>'


if __name__ == "__main__":
    app.run(debug=True)
