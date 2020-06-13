from flask import Flask,request

from . import api


@api.route('tasks/rnd/new')
def task_new():
    '''
        Queue rnd new to background worker
        ---
        responses:
          200:
            description: return task id
    '''
    from app.tasks.rnd import new
    task=new.apply_async()
    return task.id

@api.route('tasks/rnd/predict',methods=['POST'])
def task_predict():
    ''' 
        Queue rnd predict task
        ---
        parameters:
          - in: body
            name: body
            required: true
            schema:
                id: PredictInput
                required:
                    - data
                properties:
                    data:
                        type: array
                        items: 
                            type: number
                            format: double
                        description: data array
                        default: [5.1,3.3,1.7,0.5]
        responses:
          200:
            description: task id
    '''
    from app.tasks.rnd import predict
    dataInput=request.json["data"]
    task=predict.apply_async(args=[dataInput])
    return task.id