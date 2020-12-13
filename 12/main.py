# Advent of Code Day 12: Rain Risk

infile = open('input.txt', 'r')

ship_movement = []
with infile as f:
    for line in f:
        line = line.rstrip()
        ship_movement.append([line[slice(1)], int(line[slice(1, 5)])])

ship_position = [0, 0, 'E']
turned = 0

for i in range(0, len(ship_movement)):
    if ship_movement[i][0] == 'R':
        if ship_position[2] == 'E':
            if ship_movement[i][1] == 90:
                if turned == 0:
                    turned = 1
                    ship_position = [ship_position[0], ship_position[1], 'S']
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
            ship_position = [ship_position[0] + ship_movement[i][1], ship_position[1], ship_position[2]]
        if ship_position[2] == 'W':
            ship_position = [ship_position[0] - ship_movement[i][1], ship_position[1], ship_position[2]]
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

print('\nPart 1 Solution:\n=================================')
print('Final Position:', ship_position)
print('Manhattan Distance:', abs(int(ship_position[0])) + abs(int(ship_position[1])))

ship_position = [0, 0, 'E']
waypoint_position = [10, 1]
waypoint_offset = []

for i in range(0, len(ship_movement)):
    if ship_movement[i][0] == 'R':
        if ship_movement[i][1] == 90:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0]+waypoint_offset[1]), (ship_position[1]-waypoint_offset[0])]
        if ship_movement[i][1] == 180:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0] - waypoint_offset[0]), (ship_position[1]-waypoint_offset[1])]
        if ship_movement[i][1] == 270:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0]-waypoint_offset[1]), (ship_position[1]+waypoint_offset[0])]
    if ship_movement[i][0] == 'L':
        if ship_movement[i][1] == 90:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0]-waypoint_offset[1]), (ship_position[1]+waypoint_offset[0])]
        if ship_movement[i][1] == 180:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0] - waypoint_offset[0]), (ship_position[1]-waypoint_offset[1])]
        if ship_movement[i][1] == 270:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0]+waypoint_offset[1]), (ship_position[1]-waypoint_offset[0])]
    if ship_movement[i][0] == 'F':
        for x in range(0, ship_movement[i][1]):
            waypoint_offset = [waypoint_position[0] - ship_position[0], waypoint_position[1] - ship_position[1]]
            ship_position = [waypoint_position[0], waypoint_position[1], ship_position[2]]
            waypoint_position = [ship_position[0] + waypoint_offset[0], ship_position[1] + waypoint_offset[1]]
    if ship_movement[i][0] == 'N':
        waypoint_position = [waypoint_position[0], waypoint_position[1] + ship_movement[i][1]]
    if ship_movement[i][0] == 'S':
        waypoint_position = [waypoint_position[0], waypoint_position[1] - ship_movement[i][1]]
    if ship_movement[i][0] == 'E':
        waypoint_position = [waypoint_position[0] + ship_movement[i][1], waypoint_position[1]]
    if ship_movement[i][0] == 'W':
        waypoint_position = [waypoint_position[0] - ship_movement[i][1], waypoint_position[1]]

print('\nPart 2 Solution:\n=================================')
print('Ship Position:', ship_position)
print('Waypoint Position:', waypoint_position)
print('Manhattan Distance:', abs(ship_position[0]) + abs(ship_position[1]))
