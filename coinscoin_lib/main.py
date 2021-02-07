from celery.bin import worker
from coinscoin_lib.tasks import app_celery

if __name__ == "__main__":
    worker.worker(app=app_celery).run(beat=True, task_events=True)
