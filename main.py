# Deletes odd lines in the .txt file

arr = []
out = []

way = "F:\\448\\ENRUS.TXT"
with open(way, "r") as file:
    for line in file:
        arr.append(line)

i = 0
while i < (len(arr)):
    if (i % 2) == 0:
        out.append(arr[i])
    i = i + 1

with open("F:\\words.txt", "w") as file:
    file.writelines(out)