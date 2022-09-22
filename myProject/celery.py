import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')

# Starting celery app
# COMMAND TO START WORKERS -> "celery -A myProject worker -l info -P gevent --pool=solo"
app = Celery('myProject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
