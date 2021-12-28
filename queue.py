from rq import Queue
from utils import cache

q = Queue(connection=cache)