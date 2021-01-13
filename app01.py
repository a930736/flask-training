from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def test(name=None):
    if name ==None:
        return "Hello World"
    return "Hello "+name +"!"

if __name__ =="__main__":
    app.run(debug =True)
