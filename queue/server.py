from multiprocessing.managers import BaseManager
from queue import Queue
queue = Queue()
class QueueManager(BaseManager): pass
QueueManager.register('get_queue', callable=lambda:queue)
m = QueueManager(address=('localhost', 5000), authkey=b'pillintime')
s = m.get_server()
s.serve_forever()