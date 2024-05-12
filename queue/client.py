from multiprocessing.managers import BaseManager
import requests
import datetime

server_url="http://175.45.205.29:8080/api/cabinet/sensor"

def send_request(msg:str):
    data=msg.split(" / ")
    json_dict={
        "serial":data[2],
        "index":data[1]
    }
    for i in range(3):
        try:
            res=requests.post(url=server_url,
                            json=json_dict,
                            timeout=10)
            print(res.status_code)
            print(res.text)
            return
        except:
            print(f"{str(datetime.datetime.now())} ; Something Went Wrong {i+1} - index: {data[1]}, time: {data[0]}")

class QueueManager(BaseManager): pass

QueueManager.register('get_queue')
m = QueueManager(address=('localhost', 5000), authkey=b'pillintime')
m.connect()
queue = m.get_queue()

while True:
    send_request(queue.get())