import RPi.GPIO as GPIO
import time
from evdev import UInput, ecodes as e

GPIO.setmode(GPIO.BCM)
SWITCH_PIN = 17
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ui = UInput()

try:
    while True:
        if GPIO.input(SWITCH_PIN) == GPIO.LOW:
            ui.write(e.EV_KEY, e.KEY_LEFT, 1)  # Send left arrow key
            ui.write(e.EV_KEY, e.KEY_LEFT, 0)
            ui.syn()
            time.sleep(0.5)  # Debounce
finally:
    ui.close()
    GPIO.cleanup()
