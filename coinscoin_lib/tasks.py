from celery import Celery
from coinscoin_lib.config_manager import ConfigManager
from coinscoin_lib.data_dump import DataDump

app_celery = Celery('coinscoin_lib.tasks', backend=ConfigManager.get_config().internal_redis_connection_string,
                    broker=ConfigManager.get_config().internal_redis_connection_string)
app_celery.conf.update()


@app_celery.task
def data_dump_task():
    print("Data_dump_task")
    DataDump().run_data_dump_master()
