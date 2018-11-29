'''
Test for primality and generate a Pratt Certificate for primes
'''

def main ():
    N = int ( input ( "Enter a number: " ) )
    primeFactors = factorize ( N - 1, set() )

    if N == 2:
        print ( "2 is prime" )
    elif ( witness ( N, primeFactors ) == -1 ):
        print ( "%d is not prime" % ( N ) )
    else:
        print ( "%d -- %d" % ( N, witness ( N, primeFactors ) ) )
        certificate ( N, primeFactors, "    " )

def factorize ( N, primeFactors ):
    '''
    Return a sorted list of the prime factors of a given number
    :param: N:            the number to be prime factorized
    :param: primeFactors: list containing the prime factors of number
    '''
    factor = 3
    if N == 1:
        return sorted ( list ( primeFactors ) )
    elif N % 2 == 0:
        primeFactors.add(2)
        return factorize ( N // 2, primeFactors )
    else:
        while N % factor != 0:
            factor += 2
        primeFactors.add(factor)
        return factorize ( N // factor, primeFactors )

def witness ( N, primeFactors ):
    '''
    test for primality and if the input is prime, generate a witness
    :param: N           : the number to test for primality and generate a witness for 
    :param: primeFactors: a list of the prime factors of number - 1
    '''
    a = 2
    if a ** (N - 1) % N != 1:
        return -1 
    else: 
        while ( 1 in [a ** ( (N - 1) // k) % N for k in primeFactors] ):
            a += 1
    return a 

def certificate ( N, primeFactors, space ):
    '''
    generate a Pratt Certificate for a prime number
    :param: N:            the number to be issued a certificate
    :param: primeFactors: list of the prime factors of number - 1
    :param: space:        formatting string of empty space
    '''
    for k in primeFactors:
        if k == 2:
            print ( space + "2")
        else:
            print( space + "%d -- %d" % ( k, witness ( k, factorize ( k - 1, set() ) ) ) )
            certificate ( k, factorize ( k - 1, set() ), space  + "     " )

if __name__ == "__main__":
    main()
