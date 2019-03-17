def distance(strand_a, strand_b):
    count = 0
    if(len(strand_a) != len(strand_b)):
        raise ValueError("Hamming strings must be of the same size")
    else:
        for i in range(len(strand_a)):
            count += (0 if strand_a[i] == strand_b[i] else 1)
    return count
