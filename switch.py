import RPi.GPIO as GPIO
from time import sleep
from energenie import switch_on, switch_off

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)
switch_off()
status = "off"
while True:
    GPIO.wait_for_edge(26, GPIO.FALLING)
    switch_on()
    status = "on"
    sleep(0.5)
    if status == "on":
        GPIO.wait_for_edge(26, GPIO.FALLING)
        switch_off()
        status = "off"
        sleep(0.5)
