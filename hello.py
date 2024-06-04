from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello!</p>"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

#if __name__ == "__main__":
#    app.run(host="0.0.0.0")