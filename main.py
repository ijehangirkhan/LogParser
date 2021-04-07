import re

file = open('sample.log', 'r')
lines = file.readlines()
file.close()

off_time_in_seconds = float()
for line in lines:
    line = line.strip()
    off = re.search(r'(.*)State: OFF', line)
    if off is not None:
        off_result = off.group(0).split()[:4]
        time = off_result[2]
        time = time.split(":")
        for index, value in enumerate(time):
            if index == 0:
                off_time_in_seconds = off_time_in_seconds + (float(value) * 3600)
            elif index == 1:
                off_time_in_seconds = off_time_in_seconds + (float(value) * 60)
            elif index == 2:
                off_time_in_seconds = off_time_in_seconds + float(value)
            elif index == 3:
                off_time_in_seconds = off_time_in_seconds + (float(value) / 1000)
# print(off_time_in_seconds)

on_time_in_seconds = float()
for line in lines:
    line = line.strip()
    on = re.search(r'(.*)State: ON', line)
    if on is not None:
        on_result = on.group(0).split()[:4]
        time = on_result[2]
        time = time.split(":")
        for index, value in enumerate(time):
            if index == 0:
                on_time_in_seconds = on_time_in_seconds + (float(value) * 3600)
            elif index == 1:
                on_time_in_seconds = on_time_in_seconds + (float(value) * 60)
            elif index == 2:
                on_time_in_seconds = on_time_in_seconds + float(value)
            elif index == 3:
                on_time_in_seconds = on_time_in_seconds + (float(value) / 1000)
# print(on_time_in_seconds)
total_time_in_seconds = off_time_in_seconds - on_time_in_seconds
print(f"The system remained ON for {total_time_in_seconds} seconds.")

print("Error timestamps are following:")
for line in lines:
    line = line.strip()
    error = re.search(r'(.*)ERR$', line)
    if error is not None:
        error_result = error.group(0).split()[:4]
        print(*error_result)