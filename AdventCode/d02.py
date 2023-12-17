import re

# day 2, p1
"""
Determine which games would have been possible 
if the bag had been loaded with only 
12 red cubes, 13 green cubes, and 14 blue cubes. 
What is the sum of the IDs of those games?
"""

# open file and read lines
ifile = open("d02_input.txt", "r")
games = ifile.readlines()

max_red = 12
max_green = 13
max_blue = 14

# returns game ID if game is valid, 0 otherwise
def is_valid_game(game):
    red = 0
    green = 0
    blue = 0
    
    # get game id
    game_id = re.search(r'\d+', game).group(0) # regex searches for 1st number, group(0) returns the number
    #game_id = re.search(r'\d+', game) # returns an obj, e.g: <re.Match object; span=(5, 6), match='1'>
    
    # get substr after the :
    game = game.split(": ")[1]

    # split str into 'num color' substrs
    records = re.split(', |; ', game)

    for record in records:
        # remove \n (if present)
        record = record.strip()
        # split number and color
        record = re.split(" ", record)
        if record[1] == 'red' and int(record[0]) > red:
            red = int(record[0])
        elif record[1] == 'green' and int(record[0]) > green:
            green = int(record[0])
        elif record[1] == 'blue' and int(record[0]) > blue:
            blue = int(record[0])
    if red > max_red or green > max_green or blue > max_blue:
        return 0
    else:
        return int(game_id)

def sum_valid_games(game_records):
    id_sum = 0
    for game in game_records:
        id_sum += is_valid_game(game)
    return id_sum

if __name__ == "__main__":
    print(sum_valid_games(games))
