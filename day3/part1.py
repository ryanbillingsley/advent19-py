import re
import functools
import matplotlib.pyplot as plt

# test_input = ('R8,U5,L5,D3\n'
#     'U7,R6,D4,L4')

test_input = ('R75,D30,R83,U83,L12,D49,R71,U7,L72\n'
    'U62,R66,U55,R34,D71,R55,D58,R83')

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def move(start_pos, end_pos, points):
    move_x = 0
    if start_pos[0] < end_pos[0]:
        move_x = 1
    elif start_pos[0] > end_pos[0]:
        move_x = -1
    if move_x != 0:
        for i in range(start_pos[0] + move_x, end_pos[0], move_x):
            points.add((i, start_pos[1]))

    move_y = 0
    if start_pos[1] < end_pos[1]:
        move_y = 1
    elif start_pos[1] > end_pos[1]:
        move_y = -1
    if move_y != 0:
        for i in range(start_pos[1] + move_y, end_pos[1], move_y):
            points.add((start_pos[0], i))

    return points

def run_wire(instructions, start_pos = (0, 0)):
    points = set()

    for instr in instructions:
        match = re.match("([RLUD])(\d*)", instr)
        command = match.group(1)
        distance = int(match.group(2))
        if command == 'R':
            end_pos = (start_pos[0] + distance, start_pos[1])
            move(start_pos, end_pos, points)
        elif command == 'L':
            end_pos = (start_pos[0] - distance, start_pos[1])
            move(start_pos, end_pos, points)
        elif command == 'U':
            end_pos = (start_pos[0], start_pos[1] + distance)
            move(start_pos, end_pos, points)
        elif command == 'D':
            end_pos = (start_pos[0], start_pos[1] - distance)
            move(start_pos, end_pos, points)

        start_pos = end_pos

    return points

def intersections(wire):
    instructions = wire.split(',')
    return run_wire(instructions)


# wires = test_input.split('\n')
# points = list(map(intersections, wires))

# plt.scatter(*(zip(*set.union(points[0], points[1]))))
# plt.show()

with open('day3.txt', 'r') as content_file:
    wires = content_file.readlines()

points = list(map(intersections, wires))

common = set.intersection(points[0], points[1])
print(common)
distances = map(lambda test_point: manhattan_distance((0, 0), test_point), common)

print(min(list(distances)))
