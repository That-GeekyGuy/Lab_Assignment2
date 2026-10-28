from flask import Flask, jsonify, request

app = Flask(__name__)


def add(a, b):
    return a + b


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/add")
def add_route():
    try:
        a = float(request.args["a"])
        b = float(request.args["b"])
    except (KeyError, ValueError):
        return jsonify(error="query params a and b must be numbers"), 400
    return jsonify(result=add(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
