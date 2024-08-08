import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
commands = data[1]

next_p = [-1] * n
last_non_f = n

for i in range(n - 1, -1, -1):
    next_p[i] = last_non_f
    if commands[i] != 'F':
        last_non_f = i

possible_p = set()
p = 0
direction = 1

for command in commands:
    if command == 'F':
        p += direction
    elif command == 'R':
        direction = 1
    elif command == 'L':
        direction = -1

direction = 1

for i in range(n):
    if commands[i] == 'F':
        count_F = next_p[i] - i - 1
        if direction == -1:
            possible_p.add(p + 2 * count_F + 1)
        else:
            possible_p.add(p - 1)
        if direction == 1:
            possible_p.add(p - 2 * count_F - 1)
        else:
            possible_p.add(p + 1)
    elif commands[i] == 'R':
        count_F = next_p[i] - i - 1
        if direction == 1:
            possible_p.add(p + 1)
        else:
            possible_p.add(p - 2 * count_F - 1)
        possible_p.add(p - 2 * count_F)
        direction = 1
    elif commands[i] == 'L':
        count_F = next_p[i] - i - 1
        if direction == -1:
            possible_p.add(p - 1)
        else:
            possible_p.add(p + 2 * count_F + 1)
        possible_p.add(p + 2 * count_F)
        direction = -1

print(len(possible_p))
