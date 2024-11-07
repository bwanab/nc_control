from flask import Flask, request, session, render_template
from flask_bootstrap import Bootstrap
from .control.nc_control import *
import os

print(os.getcwd())

app = Flask(__name__)

bootstrap = Bootstrap(app)

banks = get_preset_banks("preset_banks.csv")
presets = get_preset_map("preset_map.csv")
current_bank = list(banks.keys())[0]
current_preset = banks[current_bank][0]
last_preset_per_bank = {}

@app.route('/')
def index():
    global banks, presets, current_bank, current_preset
    bank_presets = banks[current_bank]
    select_preset(presets[current_preset])
    bank_list = list(banks.keys())
    return render_template('presets.html', bank_name=current_bank, bank=bank_presets, bank_list=bank_list, preset=current_preset)
    

@app.route('/set_preset/<preset>/<bank_name>')
def set_preset(preset, bank_name):
    global banks, presets, current_bank, current_preset
    current_preset = preset
    return index()

@app.route('/set_bank/<bank_name>')
def set_bank(bank_name):
    global banks, presets, current_bank, current_preset, last_preset_per_bank
    last_preset_per_bank[current_bank] = current_preset
    current_bank = bank_name
    current_preset = last_preset_per_bank.get(current_bank, banks[current_bank][0])
    return index()


