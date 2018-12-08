from graphviz import Digraph
import sys

def main ():
    if len( sys.argv) != 2:
        print ("Only provide one argument")
        exit()

    N = int ( sys.argv[1] )
#    N = int ( input ("Enter a number: ") )
    primeFactors = factorize ( N - 1, [] )

    g = Digraph ('G', filename = 'sample-output/certificateGraph_' + '%s'%N + '.gv')
    g.attr( 'node', shape='plaintext', fixedsize='true', width='0.9')

    if witness ( N, primeFactors ) == -1:
        print ( "%d is not prime" %N )
    else:
        graph ( N, primeFactors, witness ( N, primeFactors ), subLayer ( N, primeFactors ), g, [] )
        g.view()

def factorize ( N, primeFactors ):
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
    child = set()
    for i in primeFactors:
        child.add( witness (i, factorize (i - 1, [] ) ) )
    return sorted ( list ( child ) )

def graph ( N, primeFactors, parent, child, g, existingNodes ):
    for pair in child:
        childN = pair[0]
        childFactors = factorize ( childN - 1, [] )
        for i in range ( primeFactors.count(childN) ):
            g.edge ( '%s' %(parent,), '%s' %(pair,) )

        if childN not in existingNodes:
            graph ( childN, childFactors, pair, subLayer ( childN, childFactors ), g, existingNodes )
            existingNodes.append(childN)


main()


