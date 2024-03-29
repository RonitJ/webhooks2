from flask import Flask 
from flask import Flask, jsonify
from flask import request
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

app = Flask(__name__) 
  
#@app.route('/hello') 
#def hello_world(): 
#    return 'Hello World'
  
# main driver function 
#if __name__ == '__main__': 
  
#    app.run()
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

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
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
@csrf_exempt
def hello(request):
    return HttpResponse('pong')

if __name__ == '__main__':
    app.run(debug=True)
