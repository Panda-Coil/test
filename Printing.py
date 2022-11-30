#10min x 3
#20min x 3
#Python Pillow https://www.youtube.com/watch?v=REMyfaLvkkE
#pink

import fpdf
import os
import time
import subprocess

folderpath = r"/Users/kane/Desktop/work/tax/22_gensen_pdf/"
program = r"/System/Applications/Preview.app"

file_paths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
all_files = {}

file = r"/Users/kane/Desktop/work/tax/22_gensen_pdf/June.pdf"

opened_file = subprocess.Popen([program, file])

#for path in file_paths:
