# blinking program

# incorporate modules 
import machine #module w all microcontroller stuff
import time #modulw w time 

# make the LED object 
#green is GPIO Pin0)
led = machine.Pin(0, machine.Pin.OUT)

# infinite loop
while True:
  led.value(1) #turn on the led
  time.sleep(0.5) #.25 second delay 
  led.value(0) #turn off 
  time.sleep(0.5) #.25 second delay
  


  
  


