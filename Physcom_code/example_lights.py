import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#circuit pin used
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #pin output
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #pin input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count till pin high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when ctr+c 
try:
    # Main
    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()