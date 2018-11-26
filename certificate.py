'''
Test for primality and generate a Pratt Certificate for primes
'''


def main ():
    N = int ( input("Enter a number: ") )
    primeFactors = factorize ( N-1, set() )

    if N == 2:
        print ( "2 is prime" )
    elif (witness (N, primeFactors) == -1):
        print ( "%d is not prime" % ( N ) )
    else:
        print ( "%d -- %d" % ( N, witness ( N, primeFactors ) ) )
        certificate ( N, primeFactors, "    " )

def factorize ( number, primeFactors ):
    '''
    Return a sorted list of the prime factors of a given number
    :param: number:       the number to be prime factorized
    :param: primeFactors: list containing the prime factors of number
    '''
    factor = 3
    if number == 1:
        return sorted ( list ( primeFactors ) )
    elif number % 2 == 0:
        primeFactors.add(2)
        return factorize ( number // 2, primeFactors )
    else:
        while number % factor != 0:
            factor += 2
        primeFactors.add(factor)
        return factorize ( number // factor, primeFactors )

def witness ( number, primeFactors ):
    '''
    test for primality and if the input is prime, generate a witness
    :param: number      : the number to test for primality and generate a witness for 
    :param: primeFactors: a list of the prime factors of number - 1
    '''
    wit = 2
    if wit ** (number - 1) % number != 1:
        return -1 
    else: 
        while ( 1 in [wit ** (number // k) % number for k in primeFactors] ):
            wit += 1
    return wit 

def certificate ( number, primeFactors, space ):
    '''
    generate a Pratt Certificate for a prime number
    :param: number:       the number to be issued a certificate
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
