from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health_check():
    return jsonify({"status": "running"})


@app.route('/submit', methods=['POST'])
def handle_form_submission():
    user_input = request.form['user_input']
    # Sanitize input and process it
    return f"Received: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)
