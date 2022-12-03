#Python Pillow https://www.youtube.com/watch?v=REMyfaLvkkE
#For maximum reliability, use a fully qualified path for the executable

import fpdf
import os
import time
import subprocess
import shlex

#gets the original directory
origWD = os.getcwd()

#directories
folderpath = r"/Users/kane/Desktop/work/tax/22_gensen_pdf/"
program = r"/System/Applications/Preview.app"

#changes directory to the file
os.chdir(folderpath)

#makes a list for all files
files = [name for name in os.listdir(folderpath)]
print(files)
      
#prints each file
for name in files:
    #subprocess.call(('open', name))
    subprocess.call("lp -p", name)
    
    
    #os.startfile(name, "print")
    #os.open(name, 'print')


