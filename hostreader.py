#!/usr/bin/env python

# Host reader for EMG (current IoT class)
# Current version reads ascii strings
#   TODO: Convert this to byte streams
#   TODO: add optional graphing capabilities
# Run: ./hostreader.py device [seconds]

import serial
import sys
import time
import signal
import os
# import csv

baudrate=115200
readyCommand="" # start signal to arduino
stopCommand="T"  # stop signal to arduino
startCommand="R" # start signal from arduino
timeAllowed=20

running=False
reading=False

def done_now(sig, frame):
    sys.stderr.write("aught CTRL-C\nBe done\n")
    ser.write(stopCommand.encode())
    ser.close()
    f.close()
    sys.exit(0)

# require necessary arguments
if len(sys.argv) < 2:
    print("usage: ./base device [number of seconds to run]");
    sys.exit(1);
# optional value for time limit
if len(sys.argv) > 2:
    timeAllowed = int(sys.argv[2])
    if timeAllowed == 0:
        print('new time limit = unbounded')
    else:
        print('new time limit = {} seconds'.format(timeAllowed))

filename=sys.argv[1]

signal.signal(signal.SIGINT, done_now)

startTime = time.time()

# keep trying to open a serial connection to the port
while True:
    try:
        ser=serial.Serial(filename, baudrate, timeout=2.0)
        break
    except serial.serialutil.SerialException as e:
        sys.stderr.write('Could not open serial port {}\n'.format(filename))
        sys.exit(1)
    except FileNotFoundError as e: 
        sys.stderr.write('Failed to find device, error: {}'.format(e))
        sys.exit(1)

if not ser.isOpen():
    # add an exception catcher
    ser.open()

# create output file
outfile = time.strftime("%m_%d_%Y_%H_%M_%S") + ".csv"
f = open(outfile, 'w+')

try:
    # catch ready signal from arduino
    #while True:
    while True:
        try:
            value = ser.readline().decode("ascii")
        except UnicodeDecodeError as e: # maybe !needed due to "ascii" decode format 
                                        # above but keeping just in case
            sys.stderr.write("Caught {}, trying again...\n".format(e))
            continue
        if readyCommand in value:
            ser.write(startCommand.encode())
            sys.stderr.write("Reading enabled\n")
            sys.stderr.flush()
            break

    ser.write(startCommand.encode())
    print('Writing results to {}'.format(outfile))
    while True: # while running
        if timeAllowed != 0 and (time.time() - startTime > timeAllowed):
            break
        try:
            readValue = ser.readline()
            value = readValue.decode("ascii")
            f.write(value) 
            sys.stdout.write(value)
        except Exception as e:
            print("Found error: {}".format(e))
            break
        except serial.serialutil.SerialException as e:
            sys.stderr.write('Error: {}'.format(e))
            break
except OSError as e: #serial.serialutil.SerialException as e:
    sys.stderr.write("Error: {}".format(e))
    

print("Finishing up")
ser.write(stopCommand.encode())
ser.close()
f.close()
