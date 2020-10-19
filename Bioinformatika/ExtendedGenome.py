
import urllib.request


# Reproduce the PatternCount function here.
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count



# HISTOGRAM
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        return freq

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words



# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    ReversePattern = ""
    for i in range(len(Pattern)-1, -1, -1):
        ReversePattern += Pattern[i]
    return ReversePattern

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    Complement = ""
    for i in Pattern:
        if i == 'A':
            Complement += 'T'
        elif i == 'T':
            Complement += 'A'
        elif i == 'C':
            Complement += 'G'
        else:
            Complement += 'C'
    return Complement


# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    ReverseComplement = Reverse(Pattern)
    ReverseComplement = Complement(ReverseComplement)
    return ReverseComplement



# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions




# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    ExtendedGenome = Genome + Genome[0:len(Genome)//2]
    for i in range(len(Genome)):
        array[i] = PatternCount(ExtendedGenome[i:i+(len(Genome)//2)], symbol)
    return array


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n // 2]

    array[0] = PatternCount(symbol, Genome[0:n // 2])
    for i in range(1, n):
        array[i] = array[i - 1]
        if ExtendedGenome[i - 1] == symbol:
            array[i] -= 1
        if ExtendedGenome[i + (n // 2) - 1] == symbol:
            array[i] += 1
    return array


if __name__ == "__main__":

    data = urllib.request.urlopen("http://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt").read()
    a = FasterSymbolArray(data, "C")
    print(a)