# Day 3

# p1
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

# p1
# Returns indexes where adjacent numbers can appear in the previous or next line
def get_adjacent_indexes(line, symbols="!@#$%^&*()_-+={}[]/"):
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
    ifile.close()
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
    return sum_adjacent

# Returns the product of numbers in line that whose indexes are in adjacent_indexes
# number is considered to be adjacent even if one digit has adjacent index
def multiply_adjacent_numbers(line, adj_indexes):
    pass

# p2
# Returns a dictionary, where 
# keys: are indexes where adjacent symbols can appear in the previous or next line
# vals: list of numbers adjacent to an index
def get_adjacent_indexes_and_nums(line, symbols="0123456789"):
    adj_dict = {}
    reading_num = False
    curr_num = ""

    for index, val in enumerate(line):

        # check if val in a number
        if val in symbols and not reading_num:
            reading_num = True
            curr_num += val
            adj_dict[index] = ["empty"]
            # add prev index
            if index > 0:
                adj_dict[index - 1] = ["empty"]
            # add next index
            if index < len(line) - 2:
                adj_dict[index + 1] = ["empty"]
        elif val in symbols and reading_num:
            curr_num += val
            adj_dict[index] = ["empty"]
            # add prev index
            if index > 0:
                adj_dict[index - 1] = ["empty"]
            # add next index
            if index < len(line) - 2:
                adj_dict[index + 1] = ["empty"]
        else:
            if len(curr_num) > 0:
                for key in adj_dict:
                    if adj_dict[key] == ["empty"]:
                        adj_dict[key] = curr_num
            curr_num = ""
            reading_num = False
        
        # ensure that number is added to dict if it is the last symbol in line
        if index == len(line) - 1:
            if len(curr_num) > 0:
                for key in adj_dict:
                    if adj_dict[key] == ["empty"]:
                        adj_dict[key] = curr_num

    return adj_dict

# Puzzle 2 Solution
def sum_gear_ratios(filename="d03_input.txt"):
    
    ifile = open(filename, "r")
    lines = ifile.readlines()
    ifile.close()
    total_sum = 0

    for index, line in enumerate(lines):
        # get adjacent indexes from
        pass

if __name__ == "__main__":
    print(f"Puzzle 1: {sum_all_adjacent_numbers()}")
    #print(f"Puzzle 2: {sum_gear_ratios('d03_smoke.txt')}")
    sum_gear_ratios('d03_smoke.txt')