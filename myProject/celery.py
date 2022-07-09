import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')

# Starting celery app
app = Celery('myProject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
