import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

optocoupler1 = 17                                             # Descriptive Variable for pin 17
optocoupler2 = 22
optocoupler3 = 23
optocoupler4 = 24
optocoupler5 = 27
optocouplerImaNqma = 16

GPIO.setup(optocoupler1, GPIO.IN, GPIO.PUD_UP)                # Set optocoupler as input and Activate pull up resistor
GPIO.setup(optocoupler2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(optocoupler3, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(optocoupler4, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(optocoupler5, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(optocouplerImaNqma, GPIO.IN, GPIO.PUD_UP)

a = 0
b = 0
c = 0
d = 0
e = 0
x = 0


while True:  # Create an infinite loop
    optocoupler1_state = GPIO.input(optocoupler1)               # Make it input
    optocoupler2_state = GPIO.input(optocoupler2)
    optocoupler3_state = GPIO.input(optocoupler3)
    optocoupler4_state = GPIO.input(optocoupler4)
    optocoupler5_state = GPIO.input(optocoupler5)
    optocouplerImaNqma_state = GPIO.input(optocouplerImaNqma)

    if optocoupler1_state == 0:                                 # When there is elecricity then write
        f = open("1.txt", "a")                                  # Open an external file
        time.sleep(.1)  # delay
        print("Optocoupler1 reached")                           # Print in terminal
        a = a + 1
        f.write(str(a))                                         # Write a number of an impulse
        f.write(" - Optocoupler1 reached 336v \r\n\n")          # Write in external file
        f.close()                                               # Close the external file
        
    if optocoupler2_state == 0:
        f = open("2.txt", "a")
        time.sleep(.1)
        print("Optocoupler2 reached")
        b = b + 1
        f.write(str(b))
        f.write(" - Optocoupler2 reached 392v \r\n\n")
        f.close()
        
    if optocoupler3_state == 0:
        f = open("3.txt", "a")
        time.sleep(.1)
        print("Optocoupler3 reached")
        c = c + 1
        f.write(str(c))
        f.write(" - Optocoupler3 reached 448v \r\n\n")
        f.close()
        
    if optocoupler4_state == 0:
        f = open("4.txt", "a")
        time.sleep(.1)
        print("Optocoupler4 reached")
        d = d + 1
        f.write(str(d))
        f.write(" - Optocoupler4 reached 504v \r\n\n")
        f.close()
        
    if optocoupler5_state == 0:
        f = open("5.txt", "a")
        time.sleep(.1)
        print("Optocoupler5 reached")
        e = e + 1
        f.write(str(e))
        f.write(" - Optocoupler5 reached 560v \r\n\n")
        f.close()
        
    if optocouplerImaNqma_state == 1:                           # When there is no  electricity then write
        f = open("ImaNqma.txt", "a")
        time.sleep(.1)
        print("OptocouplerImaNqma reached")
        x = x + 1
        f.write(str(x))
        f.write(" - There's no electricity \r\n\n")
        f.close()

