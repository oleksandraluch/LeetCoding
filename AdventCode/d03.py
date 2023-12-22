# Day 3
# puzzle 1 - solved
# puzzle 2 - not solved

# p1
# Returns sum of the numbers in line that whose indexes are in adjacent_indexes
# number is considered to be adjacent even if one digit has adjacent index
def sum_adjacent_numbers(line, adjacent_indexes):
    total_sum = 0
    reading_num = False
    adjacent_to = False
    curr_num = ""

    for index, symbol in enumerate(line):
        if symbol.isnumeric() and not reading_num:
            curr_num = symbol
            reading_num = True
            if index in adjacent_indexes: adjacent_to = True
        elif symbol.isnumeric() and reading_num:
            curr_num += symbol
            if index in adjacent_indexes: adjacent_to = True
        elif not symbol.isnumeric():
            if curr_num != "" and adjacent_to: 
                total_sum += int(curr_num)
            reading_num = False
            adjacent_to = False
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

# p2
# Returns the the sum of products of numbers adjacent to * in line
# Indexes of adjacent numbers are keys in arg dictionaries: indexes_prev, indexes_line, indexes_next.
# Adjacent numbers are stored in arg dicts values. Each value is a list and and can store a few adjacent numbers
def multiply_adjacent_numbers(line, indexes_prev, indexes_line, indexes_next):
    sum_of_products = 0

    # Look for * in line
    for index, val in enumerate(line):
        # if * is found
        if val == '*':
            # multiply the adjacent numbers with product
            product = 1
            adjacent_to = 0

            if index in indexes_prev:
                for num in indexes_prev[index]:
                    product = product * int(num)
                    adjacent_to = adjacent_to + 1

            if index in indexes_line:
                for num in indexes_line[index]:
                    product = product * int(num)
                    adjacent_to = adjacent_to + 1
                    
            if index in indexes_next:
                for num in indexes_next[index]:
                    product = product * int(num)
                    adjacent_to = adjacent_to + 1
            
            # check if 2 adjacent numbers were multiplied
            if adjacent_to == 2:
                sum_of_products += product

    return sum_of_products

# todo: remove repetitions
# p2
# Returns a dictionary, where 
# key: index where adjacent symbols can appear in the previous, current or next line
# val: list of numbers adjacent to an index (key)
def get_adjacent_indexes_and_nums(line):
    adj_dict = {}
    reading_num = False
    curr_num = ""

    for index, val in enumerate(line):

        # if val is a num and is a first digit in a number
        if val.isnumeric() and not reading_num:
            reading_num = True
            curr_num = val

            # add a placeholde for current index to dict
            if index in adj_dict: adj_dict[index].append('e') # e for empty
            else: adj_dict[index] = ['e']

            # add 'e' for previous index
            if index > 0:
                if (index - 1) in adj_dict: adj_dict[index - 1].append('e')
                else: adj_dict[index - 1] = ['e']
            
            # add 'e' for next index
            if index < len(line) - 1:
                if (index + 1) in adj_dict: adj_dict[index + 1].append('e')
                else: adj_dict[index + 1] = ['e']

        # if val is a num and isn't the first digit in a number
        elif val.isnumeric() and reading_num:
            curr_num += val

            # REPETITION -> from above if statement
            if index in adj_dict: adj_dict[index].append('e')
            else: adj_dict[index] = ['e']
            if index > 0:
                if (index - 1) in adj_dict: adj_dict[index - 1].append('e')
                else: adj_dict[index - 1] = ['e']
            if index < len(line) - 1:
                if (index + 1) in adj_dict: adj_dict[index + 1].append('e')
                else: adj_dict[index + 1] = ['e']
            # ! REPETITION
                
        # if val isn't numeric
        else:
            # if curr_num exists
            if len(curr_num) > 0:
                # replace all placeholders in adj_dict with curr_num
                for key in adj_dict:
                    for i, elem in enumerate(adj_dict[key]):
                        # if curr_num isn't in adj_dict yet and there is a placeholder
                        if not curr_num in adj_dict[key] and elem == 'e':
                            # replace a placeholder with curr_num
                            adj_dict[key][i] = curr_num 
                        # if curr_num is in adj_dict yet and there is a placeholder
                        elif curr_num in adj_dict[key] and elem == 'e':
                            # remove placeholder
                            adj_dict[key].remove('e')

            reading_num = False
        
        # ensure that number is added to dict if it is the last symbol in line
        if index == len(line) - 1:

            # REPETITION -> from above else statement:
            if len(curr_num) > 0:
                for key in adj_dict:
                    for i, elem in enumerate(adj_dict[key]):
                        if not curr_num in adj_dict[key] and elem == 'e':
                            adj_dict[key][i] = curr_num 
                        elif curr_num in adj_dict[key] and elem == 'e':
                            adj_dict[key].remove('e')
            # ! REPETITION
    return adj_dict


# Puzzle 2 Solution
def sum_gear_ratios(filename="d03_input.txt"):
    
    ifile = open(filename, "r")
    lines = ifile.readlines()
    ifile.close()
    total_sum = 0

    # smoke
    # adj_prev = {}
    # adj_line = {}
    # adj_next = {}
    # adj_prev = get_adjacent_indexes_and_nums(lines[2])
    # adj_line = get_adjacent_indexes_and_nums(lines[3])
    # adj_next = get_adjacent_indexes_and_nums(lines[4])

    # print(f"Adj dicts:\n{adj_prev}\n{adj_line}\n{adj_next}")

    # print(f"line 4: {multiply_adjacent_numbers(lines[3], adj_prev, adj_line, adj_next)}")
    # ! smoke

    for index, line in enumerate(lines):
        adj_prev = {}
        adj_line = {}
        adj_next = {}
        # get adjacent indexes from previous line
        if index > 0:
            adj_prev = get_adjacent_indexes_and_nums(lines[index - 1])
        # get adjacent indexes from the line
        adj_line = get_adjacent_indexes_and_nums(line)
        # get adjacent indexes from the next line
        if index < len(lines) - 1:
            adj_next = get_adjacent_indexes_and_nums(lines[index + 1])
        
        total_sum += multiply_adjacent_numbers(line, adj_prev, adj_line, adj_next)
    return total_sum

if __name__ == "__main__":
    
    print(f"Puzzle 1: {sum_all_adjacent_numbers()}")
    print(f"Puzzle 2: {sum_gear_ratios()}")