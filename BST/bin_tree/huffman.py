# Bojan Uljarević RA15-2017        23.4.2020.

class Node:

    def __init__(self, p = None, l = None, r = None, d = None):
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

    def printNode(self):
        print(self.data.value, self.data.freq)

class Data:

    def __init__(self, val1, val2):
        self.value = val1
        self.freq = val2



def GetHistogram(string):
    characters = {}
    for c in string:
        characters[c] = 0
    for c in string:
        characters[c] += 1
    L = []
    for k in characters:
        L.append(Node(None, None, None, Data(k, characters[k])))
    return L

def GetMinFreqElem(dataList):
    minFreqElem = dataList[0]
    for i in dataList:
        if i.data.freq < minFreqElem.data.freq:
            minFreqElem = i
    return minFreqElem

def RemoveElem(dataList, val):
    freq = 0
    for i in dataList:
        if i.data.value == val:
            freq = i.data.freq
            dataList.remove(i)
            return i
    return None

def PutElem(dataList, node):
    dataList.append(node)

def BuildHuffTree(L):
    while len(L) > 1:
        minEl1 = RemoveElem(L, GetMinFreqElem(L).data.value)
        minEl2 = RemoveElem(L, GetMinFreqElem(L).data.value)
        newNode = Node(None, minEl1, minEl2, Data(minEl1.data.value + minEl2.data.value, minEl1.data.freq + minEl2.data.freq))
        minEl1.parent = newNode
        minEl2.parent = newNode
        PutElem(L, newNode)
    return newNode

def HuffmanCode(node, val):
    if node != None:
        if node.left != None:
            HuffmanCode(node.left, val)
        if node.right != None:
            HuffmanCode(node.right, val)
        if node.right == None and node.left == None:
            if node.data.value == val:
                huff = ""
                while node.parent != None:
                    if node.parent.left == node:
                        huff += '0'
                    else:
                        huff += '1'
                    node = node.parent
                print(huff[::-1])

if __name__ == "__main__":


    # zadatak 1
    input1 = ['a', 'b']
    L = GetHistogram(input1)

    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    L = GetHistogram(input2)

    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    L = GetHistogram(input3)

    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    L = GetHistogram(input4)

    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
    L = GetHistogram(input5)

    # zadatak 2

    root = BuildHuffTree(L)
    root.printNode()

    # zadatak 3

    HuffmanCode(root, 'a')
    HuffmanCode(root, 'b')
    HuffmanCode(root, 'c')
    HuffmanCode(root, 'd')
    HuffmanCode(root, 'e')
    HuffmanCode(root, 'f')
    HuffmanCode(root, 'g')






