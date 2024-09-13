from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    with app.app_context():
        db.init_app(app)

default_url = 'https://images.rawpixel.com/image_png_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTAxL3JtNjA5LXNvbGlkaWNvbi13LTAwMi1wLnBuZw.png'

#    Model down here

class Blog(db.Model):

    __tablename__ = 'bloggers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(25), nullable=False)

    last_name = db.Column(db.String(30), nullable=False)

    image_url = db.Column(db.String(300), nullable=False, default='default_url')

    def __repr__(self):
        """show info about post"""
        p = self 
        return f'<Pet id ={p.id} first name ={p.first_name} last name ={p.last_name} img ={p.image_url}'
    
    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"



