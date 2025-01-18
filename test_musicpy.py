from musicpy import *

def basic_blues_bass_line(root):
    blues_bass = [0, 4, 7, 9, 10, 9, 7, 4]
    c1 = chord([N(root) + x for x in blues_bass]) % (1/4, 1/4)
    c4 = chord([N(root) + (x + 5) for x in blues_bass]) % (1/4, 1/4)
    c5 = chord([N(root) + (x + 7) for x in blues_bass]) % (1/4, 1/4)

    blues_bass_chord = c1 + c4 + c1 + c1 + c4 + c4 + c1 + c1 + c5 + c4 + c1 + c1

    return blues_bass_chord

def basic_blues_drums():
    l = 'K;PH,i:1/8,K;S;OH,i:1/8'
    return drum(l) * (4 * 12)

bass_track = track(basic_blues_bass_line('C2'), instrument='Electric Bass (finger)', track_name='bass')
drum_track = track(basic_blues_drums().notes, instrument='Synth Drum', channel=9, track_name='drums')
np = build([bass_track, 
            drum_track
            ],
           bpm=150)

play(np, wait=True)
