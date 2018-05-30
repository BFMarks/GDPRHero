from __future__ import absolute_import, unicode_literals
import random
from celery.task import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# celery -A GDPRHero  worker -l info
# celery -A GDPRHero  beat -l info -S django
# redis-server

@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    logger.info('Adding {0} + {1}'.format(x, y))
    return total

@task(name="sum_list_numbers")
def xsum(numbers):
	return sum(numbers)