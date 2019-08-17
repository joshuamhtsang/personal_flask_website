from app import make_celery

celery = make_celery()


@celery.task()
def shoot():
    print("shoot!")
    return 0
