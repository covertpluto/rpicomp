from gpiozero import LED
import RPi.GPIO as GPIO
import time

IDLE_TIMEOUT = 120 # in seconds

pirpin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirpin, GPIO.IN)

led = LED(27)

idle_start = time.time()

def check_idle():
    if time.time() - idle_start > IDLE_TIMEOUT:
        print("Idle timer passed")
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
        return True
    else:
        time.sleep(0.1)
        return False

def set_timer(n):
    global idle_start
    print("You moved. Resetting idle timer...")
    idle_start = time.time()

GPIO.add_event_detect(pirpin, GPIO.BOTH, callback=set_timer, bouncetime=300)

while True:
    print(round(time.time() - idle_start, 1))
    check_idle()

