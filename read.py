errors = []                       # The list where we will store results.
linenum = 0
substr = "-p".lower()          # Substring to search for.
with open ('/Users/randytran/Desktop/pythonProject/bash_command_data.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.lower().find(substr) != -1:    # if case-insensitive match,
            errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))
for err in errors:
    print(err)