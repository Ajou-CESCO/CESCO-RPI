import datetime
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

def test():
    QueueManager.register('get_queue')
    m = QueueManager(address=('localhost', 5000), authkey=b'pillintime')
    m.connect()
    queue = m.get_queue()
    msg=queue.get()
    print(f"Type: {type(msg)}")
    print(f"MSG: {msg}")

test()