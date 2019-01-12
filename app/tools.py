import os

try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    print("Error importing RPi.GPIO!  "
          "This is probably because you need superuser privileges.  "
          "You can achieve this by using 'sudo' to run your script")


def init_board():
    OUTPUT_PIN = 13
    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()
    print(mode)
    print('INIT the output pin {} to low'.format(OUTPUT_PIN))
    GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)


def get_pin_state(pin):
    """
    Returns the pin state: 1 if it is high 0 otherwise

    :return:
    """
    return GPIO.input(pin)


def set_pin_state(pin, value):
    """
    Turns on or off the pin on device

    :param pin:
    :param value:
    :return:
    """
    GPIO.output(pin, value)


def get_cpu_temperature():
    """
    Returns the CPU temperature in celsius

    :return:
    """
    temp = os.popen("vcgencmd measure_temp").readline()\
        .replace('temp=', "")\
        .replace("'C", "")\
        .strip()
    return temp
