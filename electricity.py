import sys
import os
from signal import signal, SIGINT
import requests
import json
from collections import namedtuple
from datetime import datetime, date, time, timezone
#import pytz
import RPi.GPIO as gpio
from time import sleep
import threading

optc1 = 17  # Descriptive Variable for pin 17
optc2 = 22  # Optc = optocoupler
optc3 = 23
optc4 = 24
optc5 = 27
startedge1 = datetime.now()
startedge2 = datetime.now()
startedge3 = datetime.now()
startedge4 = datetime.now()
startedge5 = datetime.now()
'''deltaedge1 = datetime.now()
deltaedge2 = datetime.now()
deltaedge3 = 0.0
deltaedge4 = 0.0
deltaedge5 = 0.0
'''
printflag = 0
lock_c = threading.Lock()

def increase_counter(channel):
    global startedge, deltaedge, moment
    global lock_c, old_timestamp, time_delay, printflag
    global startedge1, startedge2, startedge3, startedge4, startedge5
    global deltaedge1, deltaedge2, deltaedge3, deltaedge4, deltaedge5
    lock_c.acquire()
    #master_counter += 1.0
    curr_timestamp = datetime.now()
    #delta = curr_timestamp - old_timestamp
    #old_timestamp = curr_timestamp
    #totalmicrosec = delta.total_seconds() * 1000000.0
    #time_delay += totalmicrosec

    if channel == optc1:
        if gpio.input(channel):
            deltaedge1 = curr_timestamp - startedge1
            printflag = 1
            sync_event.set()
        else:
            startedge1 = curr_timestamp

        

    elif channel == optc2:
        if gpio.input(channel):
            deltaedge2 = curr_timestamp - startedge2
        else:
            startedge2 = curr_timestamp
    elif channel == optc3:
        if gpio.input(channel):
            deltaedge3 = curr_timestamp - startedge3
        else:
            startedge3 = curr_timestamp
    elif channel == optc4:
        if gpio.input(channel):
            deltaedge4 = curr_timestamp - startedge4
        else:
            startedge4 = curr_timestamp
    else:
        if gpio.input(channel):
            deltaedge5 = curr_timestamp - startedge5
        else:
            startedge5 = curr_timestamp

    
    lock_c.release()
    #print('abccc')

sync_event = threading.Event()
exit_flag = False

def upload_thread_function():
    global sync_event, exit_flag, printflag

    while True:
        sync_event.wait()
        sync_event.clear()
        '''
        flow_curr_timestamp = datetime.now()
        flow_delta = (flow_curr_timestamp - flow_old_timestamp).total_seconds()
        #print (flow_curr_timestamp, flow_old_timestamp, flow_delta)
        flow_old_timestamp = flow_curr_timestamp

        #upload_data()     #in production must be uncommented
        #print(get_data())  #in production must be commented
        '''
        if printflag == 1:
            print("Optocoupler1 reached 336v", startedge1, deltaedge1)
            print("Optocoupler2 reached 392v", startedge2, deltaedge2)
            print("Optocoupler3 reached 448v", startedge3, deltaedge3)
            print("Optocoupler4 reached 504v", startedge4, deltaedge4)
            print("Optocoupler5 reached 560v", startedge5, deltaedge5)
            printflag = 0

        if exit_flag:
            break;

def exit_handler(signal_recieved, frame):
    exit_flag = True
    sync_event.set()
    print('gracefully finish counter thread - 2, Ctrl - C')


if __name__=='__main__':
    signal(SIGINT, exit_handler)
    gpio.setmode(gpio.BCM)
    gpio.setup(optc1, gpio.IN, gpio.PUD_UP)
    gpio.setup(optc2, gpio.IN, gpio.PUD_UP)
    gpio.setup(optc3, gpio.IN, gpio.PUD_UP)
    gpio.setup(optc4, gpio.IN, gpio.PUD_UP)
    gpio.setup(optc5, gpio.IN, gpio.PUD_UP)

    gpio.add_event_detect(optc1, gpio.BOTH, callback=increase_counter)
    gpio.add_event_detect(optc2, gpio.BOTH, callback=increase_counter)
    gpio.add_event_detect(optc3, gpio.BOTH, callback=increase_counter)
    gpio.add_event_detect(optc4, gpio.BOTH, callback=increase_counter)
    gpio.add_event_detect(optc5, gpio.BOTH, callback=increase_counter)

    th = threading.Thread(target=upload_thread_function)
    th.start()
    print('Counter thread started')

    while True:
        sleep(60)

        #print ("RPM is {0}".format(master_counter - master_counter_old))
        #revcount_old = revcount
        #revcount = 0
        sync_event.set()
        if exit_flag:
            break

    #TODO: join the thread
    exit_flag = True
    sync_event.set()
    th.join()
    print('Gracefully finish the counter thread - 1')
    exit(0)

