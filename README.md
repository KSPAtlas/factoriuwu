# factoriuwu
Uwuifies factorio locale files

# Dependencies
Since it's a python script, it depends on Python itself. This script also depends on uwuipy, which can be installed using
`pip install uwuipy`

# Usage
`python uwu.py <input file> <output file>`

# Uwuifing core and base locales

The Factorio locale directories are located at
`<download/steam directory>/data/{core,base}/locale`

1. Copy the `en` directories to new directories with two-letter names, like `uw`.
2. For core, edit the info.json file in the `uw` directory and change English to something else, like UwU.
3. Move the `core.cfg`, `base.cfg` (from the directories) and `uwu.py` (from this repo) files to a working directory.
4. Run the script on both of them, in the format `python uwu.py input.cfg output.cfg`, replacing input.cfg with core/base.cfg and output.cfg with your own output names (make sure not to confuse the files) like uwucore/uwubase.cfg.
5. Move the files back to their respective directories, and rename them back to core/base.cfg
6. If you did this correctly, you should now be able to start factorio, change the language to what you set the name to (like UwU) and enjoy the experience.
