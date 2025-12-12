#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/')
def index():
    return jsonify({
        "message": "ChainLock secured application",
        "signed": True,
        "sbom": "attached"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
