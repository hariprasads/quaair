__author__ = 'hanumesh'

from celery import task
from celery.task import Task, PeriodicTask
from datetime import timedelta
import sys
import os
from air_quality_analyser import settings
sys.path.append(os.path.join(settings.BASE_DIR, 'analyser'))
from analyser import user_air_quality_data
from celery.schedules import crontab


class UpdateContent(PeriodicTask):
    """
    This is class used to update build number
    """
    # run update query every 25th minute of every 2 hours
    if settings.TASK_DEBUG:
        run_every = timedelta(seconds=60)
    else:
        run_every = crontab(minute='*/15')

    def run(self):
        user_air_quality_data.run_update_content()


from celery import task, group, Celery
app = Celery('portal')
@app.task
def Test():
    import time
    time.sleep(10)
if __name__ == '__main__':
    print("sdfsd")