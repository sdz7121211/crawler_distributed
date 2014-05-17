# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from requests import Request, Session
from crawler.celery_app import app
from celery.contrib.methods import task_method
from crawler_config import headers 


class Downloader(object):

    def __init__(self):
        self.header = headers["default"]

    @app.task(name="Downloader.download", filter=task_method)
    def download(self, url):
        pass

    def __call__(self, url):
        pass


class defaultDownloader(Downloader):

    def __init__(self):
        super(defaultDownloader, self).__init__()
        self.s = Session()

    @app.task(name="defaultDownloader.download", filter=task_method)
    def download(self, url, proxies=None, params=None):
        req = Request(
                "GET", url,
                params=params,
                headers=self.header)
        prep = self.s.prepare_request(req)
        resp = self.s.send(
                prep,
                proxies=proxies,
                timeout=5)               
        if resp.status_code == 200:
            return resp.text
        else:
            return None

    @app.task(name="defaultDownloader.download", filter=task_method)
    def __call__(self, url):
        self.download(url)


if __name__ == "__main__":
    a = defaultDownloader()
