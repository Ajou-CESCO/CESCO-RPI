from multiprocessing.managers import BaseManager
import requests
import datetime

# Main Server URL
server_url="http://175.45.205.29:8080/api/dose/log"

# Consume message from queue and send request to server
def send_request(msg:str):
    print("MSG Received",msg)

    # Parse message
    msg=msg.replace("\n","")
    data=msg.split(" / ")
    json_dict={
        "serial":data[2],
        "index":data[1]
    }
    print(json_dict)
    if json_dict['serial']=="test":
        return

    # Try to send request for 3 times maximum
    for i in range(3):
        try:
            res=requests.patch(url=server_url,
                            json=json_dict,
                            timeout=10)
            print(res.status_code)
            print(res.text)
            return
        except:
            print(f"{str(datetime.datetime.now())} ; Something Went Wrong {i+1} - index: {data[1]}, time: {data[0]}")

# Init Queue

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue')
m = QueueManager(address=('localhost', 5000), authkey=b'pillintime')
m.connect()
queue = m.get_queue()

# Run Process
while True:
    send_request(queue.get())