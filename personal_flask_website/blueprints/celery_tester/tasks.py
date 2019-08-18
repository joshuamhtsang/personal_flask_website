from app import make_celery
import json
import requests

celery = make_celery()


@celery.task()
def shoot():
    print("shoot!")
    return 0


@celery.task()
def send_sleeper_request(endpoint_url, payload):
    response = requests.get(endpoint_url, params=payload)

    return json.loads(response.text)
