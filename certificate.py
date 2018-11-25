def main ():
    N = int ( input("Enter a number: ") )
    primeFactors = factorize ( N-1, set() )

    if (witness (N, primeFactors) == -1):
        print ( "%d is not prime" % ( N ) )
    else:
        print ( "The witness for %d is %d" % ( N, witness ( N, primeFactors ) ) )
        certificate ( N, primeFactors, "    " )

def factorize ( number, primeFactors ):
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
    wit = 2
    if wit ** (number-1) % number != 1:
        return -1 
    else: 
        while ( 1 in [wit ** (number // k) % number for k in primeFactors] ):
            wit += 1
    return wit 

def certificate ( number, primeFactors, space ):
    for k in primeFactors:
        if k == 2:
            print ( space + "The witness for 2 is 2")
        else:
            print( space + "The witness for %d is %d" % ( k, witness ( k, factorize ( k - 1, set() ) ) ) )
            certificate ( k, factorize ( k - 1, set() ), space  + "     " )

if __name__ == "__main__":
    main()
