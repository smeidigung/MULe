from flask import Flask, redirect, url_for, render_template
from flask_navigation import Navigation
import collections
try:
    from collections import abc
    collections.MutableSequence = abc.MutableSequence
except:
    pass

app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('My Account', 'my_account'),
    nav.Item('About MULe', 'about'),
    nav.Item('Contact the Team', 'contact'),
    nav.Item('My Signup', 'signup'),
    nav.Item('Practical Info', 'practical_info'),
    nav.Item('F.A.Q','FAQ'),
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/myaccount')
def account():
    return render_template('account.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/info')
def practical_info():
    return render_template('practical_info.html')

@app.route('/faq')
def FAQ():
    return render_template('FAQ.html')

@app.route('/navpage') 
def navpage(): 
    return render_template('navpage.html') 

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run

#if __name__ == "__main__":
#    app.run(host="0.0.0.0")