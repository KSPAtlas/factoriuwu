from uwuipy import uwuipy
import sys
from pathlib import Path

uwu = uwuipy()

try:
    with open(sys.argv[1],'r') as inputfile:
        inputlines = inputfile.readlines()
except:
    raise Exception("Exception occured while trying to open input file")    

if Path(sys.argv[2]).exists():
    raise Exception("Output file already exists")

try:
    with open(sys.argv[2],'w') as outputfile:
        for line in inputlines:
            if '=' in line:
                splitlist = line.split('=', 1)
                splitlist[1] = uwu.uwuify(splitlist[1]).replace('\n', '')
                print(splitlist)
                outputfile.write(f"{splitlist[0]}={splitlist[1]}\n")
            else:
                outputfile.write(line)
except:
    raise Exception("Exception while attempting to uwuify file")
