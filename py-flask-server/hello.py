from flask import Flask, jsonify, abort


app = Flask(__name__)


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


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/text')
def about_me():
    return 'Hi!'

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for t in tasks:
        if t['id'] == int(t['id']) == int(task_id):
            print("ok")
            task = tasks[int(task_id)-1]
            break
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})

'''
    task = filter(lambda t: int(t['id']) == int(task_id), tasks)
    final = task[0]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': final})
'''
    
if __name__ == '__main__':
    app.run(debug=True)