from multiprocessing.managers import BaseManager
from queue import Queue

# Init Queue Server
queue = Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue', callable=lambda:queue)
m = QueueManager(address=('localhost', 5000), authkey=b'pillintime')

# Run Queue Server
s = m.get_server()
s.serve_forever()