import RPi.GPIO as GPIO
import time
import threading
import os
import datetime
from multiprocessing.managers import BaseManager

interrupt_flag=False

class QueueManager(BaseManager):
    pass
QueueManager.register("get_queue")
m = QueueManager(address=('localhost', 5000),authkey=b'pillintime')
m.connect()
queue=m.get_queue()

# Get Serial Number
serial_fd = open("../serialnumber.txt", "r")
serial_number = serial_fd.readline()

def send_msg(pin_num):
    queue.put(" / ".join([str(datetime.datetime.now()),str(pin_num),serial_number]))

def get_sensor_data(pin_num):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_num, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    try:
        while interrupt_flag==False:
            if GPIO.input(pin_num)==0:
                print(f"{pin_num} CLOSED")
            elif GPIO.input(pin_num)==1:
                print(f"{pin_num} OPENED")
                send_msg(pin_num)
            else:
                print(f"{pin_num} CRITICAL ERROR")
            time.sleep(1)
    except RuntimeError:
        print("GPIO CLEANED ALREADY")

def main():
    try:
        GPIO.setmode(GPIO.BCM)
        thread1 = threading.Thread(target=get_sensor_data,args=[4])
        thread2 = threading.Thread(target=get_sensor_data,args=[17])
        thread3 = threading.Thread(target=get_sensor_data,args=[27])

        thread1.start()
        thread2.start()
        thread3.start()
        
        thread1.join()
        thread2.join()
        thread3.join()
    except KeyboardInterrupt:
        interrupt_flag=True
        print("프로세스 종료")
    GPIO.cleanup()
    pipe_writer.close()

if __name__ == "__main__":
    main()