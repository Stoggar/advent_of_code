with open('2021_day3.txt') as f:
    lines = [i.strip().strip('\n') for i in f.readlines() if not i.strip().strip('\n') == '']

def most_common_begin(lines):
    """return most common bit at position <bit>"""
    num_ones = 0
    num_zeros = 0
    for line in lines:
        if line[0] == '1':
            num_ones += 1
        elif line[0] == '0':
            num_zeros += 1
        else:
            raise ValueError()
    if num_ones >= num_zeros: 
        return '1'
    else: 
        return '0'

def most_rare_begin(lines):
    """return most common bit at position <bit>"""
    num_ones = 0
    num_zeros = 0
    for line in lines:
        if line[0] == '1':
            num_ones += 1
        elif line[0] == '0':
            num_zeros += 1
        else:
            raise ValueError()
    if num_ones < num_zeros: 
        return '1'
    else: 
        return '0'


def keep_rare(lines, i=0):
    if len(lines) == 1:
        return ''.join(lines)
    most_rare = most_rare_begin(lines)
    rest = [line[1:] for line in lines if line[0] == most_rare]
    return most_rare + keep_rare(rest, i+1)


def keep_common(lines, i=0):
    if len(lines) == 1:
        return ''.join(lines)
    most_common = most_common_begin(lines)
    rest = [line[1:] for line in lines if line[0] == most_common]
    return most_common + keep_common(rest, i+1)


def bits_to_int(bits):
    num = 0
    k = 0
    for i in range(len(bits)-1, -1, -1):
        num += 2**k if bits[i] == '1' else 0
        k += 1
    return num

def invert_bits(bits):
    inverted = ''
    for i in bits:
        inverted += '1' if i == '0' else '0'
    return inverted

print(keep_common(lines))
print(keep_rare(lines))

ox_rating = bits_to_int(keep_common(lines))
co2_rating = bits_to_int(keep_rare(lines))
print(ox_rating*co2_rating)


#gamma = [-1]*in_len
#epsilon = [-1]*in_len
#
#for i in range(len(gamma)):
#    if num_ones[i] >= num_zeros[i]:
#        gamma[i] = 1
#        epsilon[i] = 0
#    else:
#        gamma[i] = 0
#        epsilon[i] = 1
#
#print(gamma)
#print(epsilon)
#
#k = 0
#gamma_int = 0
#epsilon_int = 0
#for i in range(len(gamma)-1, -1, -1):
#    print(k)
#    gamma_int += 2**k if gamma[i] == 1 else 0
#    epsilon_int += 2**k if epsilon[i] == 1 else 0
#    k += 1
#
#print(gamma_int)
#print(epsilon_int)
#
#print(gamma_int*epsilon_int)
#
#
#
