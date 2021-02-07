from celery.bin import beat
from management_lib.tasks import app_celery

if __name__ == "__main__":
    beat.beat(app=app_celery).run(beat=True, task_events=True, pidfile='/tmp/celerybeat.pid', schedule='/tmp/celerybeat-schedule')