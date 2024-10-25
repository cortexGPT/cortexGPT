from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Cortex!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/health')
def health_check():
    return jsonify({"status": "running"})


@app.route('/')
def home():
    return render_template('index.html')
