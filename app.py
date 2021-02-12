import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/movie_index")
def movie_index():
    # Renders the review page and accesses all reviews from MongoDB
    movies = mongo.db.movies.find()
    return render_template("movies.html", movies=movies)


@app.route("/search", methods=["GET", "POST"])
def search():
    # Creates a query to look for information
    # 'movie_title' or 'director' fields in MongoDB
    query = request.form.get("query")
    movies = mongo.db.movies.find({"$text": {"$search": query}})
    return render_template("movies.html", movies=movies)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks to see if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Returns message if username is unavailable
            flash("Sorry that username already exists")
            return redirect(url_for("register"))

        register = {
            # Requests username and password
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Adds user to database
        mongo.db.users.insert_one(register)
        # Adds session cookie to user's usernam
        session["user"] = request.form["username"]
        flash("Registration successful")
        return redirect(url_for("movie_index"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks for existing username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Checks password if username is in database and
            # if both match displays flash message and creates session cookie
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hello, {} Welcome Back".format(
                        request.form.get("username")))
                return redirect(url_for("movie_index"))
            else:
                # Returns an invalid message if password is incorrect
                flash("Invalid Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Returns an invalid message if username is incorrect
            flash("Invalid Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # Removes session cookie from user
    session.clear()
    flash("You Have Successfully Logged Out")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        # Create dictionary to add fields into database
        movie = {
            "movie_title": request.form.get("movie_title"),
            "director": request.form.get("director"),
            "release_year": request.form.get("release_year"),
            "description": request.form.get("description"),
            "rating": request.form.get("rating"),
            "user_review": request.form.get("user_review"),
            "user_submitted": session["user"],
            "date_submitted": datetime.now()
        }
        # Inserts fields filled in by user into database
        mongo.db.movies.insert_one(movie)
        flash("Review Successfully Posted")
        return redirect(url_for("movie_index"))

    return render_template("add_review.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/edit_review/<movie_id>", methods=["GET", "POST"])
def edit_review(movie_id):
    if request.method == "POST":
        # Creates same dictionary as add_review
        change = {
            "movie_title": request.form.get("movie_title"),
            "director": request.form.get("director"),
            "release_year": request.form.get("release_year"),
            "description": request.form.get("description"),
            "rating": request.form.get("rating"),
            "user_review": request.form.get("user_review"),
            "user_submitted": session["user"],
            "date_submitted": datetime.now()
        }
        # Replaces existing review in database with updated one
        mongo.db.movies.update({"_id": ObjectId(movie_id)}, change)
        flash("Review Changes Saved Successfully")
        return redirect(url_for("movie_index"))

    # Finds movie and loads the appropriate review the user
    # has selected based on _id field
    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template("edit_review.html", movie=movie)


@app.route("/delete_review/<movie_id>")
def delete_review(movie_id):
    # Locates and removes review based on _id field
    mongo.db.movies.remove({"_id": ObjectId(movie_id)})
    flash("Review Removed")
    return redirect(url_for('movie_index'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
