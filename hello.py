from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

# Filters in jinja2
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags


def index():
    first_name = "Asad"
    stuff = "This is bold Text"
    favorite_pizza = ["Pop","Cheese","onion",777]
    return render_template("index.html",
                           first_name= first_name,
                           stuff = stuff,
                           favorite_pizza = favorite_pizza)


# localhost:8000/user/asad
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#Creating custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500