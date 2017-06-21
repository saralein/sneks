from sense_hat import SenseHat
from time import sleep
import sprites

sense = SenseHat()

def hatch():
  # SunFounder touch switch

def wag():
  while True:
    sense.set_pixels(sprites.Sneks)
    sleep(0.5)
    sense.set_pixels(sprites.Sneks_wag)
    sleep(0.5)
