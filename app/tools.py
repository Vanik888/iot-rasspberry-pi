import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  "
          "This is probably because you need superuser privileges.  "
          "You can achieve this by using 'sudo' to run your script")


def init_board():
    OUTPUT_PIN = 23
    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()
    print(mode)
    print('INIT the output pin {} to low'.format(OUTPUT_PIN))
    GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)

