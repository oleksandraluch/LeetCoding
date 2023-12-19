# Day 3, p1

def read_adjacent_numbers(line, adjacent_indexes):
    for symbol in line:
        pass

# returns indexes where adjacent numbers can appear in the previous or next line
def get_adjacent_indexes(line):
    symbols = "!@#$%^&*()_-+={}[]/"
    adj_indexes = []
    for index, val in enumerate(line):
        # check if val is a symbol
        if val in symbols:
            # add current index
            if not index in adj_indexes: 
                adj_indexes.append(index)
            # add previous index
            if index > 0:
                if not (index-1) in adj_indexes: 
                    adj_indexes.append(index-1)
            # add next index
            if index < len(line) - 1:
                if not (index+1) in adj_indexes: 
                    adj_indexes.append(index+1)
    adj_indexes.sort()
    return adj_indexes

if __name__ == "__main__":

    ifile = open("d03_smoke.txt", "r")
    lines = ifile.readlines()

    for line in lines:
        print(get_adjacent_indexes(line))

    