import RPi.GPIO as GPIO
import time
import threading
import datetime
from multiprocessing.managers import BaseManager

# For Catching Keyboard Interrupt and killing process safely
interrupt_flag=False

# Queue Init
class QueueManager(BaseManager):
    pass

QueueManager.register("get_queue")
m = QueueManager(address=('localhost', 5000),authkey=b'pillintime')
m.connect()
queue=m.get_queue()

# Get Serial Number
serial_fd = open("../serialnumber.txt", "r")
serial_number = serial_fd.readline()

# Pin Used: 4, 17, 27, 22, 23
# Each Pin is mapped to 1, 2, 3, 4, 5
rack_dict={
    4:1,
    17:2,
    27:3,
    22:4,
    23:5
}

# send message to queue
def send_msg(pin_num:int) -> None:
    queue.put(" / ".join([str(datetime.datetime.now()),str(pin_num),serial_number]))

def get_sensor_data(pin_num:int) -> None:
    # Setup Pin
    GPIO.setup(pin_num, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
    # Read Sensor Data for every sec
    try:
        while interrupt_flag==False:
            if GPIO.input(pin_num)==0:
                print(f"{rack_dict[pin_num]} CLOSED")
            elif GPIO.input(pin_num)==1:
                print(f"{rack_dict[pin_num]} OPENED")
                send_msg(rack_dict[pin_num])
            else:
                print(f"{rack_dict[pin_num]} CRITICAL ERROR")
            time.sleep(1)

    except RuntimeError:
        print("GPIO CLEANED ALREADY")

def main() -> None:
    # Make threads for each sensor and run
    try:
        GPIO.setmode(GPIO.BCM)
        thread1 = threading.Thread(target=get_sensor_data,args=[4])
        thread2 = threading.Thread(target=get_sensor_data,args=[17])
        thread3 = threading.Thread(target=get_sensor_data,args=[27])
        thread4 = threading.Thread(target=get_sensor_data,args=[22])
        thread5 = threading.Thread(target=get_sensor_data,args=[23])

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()

    except KeyboardInterrupt:
        interrupt_flag=True
        print("프로세스 종료")
    GPIO.cleanup()

if __name__ == "__main__":
    main()