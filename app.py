from flask import Flask, request, session, render_template
from flask_bootstrap import Bootstrap
from .control.nc_control import *
import os

print(os.getcwd())

app = Flask(__name__)

bootstrap = Bootstrap(app)

bank = get_preset_banks("preset_banks.csv")
presets = get_preset_map("preset_map.csv")
current_bank = list(bank.keys())[0]
current_preset = bank[current_bank][0]

@app.route('/')
def index(bank_name=current_bank, preset=current_preset):
    global bank, presets, current_bank, current_preset
    bank_list = bank[bank_name]
    return render_template('presets.html', bank_name=bank_name, bank=bank_list, preset=preset)
    

@app.route('/set_preset/<preset>/<bank_name>')
def set_preset(preset, bank_name):      
    print(preset, bank_name)
    return index(bank_name=bank_name, preset=preset)



