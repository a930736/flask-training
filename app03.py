#製作表單 接收回傳值
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.values["send"] =="送出":
            return render_template("index.html", name = request.values["user"])
    return render_template("index.html", name ="")


if __name__ =="__main__":
    app.run(debug =True)
