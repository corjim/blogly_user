from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    with app.app_context():
        db.init_app(app)



#    Model down here

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(25), nullable=True)

    last_name = db.Column(db.String(30), nullable=False, default='Demo')

    image_url = db.Column(db.String(90), nullable=False)

    def __repr__(self):
        """show info about post"""
        p = self 
        return f'<Pet id ={p.id} first name ={p.first_name} last name ={p.last_name} img ={p.image_url}'
    
    @classmethod
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"



