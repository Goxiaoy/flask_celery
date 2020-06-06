from flask import Flask
from . import api


@api.route('tasks/one/run')
def task_one():
    '''
        Queue task_one to background worker
        ---
        responses:
          200:
            description: return task id
    '''
    from app.tasks.task_one import one
    task=one.apply_async()
    return task.id

@api.route('tasks/one/<string:taskId>')
def task_one_status(taskId):
    ''' 
        Query background task status
        ---
        parameters:
          - in: path
            name: taskId
            required: true
            description: The ID of Task
            type: string
        responses:
          200:
            description: task Status
    '''
    from app.tasks.task_one import one
    return one.AsyncResult(taskId).state