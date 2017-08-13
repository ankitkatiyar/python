'''
Created on 13-Aug-2017

@author: Ankit
'''
'''A class that can find prime numbers with different algorithms'''

from math import sqrt, floor

import time as tm


class PrimeFinder:
    
    @staticmethod
    def smallPrime(num):
        for k in range(2, num):
            if num % k == 0:
                return False
        return True
    
    """ Using a better also for the large number of series""" 
    @staticmethod
    def largePrime(num):
        for k in range(2, floor(sqrt(num))):
            if num % k == 0:
                return False
        return True

    """ Define a generic function for calculation """
    @staticmethod
    def isPrime(num):
        if num < 10000:
            return  PrimeFinder.smallPrime(num)
        else:
            return  PrimeFinder.largePrime(num)
        
    """ Define a generic function for lists of elements """
    @staticmethod
    def isPrimes(num=[]):
        out = list()
        for n in num:
            out.append(PrimeFinder.isPrime(n))
        return out
    
    
    
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    ''' Start test and also track the time'''
    start = tm.time()
    for n in range(1, 10):
        print(n, " is prime: ", PrimeFinder.smallPrime(n))
    print("Completed in: ", (tm.time() - start)) 
    
    '''test for larger series'''
    start = tm.time()
    for n in range(1, 10000):
        """ avoid printing as it takes time """
        PrimeFinder.smallPrime(n)
    timeTaken = (tm.time() - start)
    print("Completed in: ", timeTaken) 
    
    ''' test for same series but with different algo '''
    start = tm.time()
    for n in range(1, 10000):
        PrimeFinder.largePrime(n)
    timeTaken1 = (tm.time() - start);
    print("Completed with large fn in: ", timeTaken1) 
    print("Time saved: ", (timeTaken - timeTaken1))
    
    ''' try generic function call '''
    start = tm.time()
    for n in range(1, 100000):
        PrimeFinder.isPrime(n)
    timeTaken = (tm.time() - start);
    print("Completed with large fn in: ", timeTaken) 
    
    
    ''' test our generic function for list '''
    start = tm.time()
    out = PrimeFinder.isPrimes(list(range(1, 10000)))
    timeTaken = (tm.time() - start);
    print('Computed in: ', timeTaken, ' first few outputs:', out[:10])

    

    
