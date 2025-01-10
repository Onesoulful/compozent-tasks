from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store (replace with a database in production)
tasks = []
task_id_counter = 1

# Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.json
    new_task = {
        "id": task_id_counter,
        "title": data["title"],
        "description": data["description"],
        "status": "pending"
    }
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify(new_task), 201

# Retrieve Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Retrieve a Single Task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

# Update Task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        task.update(data)
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

# Delete Task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
