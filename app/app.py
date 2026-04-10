from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, secure world!"

@app.route("/ping")
def ping():
    # BAD: command injection risk - Semgrep will flag this
    host = request.args.get("host", "localhost")
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True)
    return result.stdout.decode()

if __name__ == "__main__":
    app.run(debug=True) # BAD: debug=True in prod - Semgrep will flag this
