#Python Pillow https://www.youtube.com/watch?v=REMyfaLvkkE
#For maximum reliability, use a fully qualified path for the executable
import os

#gets the original directory
origWD = os.getcwd()

#askes fir directories
userin = input(r"directory>")
folderpath = userin
#changes directory to the file
os.chdir(folderpath)

#makes a list for all files
files = ["lp " + name for name in os.listdir(folderpath)]
print(files)

#prints each file
for name in files:
    os.system(name)




#os.startfile(name, "print") windows only

#subprocess.call(('open', name)) works
#os.open(name, 'print')


