import csv
import rtmidi
import rtmidi.midiutil

def connect_to_nano():
    try:
        midiout = rtmidi.midiutil.open_midioutput("Nano Cortex")
    except:
        print("Error opening Nano Cortex MIDI output")

def select_preset(preset):
    global midiout
    pc = [0xC0, preset]
    try:    
        midiout[0].send_message(pc)
    except:
        print(f"Error sending preset message: {pc}")


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
    
if __name__ == '__main__':
    connect_to_nano()
