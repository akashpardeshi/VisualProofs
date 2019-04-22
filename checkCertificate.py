import time

"""
checks a text file that contains
a Pratt Certificate based on the 
VELP conditions
"""

def getBlock(lines):
    """
    Return a list of the lines that are at a 
    greater indentation level than the first
    line of the list.
    :param: lines: a list of lines from the text file
    """
    block = [lines[0]]
    for line in lines[1:]:
        if len(line.split("\t")) == len(lines[0].split("\t")):
            break
        if len(line.split("\t")) > len(lines[0].split("\t")):
            block.append(line)
    return block

def checkCert(block):
    """
    Return True or False if the block passes
    the VELP test
    :param: block: a list of lines to be checked
    """
    print("checking: ")
    print(block)

    # base case
    if len(block) == 1 and block[0].strip() == "2--1":
        print("========================")
        return True

    # check VELP conditions
    if checkVertex(block[0]) == False:
        return False
    if checkEdge(block) == False:
        return False
    if checkLeaf(block) == False:
        return False
    if checkProd(block) == False:
        return False

    print("========================")

    # recursively check the sub-blocks in block
    # specifically the blocks at +1 indentation level
    for node in enumerate(block[1:]):
        if len(node[1].split("\t")) == 1 + len(block[0].split("\t")):
            if checkCert(getBlock(block[1+node[0]:])) == False:
                return False
    return True

def checkVertex(node):
    print("checking V:")
    N = int(node.strip().split("--")[0])
    a = int(node.strip().split("--")[1])
    if a**(N-1) % N != 1:
        print(str(node) + "is bad\n")
        return False
    print("vertex %s good\n" %(str(node)))
    return True
 
def checkEdge(block):
    print("checking E:")
    N = int (block[0].strip().split("--")[0])
    a = int (block[0].strip().split("--")[1])
    for node in block[1:]:
        k = int (node.strip().split("--")[0])
        if len(node.split("\t")) == 1 + len(block[0].split("\t")):
            if (N - 1) % k != 0 or a**((N-1)//k) % N == 1:
                print("%d is not a witness to %d\n" %(a, N))
                return False
    print("%d**(%d-1)/k != 1 for all k\n" %(a, N))
    return True

def checkLeaf(block):
    print("checking L:")
    for node in block:
        if node.strip() == "2--1":
            print("there is a node that leads to 2--1\n")
            return True
    print("there is a node that does not lead to 2--1\n")
    return False

def checkProd(block):
    print("checking P:")
    N = int (block[0].strip().split("--")[0])
    prod = 1
    for node in block[1:]:
        n = int (node.strip().split("--")[0])
        if len(node.split("\t")) == 1 + len(block[0].split("\t")):
            prod *= n
    if prod != N - 1:
        print("product is not correct\n")
        return False
    print("product is %d == %d-1\n" %(prod, N) )
    return True

def main():
    inputFile = open("certificate.txt", "r")
    timeFile = open("checkTimes.txt", "a")
    lines = inputFile.readlines()
    lines = [node.rstrip() for node in lines]
    startTime = time.time()

    if checkCert(lines) == True:
        print("certificate is valid")
    else:
        print("certificate is not correct")

    endTime = time.time()

    timeFile.write(str(endTime - startTime) + "\n")
    timeFile.close()
    inputFile.close()

main()
