from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/favNumber/<int:n>")
def favNumber(n):
    result = {
        "My Favourite Number" : n
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)