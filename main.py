from flask import Flask, redirect, url_for, render_template, flash
import secret
import forms
import sys

app = Flask(__name__)

app.config['SECRET_KEY'] = secret.secret_key


#Navigation bar

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
    {"text": "My profile", "url": url_for('user',username="user.username")}, # TODO: make dynamic
    {"text": "Name", "url": url_for('name')},
    ]

    return dict(navbar = nav)



#Regular pages

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

@app.route('/user/<username>')
def user(username):
    return render_template("user.html",username=username) 

@app.route('/name', methods=['GET', 'POST'])
def name():
    firstName = None
    lastName = None
    email = None
    validateEmail = None
    password = None
    validatePassword = None
    phone = None
    mensaID = None
    birthday = None
    snoring = None
    diet = None
    otherdiet = None
    country = None
    form = forms.UserForm()

    if form.validate_on_submit():
        
        flash("Form submitted successfully")

        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        validateEmail = form.validateEmail.data
        password = form.password.data
        validatePassword = form.validatePassword.data
        phone = form.phone.data
        mensaID = form.mensaID.data
        birthday = form.birthday.data
        snoring = form.snoring.data
        diet = form.diet.data
        otherdiet = form.otherdiet.data
        country = form.country.data

        form.firstName.data = ''
        form.lastName.data = ''
        form.email.data = ''
        form.validateEmail.data = ''
        form.password.data = ''
        form.validatePassword.data = ''
        form.phone.data = ''
        form.mensaID.data = ''
        form.birthday.data = ''
        form.snoring.data = ''
        form.diet.data = ''
        form.otherdiet.data = ''
        form.country.data = ''
        
        
        print(f'''
            Name: {firstName} {lastName}
            Email: {email}
            Password: {password}
            Phone number: {phone}
            mensaID: {mensaID}
            Date of Birth: {birthday}
            Snoring: {snoring}
            Diet: {diet}:{otherdiet}
            Country: {country}''',
        file=sys.stderr)
        
        return render_template('name.html',
        firstName = firstName,
        lastName = lastName,
        email = email,
        validateEmail = validateEmail,
        password = password,
        validatePassword = validatePassword,
        phone = phone,
        mensaID = mensaID,
        birthday = birthday,
        snoring = snoring,
        diet = diet,
        otherdiet = otherdiet,
        country = country,
        form = form)
    else:
        flash("Error in submission")
        return render_template('name.html', form=form)
        





#Error pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


#if __name__ == "__main__":
#    app.run

#if __name__ == "__main__":
#    app.run(host="0.0.0.0")