from app import app
from data.tasks import tasks_list

@app.route('/')
def test():
    return 'Show me the key to the future'

@app.route('/tasks')
def get_all_tasks():
    tasks = tasks_list
    return tasks

@app.route('/tasks/<int:task_id>')
def get_single_task(task_id):
    tasks = tasks_list
    for task in tasks_list:
        if task['id'] == task_id:
            return task
    return {'Error!' f'task ID {task_id} Does not Exist!'}, 404