# NC_Control

A Python web application to control presets on the Neural DSP Nano Cortex via MIDI.

> NOTE: This is a work in progress with known rough edges.

## Prerequisites
- Neural DSP Nano Cortex
- Python with pip
- USB-C cable

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/bwanab/nc_control.git
   cd nc_control
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure presets:
   - Set up your presets on the Nano Cortex
   - Update `preset_map.csv` with your presets
   - Configure preset banks in `preset_banks.csv`

## Configuration Files

### preset_map.csv
Format: `<preset_name>,<preset_number>`
- `preset_name`: Should match the name on your Nano Cortex
- `preset_number`: The numerical position of the preset on the Nano Cortex (must be counted manually)

### preset_banks.csv
Format: `<bank_name>,<preset_1>,<preset_2>,...,<preset_n>`
Example:
```csv
Clean,Indy 2 1 Clean,Indy 2 1 Chorus,Indy 2 1 Delay
```

## Usage

### Web Interface
1. Connect the Nano Cortex via USB-C
2. Start the application:
   ```bash
   flask run
   ```
3. Open http://127.0.0.1:5000 in your browser

### Python Interactive Control
```python
from control.nc_control import *
connect_to_nano()
select_preset(15)  # Selects preset #15
```

The repository appears to be a useful tool for Neural DSP Nano Cortex users who want to control their presets programmatically or through a web interface.



