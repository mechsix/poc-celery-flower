from celery import Celery
from .tasks import task1, task2

broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379/0'

worker = Celery('main_worker', broker=broker, backend=backend)

task1 = worker.task(task1)
task2 = worker.task(task2)
