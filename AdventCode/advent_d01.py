# d 1, Part 1

ifile = open("d01.txt", "r")
lines = ifile.readlines()
sum = 0

for line in lines:
    first = ""
    last = ""

    first_found = False
    for i in line:
        if i.isnumeric() and not first_found:
            first = i
            first_found = True
        if i.isnumeric() and first_found:
            last = i

    sum = sum + int(str(first) + str(last))

print(sum)
