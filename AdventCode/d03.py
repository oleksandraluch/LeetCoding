# Day 3, p1

symbols = "!@#$%^&*()_-+={}[]/"

def read_adjacent_numbers(line, adjacent_indexes):
    for symbol in line:
        pass

def get_adjacent_indexes(line):
    adj_indexes = []
    for index, val in enumerate(line):
        if val in symbols:
            adj_indexes.append(index)
    return adj_indexes

if __name__ == "__main__":

    ifile = open("d03_smoke.txt", "r")
    lines = ifile.readlines()

    for line in lines:
        print(get_adjacent_indexes(line))

    