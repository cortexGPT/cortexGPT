from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health_check():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    app.run(debug=True)
