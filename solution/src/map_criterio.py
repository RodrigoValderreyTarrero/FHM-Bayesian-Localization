import random as rn

def binary_criteria(dims):
    prob = 0.15
    map = [[0 for _ in range(dims[1])] for row in range(dims[0])]
    for n in map:
        for m in range(len(n)):
            rnd = rn.random()
            if rnd <= prob:
                n[m] = 1
    return map

def prob_criteria(dims):
    prob = 1/(dims[0]*dims[1])
    map = [[prob for _ in range(dims[1])] for row in range(dims[0])]
    return map