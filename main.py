import json
with open('manpage-data.json', 'r') as f:
    for line in f:
        cmd_manpage = json.loads(line)
        if cmd_manpage['name'] == 'find':
            print(cmd_manpage['name'])
            print(json.dumps(cmd_manpage, sort_keys=True, indent=4))

print('finish')