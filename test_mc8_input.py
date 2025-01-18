#!/usr/bin/env python
#
# midiin_poll.py
#
"""Show how to receive MIDI input by polling an input port."""

from __future__ import print_function

import logging
import sys
import time

from rtmidi.midiutil import open_midiinput


log = logging.getLogger('midiin_poll')
logging.basicConfig(level=logging.DEBUG)

# Prompts user for MIDI input port, unless a valid port number or name
# is given as the first argument on the command line.
# API backend defaults to ALSA on Linux.
# port = sys.argv[1] if len(sys.argv) > 1 else None
#port = "Morningstar MC8"
port = "mio"

try:
    midiin, port_name = open_midiinput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()

print("Entering main loop. Press Control-C to exit.")
try:
    while True:
        # count down from 4 at 0.5 second interval
        print("Starting in:")
        for i in range(4, -1, -1):
            print(i)
            time.sleep(1.0)
    
        timer = time.time()
        msg = None
        while msg == None:
            msg = midiin.get_message()
        dt = time.time() - timer
        print("[%s] @%0.6f %r" % (port_name, dt, msg))

        time.sleep(0.01)
except KeyboardInterrupt:
    print('')
finally:
    print("Exit.")
    midiin.close_port()
    del midiin