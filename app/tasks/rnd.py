from . import celery

@celery.task
def new():
    from app.new import main
    main()

@celery.task
def predict(dataInput):
    from app.predict import main
    # dataInput=[5.1,3.3,1.7,0.5]
    name = main(dataInput)
    return name