from multiprocessing.managers import BaseManager
import datetime

class QueueManager(BaseManager):
    pass

QueueManager.register("get_queue")

m = QueueManager(address=('localhost', 5000),authkey=b'pillintime')
m.connect()
queue=m.get_queue()

serial_number="test"

def send_msg(pin_num:int) -> None:
    queue.put(" / ".join([str(datetime.datetime.now()),str(pin_num),serial_number]))

send_msg(0)