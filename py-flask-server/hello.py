from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)

# (Ошибка 400)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


# задание 0.3 (Ошибка 404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# задание 0.0 (запуск сервера)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/text')
def about_me():
    return 'Hi!'

# задание 0.1 (полный список данных)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# задание 0.2 (API с запросом по ID)
''' # код из хабра
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task1 = list(filter(lambda t: t['id'] == task_id, tasks))
    final = task1[0]
    if len(task1) == 0:
        abort(404)

    return jsonify({'task': final})
'''

# код из Github: https://github.com/miguelgrinberg/REST-tutorial/blob/master/rest-server.py

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


''' # Мой код

    for t in tasks:
        if int(t['id']) == int(task_id):
            print("ok")
            task = tasks[int(task_id)-1]
            break
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})
'''

# задание 0.5 (метод POST)

'''
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
'''

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    
    task = {
        'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)