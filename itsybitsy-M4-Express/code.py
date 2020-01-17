import time
import random
import board
import adafruit_dotstar as dotstar
import digitalio
import neopixel

dots = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1)
pixels = neopixel.NeoPixel(board.A3, 100, brightness=1, auto_write=False)

touch = digitalio.DigitalInOut(board.D10)
touch.direction = digitalio.Direction.INPUT
touch.pull = digitalio.Pull.DOWN

gnd = digitalio.DigitalInOut(board.D7)
gnd.direction = digitalio.Direction.OUTPUT
gnd.value = 1


next_colour_delay = 0.3
lock_timer = 0
lock_time_limit = 100000
speed=0.02

speed = 0.0
ledcount = 30
silent = False

colours = [ 
    {"name": "red", hex: 0xff0000}, 
    {"name": "orange", hex: 0xff3300}, 
    {"name": "yellow", hex: 0xff9900}, 
    {"name": "lime", hex: 0x99ff00}, 
    {"name": "green", hex: 0x00ff00}, 
    {"name": "cyan", hex: 0x0088ff}, 
    {"name": "blue", hex: 0x0000ff}, 
    {"name": "purple", hex: 0x3300ff}, 
    {"name": "magenta", hex: 0xaa00aa}, 
    {"name": "grey", hex: 0x888888}, 
    ]

while True:    
    if not silent: print("touch[{}]".format(touch.value))

    dots[0] = (0xff0000)
    pixels.fill(0xff0000)
    time.sleep(speed)

    dots[0] = (0x00ff00)
    pixels.fill(0x00ff00)
    time.sleep(speed)

    dots[0] = (0x0000ff)
    pixels.fill(0x0000ff)
    time.sleep(speed)

    dots[0] = (0x000000)
    pixels.fill(0x000000)

    while True:
        for c in colours:
            if lock_timer < lock_time_limit :
                #set the onboard LED colour
                dots[0] = c[hex]
                #set the LEDs on the external board (start at 0 end at (but not including) 5)
                for led in range(0, 5):
                    if not silent: print("led[{:3}] to colour[{}] hex[{:06x}]".format(led, c["name"], c[hex]))
                    pixels[led] = c[hex]
                    pixels.write()
                #restart the lock timer
                lock_timer = 0
            #here we are waiting for the lock timer to expire or for a touch input
            while lock_timer < lock_time_limit and not touch.value: 
                lock_timer = lock_timer + 1
            #check - did we get a touch input? if not, stay here forever (we are locked)
            while not touch.value and lock_timer < lock_time_limit: 
                pass       
            #wait a little while before going on to the next LED colour
            time.sleep(next_colour_delay)

        while True:
            for c in colours:
                for led in range(5, ledcount + 1):
                    if not silent: print("led[{:3}] to colour[{}] hex[{:06x}]".format(led, c["name"], c[hex]))
                    dots[0] = c[hex]
                    pixels[led] = c[hex]
                    if led > 5: pixels[led -1] = 0x000000
                    dots[0] = c[hex]
                    pixels.write()
                    time.sleep(speed)

