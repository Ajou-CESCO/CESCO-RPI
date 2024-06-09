import RPi.GPIO as GPIO
import time

rack_dict={
    4:1,
    17:2,
    27:3,
    22:4,
    23:5
}

def get_sensor_data(pin_num: int):
    GPIO.setup(pin_num, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    return GPIO.input(pin_num)

def test():
    GPIO.setmode(GPIO.BCM)
    for i in rack_dict.keys():
        while get_sensor_data(i)==1:
            print(f"Pin {i} is still opened")
            time.sleep(3)
    print("All Pins Are Tested, All Connected")