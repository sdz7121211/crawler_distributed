# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from crawler.celery_app import app
from celery.contrib.methods import task_method


class Parse(object):

    def __init__(self):
        pass

    @app.task(name="Parse.parse", filter=task_method)
    def parse(self, text):
        pass

    def __call__(self):
        pass


class testParse(Parse):

    def __init__(self):
        pass

    @app.task(name="testParse.parse", filter=task_method)
    def parse(self, text):
        print text[:100]

    def __call__(self):
        pass
