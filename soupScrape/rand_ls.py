import random
import os

FILENAME = "ls.txt"

options = []
with open(FILENAME, "r") as f:
    search = f.readlines()
for i, line in enumerate(search):
    if "Syntax" in line:
        syntax = search[i+1]
    if "-" in line:
        for c in range(len(line)):
            if line[c] == '-':
                if(line[c+1] != '-'):
                    options.append(line[c+1])
                break
command = syntax
rand = random.randrange(0, len(options), 1)
command = command.replace("[Options]...", "-" + options[rand])
command = command.replace("[File]...", "")
print(command)
os.system(command)