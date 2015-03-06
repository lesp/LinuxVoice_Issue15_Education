from mcpi import minecraft
from energenie import switch_on, switch_off
from time import sleep

mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    if pos.x == -7.0:
        mc.postToChat("Light On")
        switch_on()
    else:
        switch_off()
