# Celery.
CELERY_BROKER_URL = 'redis://:@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5