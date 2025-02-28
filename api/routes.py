from flask import Blueprint, jsonify, request, render_template

api = Blueprint('tasks', __name__, 
                static_folder='../static',    # Add these to serve static files
                template_folder='../templates' # Add this to serve templates
)

# In-memory storage for tasks
task_list = []
task_id_counter = 1

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    task = {
        'id': task_id_counter,
        'title': data.get('title'),
        'description': data.get('description'),
        'completed': False
    }
    task_list.append(task)
    task_id_counter += 1
    return jsonify(task), 201

@api.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(task_list), 200

@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in task_list if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in task_list if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['completed'] = data.get('completed', task['completed'])
    return jsonify(task), 200

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global task_list
    task = next((task for task in task_list if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task_list = [t for t in task_list if t['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 204