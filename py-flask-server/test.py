
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

def get_task(task_id):
    for t in tasks:
        if t['id'] == int(t['id']) == int(task_id):
            print("ok")
            task = filter(task_id, tasks)
            break
    return print(task)

get_task(1)