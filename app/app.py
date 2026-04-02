from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/hello")
def hello():
    return "Hello world"


if __name__ == "__main__":
    # Demo-friendly: bind explicitly to localhost.
    app.run(host="127.0.0.1", port=5000)

