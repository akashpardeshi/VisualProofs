import time
import sys

"""
given a natural number, writes
a Pratt Certificate to a text file.
"""

def factorize ( N, primeFactors ):
    '''
    Return a sorted list of the prime factors of a given number
    :param: N:            the number to be prime factorized
    :param: primeFactors: list containing the prime factors of number
    '''
    factor = 3
    if N == 1:
        return list ( primeFactors )[::-1]
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

def certificate ( N, primeFactors, space, outputFile ):
    '''
    generate a Pratt Certificate for a prime number
    :param: N:            the number to be issued a certificate
    :param: primeFactors: list of the prime factors of number - 1
    :param: space:        formatting string of empty space
    '''
    for k in primeFactors:
        if k == 2:
            outputFile.write(space + "2--1\n")
        else:
            outputFile.write(space + "%d--%d\n" % ( k, witness ( k, factorize ( k - 1, [] ) ) ) )
            certificate ( k, factorize ( k - 1, [] ), space  + "\t", outputFile )

def main ():
    # N = int ( input ( "Enter a number: " ) )
    N = int (sys.argv[1])
    outputFile = open("certificate.txt", "w")
    timeFile = open("times.txt", "a")

    startTime = time.time()

    primeFactors = factorize ( N - 1, [] )
    if N == 2:
        outputFile.write("2--1\n")
        endTime = time.time()
    elif ( witness ( N, primeFactors ) == -1 ):
        print ( "%d is not prime" % ( N ) )
        endTime = time.time()
    else:
        outputFile.write("%d--%d\n" % ( N, witness ( N, primeFactors ) ))
        certificate ( N, primeFactors, "\t", outputFile )
        endTime = time.time()

    # print(endTime - startTime)
    timeFile.write(str(endTime - startTime) + "\n")

    timeFile.close()
    outputFile.close()

main()
