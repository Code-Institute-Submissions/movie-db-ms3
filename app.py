import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
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
    movies = mongo.db.movies.find()
    return render_template("movies.html", movies=movies)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry that username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form["username"]
        flash("Registration successful")
        return redirect(url_for("movie_index"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hello, {} welcome back".format(
                        request.form.get("username")))
                return redirect(url_for("movie_index"))
            else:
                flash("Invalid Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Invalid Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have successfully logged out")
    return redirect(url_for("login"))


@app.route("/add_review")
def add_review():
    if request.method == "POST":
        movie = {
            "movie_title": request.form.get("movie_title"),
            "director": request.form.get("director"),
            "description": request.form.get("description"),
            "rating": request.form.get("rating"),
            "release_year": request.form.get("release_year"),
            "user_submitted": session["user"],
        }
        mongo.db.movies.insert_one(movie)
        flash("Review Successfully Posted")
        return redirect(url_for("movie_index"))

    return render_template("add_review.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
