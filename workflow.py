# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from crawler.celery_app import app
import threading
import redis
import redis_config
import traceback
from crawler.downloader import defaultDownloader
from celery import group
from celery import subtask 
import json


@app.task()
def parsetest():
    print "test"

parse_map_test = {"parsetest": parsetest}


class Workflow(object):

    def __init__(self, parse_map=parse_map_test, downloader=defaultDownloader().download):
        super(Workflow, self).__init__()
        self.redis = redis.StrictRedis(host=redis_config.host, port=redis_config.port, db=redis_config.db)
        self.parse_map = parse_map
        self.downloader = downloader
        
    def run(self):
        while True:
            try:
                priority, details = self.redis.blpop([str(i) for i in range(10)])
                print details
                details = json.loads(details)
                url = details["url"]
                parse = self.parse_map[details["parse"]]
                (self.downloader.s(url) | parse.s()).delay()
            except:
                print traceback.format_exc()
            

            
if __name__ == "__main__":
    a = Workflow(parse_map_test)
    a.run()

