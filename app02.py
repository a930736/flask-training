# redirect to the same page index.html
from flask import Flask
from flask import render_template
from flask import url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/second")
def test():
    return redirect(url_for("index"))

if __name__ =="__main__":
    app.run(debug =True)
