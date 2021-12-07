
with open('day7.txt', 'r') as f:
    crabs = [int(i) for i in f.read().strip('\n').split(',')]

#crabs = [int(i) for i in '16,1,2,0,4,2,7,1,2,14'.split(',')]

distances = [0 for i in range(max(crabs))]

for i, crab in enumerate(crabs):
    for j, dist in enumerate(distances):
        dist = abs(crab - j)
        distances[j] += ((1+dist)/2)*dist

print(min(distances))












