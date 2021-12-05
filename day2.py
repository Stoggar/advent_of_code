x = 0
d = 0 
aim = 0
with open('2021_day2.txt') as f:
#with open('tmp.txt') as f:
    lines = [line.strip().strip('\n') for line in f.readlines()]

for line in lines:
    num = int(line.split()[-1].strip('\n'))
    if line[:7] == 'forward':
        x += num
        d += aim * num
    elif line[:4] == 'down':
        aim += num
    elif line[:2] == 'up':
        aim -= num
    else:
        raise ValueError()

print(x)
print(d)
print(x*d)


