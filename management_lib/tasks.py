from coinscoin_lib.config_manager import ConfigManager
from coinscoin_lib.tasks import data_dump_task,app_celery

@app_celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(int(ConfigManager.get_config().data_dump_task), data_dump_task.s(), name="data_dump")
    pass
