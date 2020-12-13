# Advent of Code Day 12: Rain Risk

infile = open('input.txt', 'r')

ship_movement = []
with infile as f:
    for line in f:
        line = line.rstrip()
        ship_movement.append([line[slice(1)], int(line[slice(1, 5)])])

# print(ship_movement)

ship_position = [0, 0, 'E']
# print(ship_position[2])
# print(ship_movement[1][0])
# print(ship_movement[1][1])
turned = 0

for i in range(0, len(ship_movement)-1):
    if ship_movement[i][0] == 'R':
        # print('turning right')
        if ship_position[2] == 'E':
            # print('facing east')
            # print(ship_movement[i][1])
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'S']
                # print(ship_position)
            if ship_movement[i][1] == 180:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'W']
            if ship_movement[i][1] == 270:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'N']
        if ship_position[2] == 'S':
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'W']
            if ship_movement[i][1] == 180:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'N']
            if ship_movement[i][1] == 270:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'E']
        if ship_position[2] == 'W':
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'N']
            if ship_movement[i][1] == 180:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'E']
            if ship_movement[i][1] == 270:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'S']
        if ship_position[2] == 'N':
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'E']
            if ship_movement[i][1] == 180:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'S']
            if ship_movement[i][1] == 270:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'W']
    if ship_movement[i][0] == 'L':
        if ship_position[2] == 'E':
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'N']
            if ship_movement[i][1] == 180:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'W']
            if ship_movement[i][1] == 270:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'S']
        if ship_position[2] == 'S':
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'E']
            if ship_movement[i][1] == 180:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'N']
            if ship_movement[i][1] == 270:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'W']
        if ship_position[2] == 'W':
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'S']
            if ship_movement[i][1] == 180:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'E']
            if ship_movement[i][1] == 270:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'N']
        if ship_position[2] == 'N':
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'W']
            if ship_movement[i][1] == 180:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'S']
            if ship_movement[i][1] == 270:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'E']
    if ship_movement[i][0] == 'F':
        if ship_position[2] == 'E':
            ship_position = [ship_position[0]+ship_movement[i][1], ship_position[1], ship_position[2]]
        if ship_position[2] == 'W':
            ship_position = [ship_position[0]-ship_movement[i][1], ship_position[1], ship_position[2]]
        if ship_position[2] == 'N':
            ship_position = [ship_position[0], ship_position[1] + ship_movement[i][1], ship_position[2]]
        if ship_position[2] == 'S':
            ship_position = [ship_position[0], ship_position[1] - ship_movement[i][1], ship_position[2]]
    if ship_movement[i][0] == 'N':
        ship_position = [ship_position[0], ship_position[1] + ship_movement[i][1], ship_position[2]]
    if ship_movement[i][0] == 'S':
        ship_position = [ship_position[0], ship_position[1] - ship_movement[i][1], ship_position[2]]
    if ship_movement[i][0] == 'E':
        ship_position = [ship_position[0] + ship_movement[i][1], ship_position[1], ship_position[2]]
    if ship_movement[i][0] == 'W':
        ship_position = [ship_position[0] - ship_movement[i][1], ship_position[1], ship_position[2]]
    turned = 0
    print(ship_position)

print('Final Position:', ship_position)

print('Manhattan Distance:', abs(int(ship_position[0])) + abs(int(ship_position[1])))