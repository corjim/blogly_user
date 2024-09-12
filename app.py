from flask import Flask, request, render_template, redirect, session

from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, User

from sqlalchemy import text

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog_user'

app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

connect_db(app)


app.config['SECRET_KEY'] = "eh4j!j4cjfolks34jj5"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False




@app.route('/')
def show_user():
    '''Show users on page'''

    # users = User.query.all()

    users = User.query.order_by(User.last_name, User.first_name).all()

    return render_template('base.html', user=users)





# db.drop_all()
# db.create_all()
# User.query.delete()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5510, debug=True)