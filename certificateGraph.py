from graphviz import Digraph
# import sys

'''
Test for primality and generate a directed graph Pratt Certificate for primes
'''

def main ():
#     if len( sys.argv) != 2:
#         print ("Only provide one argument")
#         exit()

#     N = int ( sys.argv[1] )
    N = int ( input ("Enter a number: ") )
    primeFactors = factorize ( N - 1, [] )

    g = Digraph ('G', filename = 'sample-output/certificateGraph_' + '%s'%N + '.gv')
    g.attr( 'node', shape='plaintext', fixedsize='true', width='0.9')

    if witness ( N, primeFactors ) == -1:
        print ( "%d is not prime" %N )
    else:
        graph ( N, primeFactors, witness ( N, primeFactors ), subLayer ( N, primeFactors ), g, [] )
        g.view()

def factorize ( N, primeFactors ):
    '''
    Return a sorted list of the prime factors of a given number
    :param: N:            the number to be prime factorized
    :param: primeFactors: list (with duplicates) containing the current known prime factors of N
    '''
    factor = 3
    if N == 1:
        return primeFactors
    elif N % 2 == 0:
        primeFactors.append(2)
        return factorize ( N // 2, primeFactors )
    else:
        while N % factor != 0:
            factor += 2
        primeFactors.append(factor)
        return factorize ( N // factor, primeFactors )

def witness ( N, primeFactors ):
    '''
    test for primality and if the input is prime, generate a (number, witness) tuple
    :param: N           : the number to test for primality and generate a witness for
    :param: primeFactors: a list of the prime factors of N - 1
    '''
    a = 2
    if N == 2:
        return ( 2, 1 )
    elif a ** (N - 1) % N != 1:
        return -1 
    else: 
        while ( 1 in [a ** ( (N - 1) // k) % N for k in primeFactors] ):
            a += 1
    return ( N, a )

def subLayer ( N, primeFactors ):
    '''
    Compute the set of nodes eminating from a parent node
    :param: N          : the parent node
    :param primeFactors: a list of the prime factors of N - 1
    '''
    child = set()
    for i in primeFactors:
        child.add( witness (i, factorize (i - 1, [] ) ) )
    return sorted ( list ( child ) )

def graph ( N, primeFactors, parent, child, g, existingNodes ):
    '''
    Draw the connections from a parent node to all children nodes
    :param: N            : the number to generate the graph of 
    :param: primeFactors : a list of the prime factors of N - 1
    :param: parent       : the parent tuple node
    :param: child        : a list of all children tuple nodes
    :param: g            : the existing graph
    :param: existingNodes: a list of the numbers on which we
                           have already recursed on
    '''
    for pair in child:
        childN = pair[0]
        childFactors = factorize ( childN - 1, [] )
        for i in range ( primeFactors.count(childN) ):
            g.edge ( '%s' %(parent,), '%s' %(pair,) )

        if childN not in existingNodes: # statement to avoid drawing edges from tuples which have already had
                                        # outgoing arcs
            graph ( childN, childFactors, pair, subLayer ( childN, childFactors ), g, existingNodes )
            existingNodes.append(childN)


main()

