import os
import sys
sys.path.insert(0, os.getcwd())
print "celery config path:", os.getcwd()

BROKER_URL = "redis://103.29.133.*:6379/11"
# CELERY_IMPORTS = ("downloader", "parse")
CELERY_RESULT_BACKEND = "redis://103.29.133.*:6379/12"
CELERY_DISABLE_RATE_LIMITS = True
CELERY_TASK_RESULT_EXPIRES = 1*60
