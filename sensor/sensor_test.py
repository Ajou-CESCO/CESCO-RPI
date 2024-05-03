import RPi.GPIO as GPIO
import time
import threading

interrupt_flag=False

def get_sensor_data(pin_num):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_num, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    try:
        while interrupt_flag==False:
            if GPIO.input(pin_num)==0:
                print(f"{pin_num} CLOSED")
            elif GPIO.input(pin_num)==1:
                print(f"{pin_num} OPENED")
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

if __name__ == "__main__":
    main()

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# while True:
#     time.sleep(1)
#     if GPIO.input(4)==0:
#         print(f"{4} CLOSED")
#     elif GPIO.input(4)==1:
#         print(f"{4} OPENED")
#     else:
#         print(f"{4} CRITICAL ERROR")