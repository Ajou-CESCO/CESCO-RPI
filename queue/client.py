from multiprocessing.managers import BaseManager
class QueueManager(BaseManager): pass
QueueManager.register('get_queue')
m = QueueManager(address=('localhost', 5000), authkey=b'pillintime')
m.connect()
queue = m.get_queue()
while True:
    print(queue.get())