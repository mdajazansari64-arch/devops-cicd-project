from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {"id": len(tasks) + 1, "title": data["title"]}
    tasks.append(task)
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)