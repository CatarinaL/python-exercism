def distance(strand_a, strand_b):
    """
    count = 0
    """
    if(len(strand_a) != len(strand_b)):
        raise ValueError("Hamming strands must be of the same size")
    #for i in range(len(strand_a)):
    #    count += (0 if strand_a[i] == strand_b[i] else 1)
    """
    for i, j in zip(strand_a, strand_b):
        count += 0 if i == j else 1
    return count
    """
    return sum([1 for i, j in zip(strand_a, strand_b) if i != j])
