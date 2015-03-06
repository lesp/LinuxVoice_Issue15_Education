"""
Linux Voice Educational Resource
Inputs and Outputs
Creating a charging station for your mobile phone
For this you will need an Energenie unit
"""

from energenie import switch_on, switch_off
from time import sleep
import easygui as eg
def timer():
    t = float(eg.enterbox(title="Linux Voice Phone Charging?", msg="How long shall I charge your phone for (in minutes)?"))
    t = t * 60
    switch_on()
    sleep(t)
    switch_off()

while True:
    choice = eg.choicebox(title="Linux Voice Phone Charging",msg="Would you like to charge your phone?", choices=("Yes","No"))
    if choice != "No":
        timer()
    else:
        print("All off")
        switch_off()
        break
