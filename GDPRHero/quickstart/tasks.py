from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task

@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
    print("QS")
    total = x * (y * random.randint(3, 100))
    print(total)
    return total

@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)