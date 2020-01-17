# Description
Lots of the racers at Diehard have been asking me for the detail of the LEDs we've been trying out. 
I have to be clear here - this is in no way a guarantee that the instructions will work for you and there is no guarantee of any kind that you won't damamge anything.  I cannot and will not accept liability for anything you do to your own equipment.

The LEDs are in supports of an idea that Diehard are promoting - and that is to add LEDs to racecars in much the same way that we do fordrone racing.  The idea revolves around the driver sets the LED colour to indicate his grid position (for instance blue = #1, green = #2 etc etc) at the start of each race.  This identifies the car in a simple fashion to improve the viewer experience (the Race Director can simply mention the cars by the LED colour) and of course - it looks pretty cool too.

We've discussed several ideas for supplying the boards, and we feel that the most practical method for now is to provide instructions.  There are plenty of us that can build these, and for those that don't feel comfortable, I'm certain that there are a couple of club members who would be happy to put one together for you.

The instructions here are meant to cater for a 5-LED setup for the racing.  The boards *can* drive thousands of LEDs, but please be aware that each LED draws current - and you can expect 60-75mA for each LED "pixel".  (each of the 3x RGB LEDs in the pixels draw ~20-25mA each).

Should you wish to add more LEDs, please make sure your equipment can handle the current.  I chose to run mine from the receiver power rail, but you do have to consider that the RX and the steering servo are also using this power rail.

We would like to strongly recommend that we all use (as close as we can) a strip of 5 LEDs, preferably cut from a 144-LED/meter strip as this will help us all achieve a similar level of brightness across all the cars on the grid.

# Examples of Parts
* LED board, WS2812B DC 5V LED Strip RGB, 1 Meter, 144 LEDs, Black PCB, cut into 5-LED sections
  * Amazon https://smile.amazon.com/gp/product/B01CDTEJR0/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1
* Adafruit Board
  * Adafruit Trinket M0 (basic LED functionality, not fast enough to cope well with PWM input processing) - https://www.adafruit.com/product/3500
  * Adafruit Trinket M0 Express (Can be used for PWM input) - https://www.adafruit.com/product/3727
* 2x 1N4001 diodes
  * Amazon - https://smile.amazon.com/gp/product/B071YWNBVM/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1
* Servo Cables
  * Amazon - https://smile.amazon.com/gp/product/B07V4558HC/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
* Heatshrink tubing
  * Amazon - https://smile.amazon.com/gp/product/B009IIOQ7S/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1
  
 
  
 
