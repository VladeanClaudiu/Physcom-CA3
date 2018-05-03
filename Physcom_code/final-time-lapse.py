import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from os import system
from time import sleep

GPIO.setmode(GPIO.BOARD)

#pin that is uses the circuit
pin_to_circuit = 7


def rc_time (pin_to_circuit):
    count = 0
  
    #Pin outpu
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Pin to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count to hich
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        print('Test 1')
        count += 1
    return count

    while (count < 500):
        camera = PiCamera()
        camera.resolution = (1024, 768)

        for i in range(1000):
            camera.capture('image{0:04d}.jpg'.format(i))
            sleep(10)

            system('convert -delay 10 -loop 0 image*.jpg animation.gif')
        return count

#catch when stop
try:
    # loop
    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()