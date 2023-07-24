import os

files = [file for file in os.listdir() if os.path.isfile(file)]
files.sort()
print(files)
