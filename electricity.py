import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

optocoupler1 = 17  # Descriptive Variable for pin 16
optocoupler2 = 22
optocoupler3 = 23
optocoupler4 = 24
optocoupler5 = 27
optocouplerImaNqma = 16

GPIO.setup(optocoupler1, GPIO.IN, GPIO.PUD_UP)  # Set optocoupler as input and Activate pull up resistor
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
    optocoupler1_state = GPIO.input(optocoupler1)
    optocoupler2_state = GPIO.input(optocoupler2)
    optocoupler3_state = GPIO.input(optocoupler3)
    optocoupler4_state = GPIO.input(optocoupler4)
    optocoupler5_state = GPIO.input(optocoupler5)
    optocouplerImaNqma_state = GPIO.input(optocouplerImaNqma)

    if optocoupler1_state == 0:
        f = open("/opt/homeautomation/logs/1.txt", "a")
        time.sleep(.001)  # delay
        print("Optocoupler1 reached")
        a = a + 1
        f.write(str(a))
        f.write(' - Optocoupler %s reached 336v at %s.\r\n\n' %(1, datetime.datetime.now()))
        f.close()
        
    if optocoupler2_state == 0:
        f = open("/opt/homeautomation/logs/2.txt", "a")
        time.sleep(.001)
        print("Optocoupler2 reached")
        b = b + 1
        f.write(str(b))
        f.write(' - Optocoupler %s reached 392v at %s.\r\n\n' %(2, datetime.datetime.now()))
        f.close()
        
    if optocoupler3_state == 0:
        f = open("/opt/homeautomation/logs/3.txt", "a")
        time.sleep(.001)
        print("Optocoupler3 reached")
        c = c + 1
        f.write(str(c))
        f.write(' - Optocoupler %s reached 448v at %s.\r\n\n' %(3, datetime.datetime.now()))
        f.close()
        
    if optocoupler4_state == 0:
        f = open("/opt/homeautomation/logs/4.txt", "a")
        time.sleep(.001)
        print("Optocoupler4 reached")
        d = d + 1
        f.write(str(d))
        f.write(' - Optocoupler %s reached 504v at %s.\r\n\n' %(4, datetime.datetime.now()))
        f.close()
        
    if optocoupler5_state == 0:
        f = open("/opt/homeautomation/logs/5.txt", "a")
        time.sleep(.001)
        print("Optocoupler5 reached")
        e = e + 1
        f.write(str(e))
        f.write(' - Optocoupler %s reached 560v at %s.\r\n\n' %(5, datetime.datetime.now()))
        f.close()
        
    if optocouplerImaNqma_state == 1:
        f = open("/opt/homeautomation/logs/6.txt", "a")
        time.sleep(.001)
        print("OptocouplerImaNqma reached")
        x = x + 1
        f.write(str(x))
        f.write(' - Optocoupler%s - There is no electricity at %s.\r\n\n' %(6, datetime.datetime.now()))
        f.close()
