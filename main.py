#!/usr/bin/python
import os
import re
import matplotlib.pyplot as plt
import threading as thr
import serial as srl
import time
import struct
import ui as ui
import binascii
import serial.tools.list_ports
from datetime import datetime
import json

ArduinoPort = ""
ArduinoSerial = None

def InitSerial():
    global ArduinoSerial
    global ArduinoPort

    print("Looking for Arduino...")
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p[1]:
            print("Device " + p[1] + " has been found on port " + p[0] + "\n")
            ArduinoPort = p[0]

    if ArduinoPort == "" :
        print("No Arduino device found" + "\n")
        return False

    print("Opening serial communication with Arduino...")
    ArduinoSerial = srl.Serial(ArduinoPort,
                     baudrate=115200,
                     bytesize=srl.EIGHTBITS,
                     parity=srl.PARITY_NONE,
                     stopbits=srl.STOPBITS_ONE,
                     timeout=0,
                     xonxoff=0,
                     rtscts=0)

    print(ArduinoSerial)
    print("")
    return ArduinoSerial.isOpen()

def ListenOnPort(registry_name):

    # dummy read to flush the port
    ArduinoSerial.readline()

    with ArduinoSerial:
        while True :
            data=ArduinoSerial.readline() # Data is of type byte hexadecimal b'\x02'
            if str(data) != "b''" :
                # b'41745.00\r\n' to 41745
                data = str(data).replace("'","").replace(".00","").replace("\\r\\n","").replace("b","")
                if len(data) == 7 :
                    print("Writting " + data + " on registry...")
                    with open(registry_name, "a") as file :
                        file.write(data +","+datetime.today().strftime("%d/%m/%y,%H:%M:%S %p")+"\n")


def Start():
    # Open file bdd_retard.csv to add new entry
    registry_name = "registry_"+datetime.today().strftime("%d-%m-%y_%H-%M-%p")+".csv"

    # Open settings
    with open('config.json') as f:
        config = json.load(f)

    # Connect on port
    if(InitSerial()==True):
        # Listen on Port and write to file in asynchrone mode
        listening = thr.Thread(target=ListenOnPort, args=[registry_name])
        listening.start()
        # Start UI
        print("Thread ListenOnPort correctly launched. Starting user interface... ")
        ui.Start(registry_name, config)

    # Stop everything when UI is gone
    print("Closing serial port...")
    ArduinoSerial.close()
    print("Ready to quit")

Start()
