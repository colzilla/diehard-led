import time
import random
import board
import adafruit_dotstar as dotstar
import touchio
import neopixel

#not the prettiest code - and a lot of repetition but I've tried to make the code simple to understand for non-coders

#this is the single LED omn the Trinket board
dots = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1)

#this is the LEDs connected to the board, currently managing up to 100 LEDs
pixels = neopixel.NeoPixel(board.A3, 100, brightness=1, auto_write=True)

#this is the pin we will use for the touch-pin - to change the colours
touch_pad = board.A0
touch = touchio.TouchIn(touch_pad)

next_colour_delay = 0.3
lock_timer = 0
lock_time_limit = 10000
speed=0.02

dots[0] = (0x000000)
pixels.fill(0x000000)


while True:    
    print(touch.value)

    #red
    colour=0xff0000
    #set the LED colours sequentially, slowly enough that we can see it
    for led in range(0, 5):
        print("led[{}]".format(led))
        pixels[led] = colour
        dots[0] = colour
        time.sleep(speed)

    #green
    colour=0x00ff00
    #set the LED colours sequentially, slowly enough that we can see it
    for led in range(0, 5):
        print("led[{}]".format(led))
        pixels[led] = colour
        dots[0] = colour
        time.sleep(speed)

    #blue
    colour=0x0000ff
    #set the LED colours sequentially, slowly enough that we can see it
    for led in range(0, 5):
        print("led[{}]".format(led))
        pixels[led] = colour
        dots[0] = colour
        time.sleep(speed)

    #black/off
    colour=0x000000
    #set the LED colours off, slowly enough that we can see it
    for led in range(0, 5):
        print("led[{}]".format(led))
        pixels[led] = colour
        dots[0] = colour
        time.sleep(speed)

#this really belongs in a loop and we cycle through all the colours in a list, but for now, it's just sequential 
    while True:
        #blue
        colour = (0x0000ff)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #red
        colour = (0xff0000)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #orange
        colour = (0xff3300)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #yellow
        colour = (0xffee00)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #lime
        colour = (0x77ff00)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #green
        colour = (0x00ff00)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #cyan
        colour = (0x0088ff)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #purple
        colour = (0x3300ff)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #magenta
        colour = (0xaa00aa)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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

        #grey
        colour = (0xa9a9a9)
        #if we are still allowed to change the colour (ie not locked):
        if lock_timer < lock_time_limit :
            #set the onboard LED colour
            dots[0] = colour
            #set the LEDs on the external board (start at 0 end at (but not including) 5)
            for led in range(0, 5):
                print("setting led[{}] colour [{:06x}]".format(led, colour))
                pixels[led] = colour
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
