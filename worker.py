from utils import cache
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

if __name__ == '__main__':
    with Connection(cache):
        worker = Worker(map(Queue, listen))
        worker.work()
