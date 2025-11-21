from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from my API!"})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT if provided
    app.run(host='0.0.0.0', port=port)





