"""Blogly application."""

from flask import Flask, request, redirect, render_template


from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://:5433/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "harrison"
app.config['DEBUG_TB_INTERCEPTION_REDIRECT'] = False
debug =DebugToolbarExtension(app)

connect_db(app)
# db.create_all()


@app.route('/')
def list_users():
    """shows list os users in db"""
    users = User.query.all()
    return render_template('list.html', users=users)

@app.route("/add_user")
def new_user_form():

    return render_template('new_user.html')

@app.route('/', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect(f"/{new_user.id}")

@app.route('/delete/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")

@app.route('/edit/<int:user_id>')
def edit_(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/edit/<int:user_id>/go', methods=["POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]
    db.session.add(user)
    db.session.commit()
    return redirect(f"/{user.id}")

@app.route('/<int:user_id>')
def show_user(user_id):
    """show details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)