#!/usr/bin/env python2

import fingerpi as fp
# from fingerpi import base

# import struct
import time
# import matplotlib.pyplot as plt
import pickle

NOTICE = """\033[93m[!!! README FIRST !!!]\033[0m
This is just a demo! This code was written to generate the `demo.png` file
located in the repository. It is not meant to be used as a standalone and/or
as a diagnostic tool.
If you run it, and receive an error -- most probably you have an environment
setup that is different from the setup of the devs.

\033[92m[IF YOU ARE JUST PLAYING AROUND]\033[0m
If you want a more interactive version of this code, run `./interactive.py`.
You can also play with the `./gui/gui.py`, but it requires Tk and Qt modules.
"""

print NOTICE

def printByteArray(arr):
    return map(hex, list(arr))

f = fp.FingerPi()

print 'Opening connection...'
f.Open(extra_info = True, check_baudrate = True)

print 'Changing baudrate...'
f.ChangeBaudrate(115200)
# f.CmosLed(False)

while True:
    print 'Place the finger on the scanner and press <Enter>'
    _ = raw_input()
    f.CmosLed(True)
    # response = f.IsPressFinger()
    response = f.CaptureFinger()
    if response[0]['ACK']:
        break
    f.CmosLed(False)
    if response[0]['Parameter'] != 'NACK_FINGER_IS_NOT_PRESSED':
        print 'Unknown Error occured', response[0]['Parameter']
        
# print f.UsbInternalCheck()
        
print 'Image captured!'
f.CmosLed(False)

print 'Transmitting image...'
t = time.time()
raw_img = f.GetImage()
tx_time = time.time() - t
# print raw_img[0]['ACK'],
# print raw_img[1]['Checksum']
print 'Time to transmit:', tx_time

print 'Closing connection...'
f.Close()

with open('raw_img.pickle', 'w') as f:
    pickle.dump(raw_img, f)

# f = figure()
# f.imshow()
