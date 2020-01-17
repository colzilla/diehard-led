![Trinket M0](https://github.com/colzilla/diehard-led/blob/master/images/3500-01.jpg)

Power from the RX (5-6V) is fed into the BAT pin via 1 or 2 1N4001 diodes in series.  
Each diode results in a 0.6v drop as the current passes.
On the first car I tried my RX voltage was 6V, so after the 2x diodes, the voltage that made it to the Trinket was 4.8V.
The Trinket (and the ItsyBitsy) is fine with a 6V input voltage, however they use a 3.3v output signal to the LEDs, and the LEDs need an in put signal that is greater than a certain percentage of the Vin or they won't 'hear' the command.

Ground from the RX goes direct to ground.

The output lead BLACK wire goes to ground
The output lead WHITE wire goes to the BAT pin (so it gets the lower voltage after the diodes)
The output lead RED wire goes to pin 3, a digital out pin.

Connect a flylead to pin 1, this will be the touch-input lead.  Connect it to a touch pad of your choice.

Connect the Trinket to your PC, and it will appear as a USB flash drive named CIRCUITPY.  
Copy the code.py file and the lib folder to the flash drive, and you should see the onboard LED flash red, green then blue, and change when you touch the touch-pin!

Note: the Trinket (including the onbord LED) is powered from USB and/or external power.  The external LEDs are from external power only.  It's fine to connect external power and USB at the same time.

