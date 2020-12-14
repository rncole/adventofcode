# Advent of Code Day 13: Shuttle Search
from sympy.ntheory.modular import solve_congruence
infile = open('input.txt','r')

input = []
with infile as f:
    for line in f:
        line = line.rstrip()
        input.append(line)

t_initial = int(input[0])
t = t_initial
bus_routes_tmp = input[1]
bus_routes = list()
while len(bus_routes_tmp)>0:
    bus_routes.append(bus_routes_tmp.partition(',')[0])
    bus_routes_tmp = bus_routes_tmp.partition(',')[2]

print('time =',t)
print('Bus Routes = ',bus_routes)
# print(len(bus_routes))
earliest_route = ''

i = 0
t = t_initial
# print(len(bus_routes))
while earliest_route == '':
    for i in range(0, len(bus_routes)):
        if bus_routes[i] != 'x':
            test_div = divmod(t, int(bus_routes[i]))[1]
            if test_div == 0:
                earliest_route = bus_routes[i]
                earliest_time = t
        i = i + 1
    t = t + 1
wait_time = earliest_time-t_initial
print('Earliest Route is:',earliest_route,'at time',earliest_time)
print('Waiting time:',wait_time)
print('Solution:',wait_time*int(earliest_route))

route_sequence_correct = 0
bus_routes_w_pos = []
for i in range(0, len(bus_routes)):
    if bus_routes[i] != 'x':
        bus_routes_w_pos.append((-1*i,int(bus_routes[i])))
    i = i+1

# Using sympy Number Theory package (https://docs.sympy.org/latest/modules/ntheory.html):
print('Part 2 Solution:', solve_congruence(*bus_routes_w_pos)[0])

