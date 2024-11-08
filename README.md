# NC_Control

This python web app connects to the Nano Cortex and allows setting the current preset. 

Presets must be:
   1. set up on the Nano Cortex
   2. described in preset_map.csv.
   3. preset banks should be set up in preset_banks.csv

A preset map row is in the form: <preset_name><preset_number> where the name can be whatever in principle, but probably should match the name given on the Nano Cortex. The preset_number must be the correct number on the Nano Cortex. Note that the only way I see to get that number is to count them.

A preset bank row is in the form: <bank_name><preset 1><preset 2><preset n> where the limit to the number of presets in a bank is arbitrary in principle, but practically limited by display real estate. An example from my setup is: Clean,Indy 2 1 Clean,Indy 2 1 Chorus,Indy 2 1 Delay.

To use:
    1. clone this directory.
    2. cd into the directory
    3. pip install -r requirements.txt
    4. connect the Nano Cortex via the USB C cable to your computer.
    5. flash run
    6. open browser to http://127.0.0.1:5000
   
You can also control the presets of the Nano Cortex interactively in python.

First, be sure to connect the Nano Cortex via the USB C cable.
python
--> from control/nc_control import *
--> connect_to_nano()
--> select_preset(15)  # selects the 15th preset as given on the Nano Cortex. This is how one can verify that the preset numbers are correct.



