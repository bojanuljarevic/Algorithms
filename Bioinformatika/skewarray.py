# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    Skew = [0] * (len(Genome) + 1)
    for i in range(len(Genome)+1):
        if Genome[i-1] == 'G':
            Skew[i] = Skew[i-1] + 1
        elif Genome[i-1] == 'C':
            Skew[i] = Skew[i-1] - 1
        else:
            Skew[i] = Skew[i-1]
    return Skew


# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    Skew = SkewArray(Genome)
    minVal = min(Skew)
    for i in range(len(Skew)):
        if minVal == Skew[i]:
            positions.append(i)
    return positions


def MaximumSkew(Genome):
    positions = [] # output variable
    Skew = SkewArray(Genome)
    minVal = max(Skew)
    for i in range(len(Skew)):
        if minVal == Skew[i]:
            positions.append(i)
    return positions

print(MinimumSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA"))