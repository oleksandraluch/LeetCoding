# Day 3

# Returns sum of the numbers in line that whose indexes are in adjacent_indexes
# number is considered to be adjacent even if one digit has adjacent index
def sum_adjacent_numbers(line, adjacent_indexes):
    total_sum = 0
    reading_num = False
    is_adjacent = False
    curr_num = ""

    for index, symbol in enumerate(line):
        if symbol.isnumeric() and not reading_num:
            curr_num = symbol
            reading_num = True
            if index in adjacent_indexes: is_adjacent = True
        elif symbol.isnumeric() and reading_num:
            curr_num += symbol
            if index in adjacent_indexes: is_adjacent = True
        elif not symbol.isnumeric():
            if curr_num != "" and is_adjacent: 
                total_sum += int(curr_num)
            reading_num = False
            is_adjacent = False
    return total_sum
        
# Returns indexes where adjacent numbers can appear in the previous or next line
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
    return adj_indexes

# Puzzle 1 solution
def sum_all_adjacent_numbers(filename="d03_input.txt"):

    ifile = open(filename, "r")
    lines = ifile.readlines()
    sum_adjacent = 0

    for index, line in enumerate(lines):
        # Find indexes that might store adjacent numbers
        adjacent_indexes = [] # gonna be unsorted, duplicates possible
        # get indexes from the prev line
        if index > 0:
            adjacent_indexes.extend(get_adjacent_indexes(lines[index - 1]))
        # get indexes from the line
        adjacent_indexes.extend(get_adjacent_indexes(line))
        # get indexes from the next line
        if index < len(lines) - 2:
            adjacent_indexes.extend(get_adjacent_indexes(lines[index + 1]))

        # if want to remove duplicates and sort:
        # adjacent_indexes = list(dict.fromkeys(adjacent_indexes))
        # adjacent_indexes.sort()
            
        sum_adjacent += sum_adjacent_numbers(line, adjacent_indexes)
    ifile.close()
    return sum_adjacent

if __name__ == "__main__":
    print(f"Puzzle 1: {sum_all_adjacent_numbers('d03_input.txt')}")