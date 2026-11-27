class TaskNotFound(Exception):
    pass
def get_task(task_id):
    raise TaskNotFound(task_id)
try:
    get_task(5)

except TaskNotFound as error:
    print("Error:", error)