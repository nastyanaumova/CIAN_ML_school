from time import sleep
from json import dumps
from confluent_kafka import Producer
import datetime
from random import randrange
import random
import string

def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

conf = {'bootstrap.servers' : '10.156.0.3:2181, 10.156.0.4:2181, 10.156.0.5:2181',
        'group.id' : 'anaumova'}
producer = Producer(conf)
while True:
    data={}
    data = {randrange(0,101): ((str(datetime.datetime.now())[:-3]), randomString())}
    producer.produce(topic='anaumova', value=dumps(data).encode('utf-8')
    sleep(5)