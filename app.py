from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Priscilla Mullins(1600-1651) - 10th Great Grandmother - Mayflower"

if __name__ == "__main__":
    app.run(debug=True)