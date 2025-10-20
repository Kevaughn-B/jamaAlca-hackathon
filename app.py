from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "JamaAlca Backend Running! Thanks to Kev!"

if __name__ == "__main__":
    app.run(debug=True)