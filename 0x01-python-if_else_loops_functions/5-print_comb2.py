#!/usr/bin/python3
output = ""
for num in range(0, 100):
    if num != 100:
        if num < 10:
            output += "0{:d}, ".format(num)
        else:
            output += "{:d}, ".format(num)
        if output == 99:
            output += '\n'
print(output)
