import time
import random
import board
import adafruit_dotstar as dotstar
import digitalio
import neopixel

#version="2020-02-07 02:49:00"

#set up the onboard LED
dots = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1)
#set up the plug-in pixel strip, in this case we are preparing for up to 100 LEDs
pixels = neopixel.NeoPixel(board.A3, 100, brightness=1, auto_write=False)

#set up the pin that reads the button push
touch = digitalio.DigitalInOut(board.D10)
touch.direction = digitalio.Direction.INPUT
touch.pull = digitalio.Pull.DOWN

#set up the pin that the button is connected to - make it a logic 0
gnd = digitalio.DigitalInOut(board.D7)
gnd.direction = digitalio.Direction.OUTPUT
gnd.value = 1

#how long we wait befoce going on to the next colour
next_colour_delay = 0.3
#initialise the lock_timer to 0
lock_timer = 0
#set the lock timer value - this is how long we wait before setting the LED permanently
lock_time_limit = 100000
#delay between steps
step_delay=0.02
#how many LEDs we are going to illuminate
ledcount = 30
#turn on and off the logging to serial console
silent = False

#create the colour matrix
colours = [ 
    {"name": "red", hex: 0xff0000}, 
    {"name": "orange", hex: 0xff2200}, 
    {"name": "yellow", hex: 0xff9900}, 
    {"name": "lime", hex: 0x99ff00}, 
    {"name": "green", hex: 0x00ff00}, 
    {"name": "cyan", hex: 0x1199ff}, 
    {"name": "blue", hex: 0x0000ff}, 
    {"name": "purple", hex: 0x3300ff}, 
    {"name": "magenta", hex: 0xbb00aa}, 
    {"name": "grey", hex: 0x888888}, 
    ]

while True:    
    # perform a little light show, cos we can
    dots[0] = (0xff0000)
    pixels.fill(0xff0000)
    time.sleep(step_delay)

    dots[0] = (0x00ff00)
    pixels.fill(0x00ff00)
    time.sleep(step_delay)

    dots[0] = (0x0000ff)
    pixels.fill(0x0000ff)
    time.sleep(step_delay)

    dots[0] = (0x000000)
    pixels.fill(0x000000)

    #now we go show the colours, going on to the next colour if the button is pressed before the timer runs out!
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

        #now we're done, make the LEDs after the 5th one do a light show.
        while True:
            for c in colours:
                for led in range(5, ledcount + 1):
                    if not silent: print("led[{:3}] to colour[{}] hex[{:06x}]".format(led, c["name"], c[hex]))
                    dots[0] = c[hex]
                    pixels[led] = c[hex]
                    if led > 5: pixels[led -1] = 0x000000
                    dots[0] = c[hex]
                    pixels.write()
                    time.sleep(step_delay)

