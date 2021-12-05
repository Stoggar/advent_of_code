with open('2021_day3.txt') as f:
    inp = [i for i in f.readlines()]

in_len = len(inp[0].strip().strip('\n'))
num_ones = [0]*in_len
num_zeros = [0]*in_len

for line in inp:
    line = line.strip('\n')
    line = line.strip()
    for bit in range(len(line)):
        if int(line[bit].strip('\n')) == 1:
            num_ones[bit] += 1
        elif int(line[bit].strip('\n')) == 0:
            num_zeros[bit] += 1
        else:
            raise ValueError()

print(num_ones)
print(num_zeros)

gamma = [-1]*in_len
epsilon = [-1]*in_len

for i in range(len(gamma)):
    if num_ones[i] >= num_zeros[i]:
        gamma[i] = 1
        epsilon[i] = 0
    else:
        gamma[i] = 0
        epsilon[i] = 1

print(gamma)
print(epsilon)

k = 0
gamma_int = 0
epsilon_int = 0
for i in range(len(gamma)-1, -1, -1):
    print(k)
    gamma_int += 2**k if gamma[i] == 1 else 0
    epsilon_int += 2**k if epsilon[i] == 1 else 0
    k += 1

print(gamma_int)
print(epsilon_int)

print(gamma_int*epsilon_int)


