from __future__ import absolute_import,unicode_literals
import os 

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_with_django.settings')

app = Celery('celery_with_django')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace ='CELERY')


#Celery Beat Settings

app.conf.beat_schedule = {
    "send_mail_everyday_at_3":{
        "task":"send_mail_app.tasks.send_mail_func",
        "schedule":crontab(hour=13,minute=12),
        
    }
}

app.autodiscover_tasks(packages=None, related_name='tasks', force=False)

@app.task(bind= True)
def debug_task(self):
    print(f'Request: {self.request!r}')