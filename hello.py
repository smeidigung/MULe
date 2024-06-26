from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.context_processor 
def inject_dict_for_all_templates():
    """ Build the navbar and pass this to Jinja for every route
    """
    # Build the Navigation Bar
    nav = [
    {"text": "Homepage", "url": url_for('index')},
    {"text": "My Account", "url": url_for('account')},
    {"text": "About MULe", "url": url_for('about')},
    {"text": "Contact", "url": url_for('contact')},
    {"text": "My Signup", "url": url_for('signup')},
    {"text": "Practical Info", "url": url_for('practical_info')},
    {"text": "FAQ", "url": url_for('FAQ')},
    #{"text": "User", "url": url_for('user')},
    ]

    return dict(navbar = nav)



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/myaccount')
def account():
    return render_template('my_account.html')

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

@app.route('/user/<name>')
def user(name):
    return render_template("user.html",username=name) 

#if __name__ == "__main__":
#    app.run

#if __name__ == "__main__":
#    app.run(host="0.0.0.0")