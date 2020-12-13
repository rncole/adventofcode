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
i = 0
ship_position = [0, 0, 'E']
waypoint_position = [10, 1]

for i in range(0, len(ship_movement)):
    if ship_movement[i][0] == 'R':
        # print('turning right')
        # print('ship:', ship_position)
        # print('waypoint:', waypoint_position)
        if ship_position[2] == 'E':
            if ship_movement[i][1] == 90:
                waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
                waypoint_position = [(ship_position[0]+waypoint_offset[1]), (ship_position[1]-waypoint_offset[0])]
            if ship_movement[i][1] == 180:
                waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
                waypoint_position = [(ship_position[0] - waypoint_offset[0]), (ship_position[1]-waypoint_offset[1])]
            if ship_movement[i][1] == 270:
                waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
                waypoint_position = [(ship_position[0]-waypoint_offset[1]), (ship_position[1]+waypoint_offset[0])]
            ship_position = [ship_position[0], ship_position[1], 'S']
            turned = 1
        if ship_position[2] == 'W':
            if ship_movement[i][1] == 90:
                waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
                waypoint_position = [(ship_position[0]+waypoint_offset[1]), (ship_position[1]-waypoint_offset[0])]
            if ship_movement[i][1] == 180:
                waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
                waypoint_position = [(ship_position[0] - waypoint_offset[0]), (ship_position[1]-waypoint_offset[1])]
            if ship_movement[i][1] == 270:
                waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
                waypoint_position = [(ship_position[0]-waypoint_offset[1]), (ship_position[1]+waypoint_offset[0])]
            ship_position = [ship_position[0], ship_position[1], 'N']
            turned = 1
        if ship_position[2] == 'N':
            if ship_movement[i][1] == 90:
                waypoint_offset = [waypoint_position[0] - ship_position[0], waypoint_position[1] - ship_position[1]]
                waypoint_position = [(ship_position[0] + waypoint_offset[1]), (ship_position[1] - waypoint_offset[0])]
            if ship_movement[i][1] == 180:
                waypoint_offset = [waypoint_position[0] - ship_position[0], waypoint_position[1] - ship_position[1]]
                waypoint_position = [(ship_position[0] - waypoint_offset[0]), (ship_position[1] - waypoint_offset[1])]
            if ship_movement[i][1] == 270:
                waypoint_offset = [waypoint_position[0] - ship_position[0], waypoint_position[1] - ship_position[1]]
                waypoint_position = [(ship_position[0] - waypoint_offset[1]), (ship_position[1] + waypoint_offset[0])]
            ship_position = [ship_position[0], ship_position[1], 'E']
            turned = 1
        if ship_position[2] == 'S':
            if ship_movement[i][1] == 90:
                waypoint_offset = [waypoint_position[0] - ship_position[0], waypoint_position[1] - ship_position[1]]
                waypoint_position = [(ship_position[0] + waypoint_offset[1]), (ship_position[1] - waypoint_offset[0])]
            if ship_movement[i][1] == 180:
                waypoint_offset = [waypoint_position[0] - ship_position[0], waypoint_position[1] - ship_position[1]]
                waypoint_position = [(ship_position[0] - waypoint_offset[0]), (ship_position[1] - waypoint_offset[1])]
            if ship_movement[i][1] == 270:
                waypoint_offset = [waypoint_position[0] - ship_position[0], waypoint_position[1] - ship_position[1]]
                waypoint_position = [(ship_position[0] - waypoint_offset[1]), (ship_position[1] + waypoint_offset[0])]
            ship_position = [ship_position[0], ship_position[1], 'W']
            turned = 1
        # print('ship:', ship_position)
        # print('waypoint:', waypoint_position)
    if ship_movement[i][0] == 'L':
        # print('ship:', ship_position)
        # print('waypoint:', waypoint_position)
        if ship_movement[i][1] == 90:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0]-waypoint_offset[1]), (ship_position[1]+waypoint_offset[0])]
        if ship_movement[i][1] == 180:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0] - waypoint_offset[0]), (ship_position[1]-waypoint_offset[1])]
        if ship_movement[i][1] == 270:
            waypoint_offset = [waypoint_position[0]-ship_position[0], waypoint_position[1]-ship_position[1]]
            waypoint_position = [(ship_position[0]+waypoint_offset[1]), (ship_position[1]-waypoint_offset[0])]
        # print('ship:', ship_position)
        # print('waypoint:', waypoint_position)
    if ship_movement[i][0] == 'F':
        for x in range(1, ship_movement[i][1]):
            waypoint_offset = [waypoint_position[0] - ship_position[0], waypoint_position[1] - ship_position[1]]
            # print('ship prior:',ship_position)
            # print('offset',waypoint_offset)
            ship_position = [waypoint_position[0], waypoint_position[1], ship_position[2]]
            # print('ship after:',ship_position)
            waypoint_position = [ship_position[0] + waypoint_offset[0], ship_position[1] + waypoint_offset[1]]
            # print('new waypoint',waypoint_position)
    if ship_movement[i][0] == 'N':
        waypoint_position = [waypoint_position[0], waypoint_position[1] + ship_movement[i][1]]
    if ship_movement[i][0] == 'S':
        waypoint_position = [waypoint_position[0], waypoint_position[1] - ship_movement[i][1]]
    if ship_movement[i][0] == 'E':
        waypoint_position = [waypoint_position[0] + ship_movement[i][1], waypoint_position[1]]
    if ship_movement[i][0] == 'W':
        waypoint_position = [waypoint_position[0] - ship_movement[i][1], waypoint_position[1]]
    turned = 0

print('\n')
print('Ship Position:', ship_position)
print('Waypoint Position:', waypoint_position)
print('Manhattan Distance:', abs(int(waypoint_position[0])) + abs(int(waypoint_position[1])))