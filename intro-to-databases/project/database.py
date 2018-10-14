import psycopg2


def connect():
    return psycopg2.connect(user='sarahschneider', password='Q-@VWfZPUbM3M5xCyRTu', database="learning", host="localhost")