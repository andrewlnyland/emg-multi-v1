#!/usr/bin/env python

# Host reader test

import serial
import sys
import time
import signal
import os

running=True
reading=False

def finished(sig, frame):
    global running 
    running = False

def start(sig, frame):
    global reading
    reading = True

def stop(sig, frame):
    global reading
    reading = False

# Write PID to Filename
print("trying")
filename="/tmp/EMGstatus"
#if (os.path.isfile(filename)):
#    sys.stderr.write("error: already running\n")
#    sys.exit(1)
f = open(filename, "w+")
f.write(str(os.getpid()))
f.close()
print("written")

# catch signals
signal.signal(signal.SIGINT, finished)
signal.signal(signal.SIGUSR1, start)
signal.signal(signal.SIGUSR2, stop)

i=0
# Outer loop
while running:
    i=0
# Inner loop
    while reading:
        print("reading {}".format(i))
        i+=1
    signal.pause()

# Done inner loop
# Done outer loop

# Wrapup
sys.stderr.write("caught CTRL-C\nDone\n")
os.remove(filename)
sys.exit(0)
