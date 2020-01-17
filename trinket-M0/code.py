import time
import random
import board
import adafruit_dotstar as dotstar
import touchio
import neopixel

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
dots = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1)
pixels = neopixel.NeoPixel(board.A3, 100, brightness=1, auto_write=True)

touch_pad = board.A0

# HELPERS
# a random color 0 -> 224
def random_color():
    return random.randrange(0, 7) * 32

touch = touchio.TouchIn(touch_pad)
n = 0.3
i = 0
m = 10000
dots[0] = (0x000000)
pixels.fill(0x000000)

# while True:
#     print("pulses[{}])".format(pulses[0]))
#     speed=0.200
#     time.sleep(speed)

while True:    
    print(touch.value)
    # print("pulses[{}])".format(pulses[0]))
    # pixels[5] = 0x0000ff
    # time.sleep(0.4)

    speed=0.02
    colour=0xff0000
    for led in range(0, 5):
        print("led[{}]".format(led))
        pixels[led] = colour
        dots[0] = colour
        time.sleep(speed)

    colour=0x00ff00
    for led in range(0, 5):
        print("led[{}]".format(led))
        pixels[led] = colour
        dots[0] = colour
        time.sleep(speed)

    colour=0x0000ff
    for led in range(0, 5):
        print("led[{}]".format(led))
        pixels[led] = colour
        dots[0] = colour
        time.sleep(speed)

    colour=0x000000
    for led in range(0, 5):
        print("led[{}]".format(led))
        pixels[led] = colour
        dots[0] = colour
        time.sleep(speed)


    while True:
        #blue
        colour = (0x0000ff)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                print("led[{}]".format(led))
                pixels[led] = colour
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #red
        colour = (0xff0000)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                print("led[{}]".format(led))
                pixels[led] = colour
            i=0
            print("c[{}] i[{}]".format(colour, i))
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #orange
        colour = (0xff3300)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                print("led[{}]".format(led))
                pixels[led] = colour
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #yellow
        colour = (0xffee00)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                print("led[{}]".format(led))
                pixels[led] = colour
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #lime
        colour = (0x77ff00)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                print("led[{}]".format(led))
                pixels[led] = colour
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #green
        colour = (0x00ff00)
        if i<m :
            dots[0] = colour
            pixels.fill(colour)
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #cyan
        colour = (0x0088ff)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                # print("led[{}]".format(led))
                pixels[led] = colour
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #purple
        colour = (0x3300ff)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                # print("led[{}]".format(led))
                pixels[led] = colour
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #magenta
        colour = (0xaa00aa)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                # print("led[{}]".format(led))
                pixels[led] = colour
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        #grey
        colour = (0xa9a9a9)
        if i<m :
            dots[0] = colour
            for led in range(0, 5):
                # print("led[{}]".format(led))
                pixels[led] = colour
            i=0
        while i < m and not touch.value : i=i+1
        while not touch.value and i < m: pass       
        time.sleep(n)

        while True:
            # print("pulses[{}])".format(pulses[0]))
            speed=0.002
            # time.sleep(speed)

            colour=0xff0000
            for led in range(0, 24):
                # print("led[{}]".format(led))
                pixels[led + 5] = colour
                pixels[led + 5 + 24] = colour
                time.sleep(speed)

            colour=0x888888
            for led in range(0, 24):
                # print("led[{}]".format(led))
                pixels[led + 5] = colour
                pixels[led + 5 + 24] = colour
                time.sleep(speed)

            colour=0x0000ff
            for led in range(0, 24):
                # print("led[{}]".format(led))
                pixels[led + 5] = colour
                pixels[led + 5 + 24] = colour
                time.sleep(speed)
