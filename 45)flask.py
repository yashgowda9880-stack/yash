from flask import Flask
app = Flask (__name__)
@app.route("/hello")
def hello():
    return "hello from Backend!"
if __name__ == "__main__":
    app.run(debug=True, port=3000)