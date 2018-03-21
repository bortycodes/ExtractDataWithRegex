import re

#file = open("regex_sum_42.txt","r")
file = open("regex_sum_85467.txt","r")

regex = "[0-9]+"
sum = 0

for match in re.findall(regex, file.read()):
    sum = sum + int(match)

print(sum)

