'''
Created on 13-Aug-2017

@author: Ankit
'''
'''A class that can find if a given number is Even or Odd'''

class EvenFinder:
    
    simpleEven = lambda num: num % 2 == 0;
    simpleOdd = lambda num: num % 2 == 1;
    
    '''  bitwise operator even test, 
    Here we will do logical AND of the number wit binary value of 1. 
    if this is equal to 0  that means last bit of the given number is 0 so given number is even '''
    logicalEven = lambda num: num & 1 == 0;
    
    logicalOdd = lambda num: num & 1 == 1;
    
    @staticmethod
    def isEven(num):
        return EvenFinder.simpleEven(num);
    
    @staticmethod
    def isOdd(num):
        return EvenFinder.simpleOdd(num);
    
    
    @staticmethod
    def isLogicalEven(num):
        return EvenFinder.logicalEven(num);
    
    @staticmethod
    def isLogicalOdd(num):
        return EvenFinder.logicalOdd(num);
    
    
if __name__ == "__main__":
        
        nums = list(range(-10, 10))
        for n in nums:
            if EvenFinder.isEven(n):
                print(n, " is even ")
            else: 
                if EvenFinder.isOdd(n):
                    print(n, ' is odd ')
            
        for n in nums:
            if EvenFinder.isLogicalEven(n):
                print(n, " is even ")
            else: 
                if EvenFinder.isLogicalOdd(n):
                    print(n, ' is odd ')
        
        
