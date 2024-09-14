from flask import Flask, request, render_template, redirect, session

from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Blog

from sqlalchemy import text

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog_user'

app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

connect_db(app)


app.config['SECRET_KEY'] = "eh4j!j4cjfolks34jj5"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



#       ***     Uncomment to wipe table and add new default user    ***

# db.drop_all()
# db.create_all()
# Blog.query.delete()

# #  Create blogger users

# vloger = Blog(first_name='Andrew', last_name='Tate')

# vampire = Blog(first_name='Riasn', last_name='star')

# President = Blog(first_name='Barack', last_name='Gentle', image_url='https://wallpapers.com/images/hd/barack-obama-contemplative-portrait-dmlomhkitv6xbvvn-2.png')

# MrSkip = Blog(first_name='Hard', last_name='Head', image_url='https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1440,w_2560,x_0,y_0/dpr_1.5/c_limit,w_1044/fl_lossy,q_auto/v1498752576/170629-ryan-trump-tease_ndlqk2')



# db.session.add(vampire)
# db.session.add(vloger)

# db.session.commit()



@app.route('/')
def user_homepage():
    '''Homepage and redirect to user's list'''

    return redirect('/users')



@app.route('/users')
def show_user():
    '''Show users on page'''

    users = Blog.query.all()

    bloggers = Blog.query.order_by(Blog.last_name, Blog.first_name).all()

    return render_template('user.html', users=users, bloggers=bloggers)


@app.route('/add/user', methods=['GET'])
def new_user_form():
    '''Show form to add a new blog user to the list'''

    return render_template('new_user.html')


@app.route("/add/user", methods=['POST'])
def new_user():
    '''Handle form for new user submission'''

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    
    new_user = Blog(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>')
def user_detail(user_id):
    '''Show details of a user'''

    user = Blog.query.get_or_404(user_id)

    return render_template('user_detail.html', user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = Blog.query.get(user_id)
    print(user)

    return render_template('edit_user.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = Blog.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = Blog.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5510, debug=True)