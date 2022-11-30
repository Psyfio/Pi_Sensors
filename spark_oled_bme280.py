from __future__ import print_function, division
import qwiic_bme280
import qwiic_micro_oled
import time
import sys
import math
import os

def soc_temp():
	temp = os.popen("vcgencmd measure_temp").readline()
	return (temp.replace("temp=","").replace("'C","").replace("\n",""))

mySensor = qwiic_bme280.QwiicBme280()
myOLED = qwiic_micro_oled.QwiicMicroOled()

if not myOLED.connected:
	print("The Qwiic Micro OLED device isn't connected to the system. Please check your connection", \
		file=sys.stderr)

myOLED.begin()
    #  clear(ALL) will clear out the OLED's graphic memory.
    #  clear(PAGE) will clear the Arduino's display buffer.
myOLED.clear(myOLED.ALL)  #  Clear the display's memory (gets rid of artifacts)
    #  To actually draw anything on the display, you must call the
    #  display() function.

myOLED.display()
time.sleep(1)

CPUTemp = soc_temp()
mySensor.begin()

while True:
	
	myOLED.clear(myOLED.PAGE)

	myOLED.clear(myOLED.PAGE)            # Clear the display
	myOLED.set_cursor(0, 0)        # Set cursor to top-left
	myOLED.set_font_type(0)         # Smallest font
	myOLED.print("T ")          # Print "A0"
	myOLED.set_font_type(1)         # 7-segment font
	myOLED.print("%.1f" % mySensor.temperature_celsius)

	myOLED.set_cursor(0, 16)       # Set cursor to top-middle-left
	myOLED.set_font_type(0)         # Repeat
	myOLED.print("H ")
	myOLED.set_font_type(1)
	myOLED.print("%.2d" % mySensor.humidity)
	
	myOLED.set_cursor(0, 32)
	myOLED.set_font_type(0)
	myOLED.print("C ")
	myOLED.set_font_type(1)
	myOLED.print(soc_temp())

	myOLED.display()
	time.sleep(.1)
