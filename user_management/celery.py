from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')
app = Celery('user_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_connection_retry_on_startup = True  
app.autodiscover_tasks()