from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello !</h1> This is main page"

@app.route("/aboutme")
def aboutme():
    return "this about me page !"

if __name__ == "__main__":
    app.run()