def main ():
    N = int ( input("Enter a number: ") )
    primeFactors = factorize ( N-1, set() )
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
    if number == 2:
        return 2
    else: 
        while ( ( wit ** (number-1) % number != 1 ) or ( 1 in [wit ** (number // i) % number for i in primeFactors] ) ):
            wit += 1
        return wit 

def certificate ( number, primeFactors, space ):
    for i in primeFactors:
        if i == 2:
            print ( space + "The witness for 2 is 2")
        else:
            print( space + "The witness for %d is %d" % (i, witness ( i, factorize( i - 1, set()) ) ) )
            certificate ( i, factorize ( i - 1, set() ), space  + "     " )

if __name__ == "__main__":
    main()
