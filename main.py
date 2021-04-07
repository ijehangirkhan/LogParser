import re

file = open('sample.log', 'r')
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip()
    # print(line)
    error = re.search(r'(.*)ERR$', line)
    if error is not None:
        error_result = error.group(0).split()[:4]
        print(error_result)
        print(error.group(0))

for line in lines:
    line = line.strip()
    # print(line)
    off = re.search(r'(.*)State: OFF', line)
    if off is not None:
        off_result = off.group(0).split()[:4]
        time = off_result[3]
        seconds = time.split(':')[1]
        print(seconds)
        print(off_result)
        print(off.group(0))

for line in lines:
    line = line.strip()
    # print(line)
    on = re.search(r'(.*)State: ON', line)
    if on is not None:
        on_result = on.group(0).split()[:4]
        print(on_result)
        print(on.group(0))