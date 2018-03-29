from user_login import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    email = db.Column(db.String(40), unique = True)
    username = db.Column(db.String(40), unique = True)
    password = db.Column(db.String(80))


    def __init__(self, firstname, lastname, email, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password

