from celery import Celery
import celeryconfig

app = Celery("crawler", 
        backend=celeryconfig.CELERY_RESULT_BACKEND,
        broker=celeryconfig.BROKER_URL,
        include=["crawler.downloader", "crawler.parse"])

# app.config_from_object("celeryconfig")


if __name__ == "__main__":
    app.start()
