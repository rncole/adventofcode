#!/usr/bin/python

# Advent of code 2021 challenge 4

# Methods of win - horizontal vertical, diagonal, reverse diagonal
# Divide file into draw order, then boards by line break.
# First item will be draws, every subsequent a board with index for board.
# For each board, create sub-index for wins: hor1, hor2... hor 5; ver1, ver2... ver5; diag; revdiag
# After boards are grouped and divided by winning paths, loop each board through subindex checks in order of index.
#
# Approach is dictionary-dictionary-list with outer dict being boards, inner dict being win paths,
# and list win path elements.

# Read first line of input file, splitting at new line and output to list to maintain order
file = open('input', 'r')
with file as f:
    draws = f.readline().strip()
    draws = draws.split(',')
    i = 0
    while i < len(draws):
        draws[i] = int(draws[i])
        i += 1

print(draws)

# Read subsequent lines to EOF, splitting boards into dict with board number as key
file = open('input', 'r')
board_id = 0
boards = {}
board = []
i = 0

with file as f:
    for i in range(2):
        next(f)
    for line in f:
        # Determine if line is blank for a break to next board, and if so reset board list and increment board ID.
        if line == "\n":
            boards[board_id] = board
            board = []
            board_id += 1
        # Continue processing line if not a break.
        else:
            line = line.strip()
            line = line.split()
            j = 0
            # Process line entries to convert to integers
            while j < len(line):
                line[j] = int(line[j])
                j += 1
            board.append(line)


# Read each board by key, splitting boards into win paths dict with win path name as key and element being list of
#  numbers in that path.  Will need to be able to read row and column of board

# Check rows for horizontal win.  Start with increment to know current position in draw list.  Read first row of first
# board then check each position's number for a winning number from first to draw position.  If no winning number, break
# and continue to next row or board.  If whole row matches, add entry to winners dict with draw position as key and
# board ID, and win type (hor/ver/dia/aid).

# Check Horizontal Win:
draw_id = 0
i = 0
j = 0
k = 0
match_count = 0
winning_boards = {}
match_numbers = []

while draw_id < len(draws):
    for l in range(len(boards)):
        for i in range(5):
            for j in range(5):
                #print("Board: ", l, "Row:", i, boards[l][i])
                for k in range(len(draws)):
                    #print("Checking ", draws[k])
                    if boards[l][i][j] == draws[k]:
                        match_numbers.append(k)
                        #print("match ", boards[l][i][j], draws[k])
                        #print(boards[l][i], match_numbers)
                        #print("Draw:", draws[k], max(match_numbers))
                if len(match_numbers) == 5:
                    #print(match_numbers)
                    #print(k, "match: ", draws[k], "board: ", boards[l][i])
                    # Add winning board to list with board ID, winning board sequence, winning type
                    winning_boards[max(match_numbers)] = [l, boards[l][i], "hor"]
                    #print(winning_boards)
            match_numbers = []
            draw_id += 1

# Check Vertical Win:
draw_id = 0
i = 0
j = 0
k = 0
match_count = 0
match_numbers = []
column = []

while draw_id < len(draws):
    for l in range(len(boards)):
        for i in range(5):
            for j in range(5):
                for k in range(len(draws)):
                    #print("Checking ", draws[k])
                    if boards[l][j][i] == draws[k]:
                        match_numbers.append(k)
                        #print("match ", boards[l][i][j], draws[k])
                        #print(boards[l][i], match_numbers)
                        #print("Draw:", draws[k], max(match_numbers))
                        column.append(boards[l][j][i])
                if len(match_numbers) == 5:
                    #print(column)
                    #print(boards[l])
                    #print(match_numbers)
                    #print(k, "match: ", draws[k], "board: ", boards[l][i])
                    # Add winning board to list with board ID, winning board sequence, winning type
                    winning_boards[max(match_numbers)] = [l, column, "ver"]
                    column = []
                    #print(winning_boards)
            match_numbers = []
            draw_id += 1


# Determine the first winning board from the list of winning boards:
first_winning_round = min(winning_boards)
first_board_id = winning_boards[first_winning_round]
first_winning_board = boards[first_board_id[0]]
# print("First Winning Board ID", first_board_id[0], ":", first_winning_board, "\n", "Winning Round: ", first_winning_round)
# Sum values of first winning board that are NOT draws up to the first winning round

sum_count = 0
winning_draw_list = []
for sum_count in range(first_winning_round+1):
    winning_draw_list.append(draws[sum_count])

# Calculate the winning Sum and Card Score for the first winning board:
i = 0
j = 0
winning_sum = 0
# print(first_winning_board)
for i in range(5):
    for j in range(5):
        #print("Checking ", first_winning_board[i][j])
        if (first_winning_board[i][j] not in winning_draw_list):
            #print("Not in List, adding ", first_winning_board[i][j])
            winning_sum = winning_sum + int(first_winning_board[i][j])
print("Winning Sum:", winning_sum, "Last Draw:", draws[first_winning_round], "Card Score: ", \
      winning_sum*draws[first_winning_round])




# ========= PART 2 ===========
# Determine the last winning board from the list of winning boards:
print("\n ===== PART 2 =====")
#print("Boards", len(winning_boards))
i = 0
id_num = 0
winning_boards_ids = []
winning_boards_temp = {}
#print(winning_boards[26][0])
for i in sorted(winning_boards):
    # print(winning_boards[i][0])
    print("Board index:", i)
    print(winning_boards[i])
    if winning_boards[i][0] not in winning_boards_ids:
        #print("Board ID:", winning_boards[i][0], "Round:", i)
        print("Adding Board ID:", winning_boards[i])
        winning_boards_temp[i] = winning_boards[i]
        #print(winning_boards_ids)
        winning_boards_ids.append(winning_boards[i][0])

    print("Winning List", winning_boards_ids)
    max_temp = max(winning_boards_temp)
    print("Winning Rounds", max(winning_boards_temp), winning_boards_temp[max_temp])
winning_boards = {}
winning_boards = winning_boards_temp
#print("Boards", len(winning_boards))
#print(winning_boards_ids)
print("last:", max(winning_boards))

last_winning_round = max(winning_boards)
last_board_id = winning_boards[last_winning_round]
last_winning_board = boards[last_board_id[0]]
print("Last Winning Board ID", last_board_id[0], ":", last_winning_board, "\n", "Winning Round: ", last_winning_round)
# Sum values of first winning board that are NOT draws up to the first winning round

sum_count = 0
winning_draw_list = []
for sum_count in range(last_winning_round+1):
    winning_draw_list.append(draws[sum_count])
#print("Draw List:", winning_draw_list)

# Calculate the winning Sum and Card Score for the first winning board:
i = 0
j = 0
losing_sum = 0
print(last_winning_board)
for i in range(5):
    for j in range(5):
        #print(last_winning_board[i][j], "list:", winning_draw_list)
        if last_winning_board[i][j] not in winning_draw_list:
            print("Not in List, adding ", last_winning_board[i][j])
            losing_sum = losing_sum + int(last_winning_board[i][j])
print("Losing Sum:", losing_sum, "Last Draw:", draws[last_winning_round], "Card Score: ", \
      losing_sum*draws[last_winning_round])
print("Draws:", winning_draw_list)
