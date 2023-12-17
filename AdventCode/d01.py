# day 1, p1

# open file n read lines
ifile = open("d01.txt", "r")
lines = ifile.readlines()

# for p2
digits = ["zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"] # zero is never used but I want it here :]

def puzzle1():
    sum_res = 0

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
        sum_res = sum_res + int(str(first) + str(last))
    return sum_res

# p2 - updated p1

def puzzle2():
    sum_res = 0

    for line in lines:
        first = ""
        last = ""

        for i, val in enumerate(line):

            # find first
            if len(first) < 1:
                if val.isnumeric():
                    first = str(val)

                elif line[i:(i + len(digits[0]))] == digits[0]:
                    first = "0"
                elif line[i:(i + len(digits[1]))] == digits[1]:
                    first = "1"
                elif line[i:(i + len(digits[2]))] == digits[2]:
                    first = "2"
                elif line[i:(i + len(digits[3]))] == digits[3]:
                    first = "3"
                elif line[i:(i + len(digits[4]))] == digits[4]:
                    first = "4"
                elif line[i:(i + len(digits[5]))] == digits[5]:
                    first = "5"
                elif line[i:(i + len(digits[6]))] == digits[6]:
                    first = "6"
                elif line[i:(i + len(digits[7]))] == digits[7]:
                    first = "7"
                elif line[i:(i + len(digits[8]))] == digits[8]:
                    first = "8"
                elif line[i:(i + len(digits[9]))] == digits[9]:
                    first = "9"
                
            # find last
            else:
                if val.isnumeric():
                    last = str(val)

                elif line[i:(i + len(digits[0]))] == digits[0]:
                    last = "0"
                elif line[i:(i + len(digits[1]))] == digits[1]:
                    last = "1"
                elif line[i:(i + len(digits[2]))] == digits[2]:
                    last = "2"
                elif line[i:(i + len(digits[3]))] == digits[3]:
                    last = "3"
                elif line[i:(i + len(digits[4]))] == digits[4]:
                    last = "4"
                elif line[i:(i + len(digits[5]))] == digits[5]:
                    last = "5"
                elif line[i:(i + len(digits[6]))] == digits[6]:
                    last = "6"
                elif line[i:(i + len(digits[7]))] == digits[7]:
                    last = "7"
                elif line[i:(i + len(digits[8]))] == digits[8]:
                    last = "8"
                elif line[i:(i + len(digits[9]))] == digits[9]:
                    last = "9"

        if not last.isnumeric(): last = first # first is last sometimes
        sum_res += int(str(first) + str(last))
    return sum_res
    
if __name__ == "__main__":
    print(f"Puzzle 1: {puzzle1()}") # 57346 for d01.txt
    print(f"Puzzle 2: {puzzle2()}") # 57345 for d01.txt