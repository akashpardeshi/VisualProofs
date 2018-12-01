from graphviz import Digraph
import sys

def main ():
     if len( sys.argv) != 2:
         print ("Only provide one argument")
         exit()

     N = int ( sys.argv[1] )
     primeFactors = factorize ( N - 1, [] )

     g = Digraph ('G', filename = 'sample-output/certificateGraph_' + '%s'%N + '.gv')
     g.attr( 'node', shape='plaintext', fixedsize='true', width='0.9')


     if N == 2:
         print ( "2 is prime" )
     elif witness ( N, primeFactors ) == -1:
         print ( "%d is not prime" %N )
     else:
         graph ( N, witness ( N, primeFactors ), subLayer ( N, primeFactors ), g )
         # g.attr(label = r'Conditions for primality: \n'
         #                r'1: For all verticies (a, N), a ^ (N-1) is congruent to 1 (mod N) \n'
         #                r'2: For all parent verticies (a, N) with child verticies (x, P), a ^ (N-1)/x and x divides N-1 \n'
         #                r'3: For all parent verticies (a, N) with child verticies (x1, P1), (x2, P2), ..., (xi, Pi), N - 1 = x1 * x2 * ... * xN \n'
         #                r'4: All verticies must eventually connect to the \'2\' vertex')
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
        return 2 
    elif a ** (N - 1) % N != 1:
        return -1 
    else: 
        while ( 1 in [a ** ( (N - 1) // k) % N for k in primeFactors] ):
            a += 1
    return ( N, a )

def subLayer ( N, primeFactors ):
    child = []
    for i in primeFactors:
        child.append( witness (i, factorize (i-1, [] ) ) )
    return child

def graph (N, parent, child, g):
    for pair in child:
        if pair == 2:
            g.edge ( '%s' %(parent,), '2' )
        else:
            g.edge ( '%s' %(parent,), '%s' %(pair,) )
            graph ( pair[0], pair, subLayer (pair[0], factorize ( pair[0] - 1, [] ) ), g )

main()



