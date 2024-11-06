import csv
import rtmidi
import rtmidi.midiutil


midiout = rtmidi.midiutil.open_midioutput("Nano Cortex")

def select_preset(preset):
    global midiout
    pc = [0xC0, preset]
    midiout[0].send_message(pc)


def get_preset_banks(pm_name):
    # return a map of {preset: [pc1, pc2, ...]}
    with open(pm_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return {row[0]: [pc for pc in row[1:]] for row in reader}

def get_preset_map(pm_name):
    # return a map of {preset: [pc1, pc2, ...]}
    with open(pm_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return {row[0]: int(row[1]) for row in reader}
    
