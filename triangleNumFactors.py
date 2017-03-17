
import math


def triangleNumFactors(limit):
    ''' Determines the first triangle number with the number of divisors equal to
        the limit. '''
    
    currentNum = 1
    maxFactors = 0
    
    while maxFactors < limit:
        numFactors = 0
        triangleNum = currentNum + 1 # update the triangle number
        
        if triangleNum % 2 != 0:
            currentNum += 1
            continue
        
        # count the number of factors for the current triangle number
        i = 1
        while i <= math.sqrt(triangleNum):
            if triangleNum % i == 0:
                numFactors += 1
            i += 1
        numFactors *= 2
                
        # check if the number of factors for the current number is the new max
        if numFactors > maxFactors:
            maxFactors = numFactors
                
        currentNum += 1
        
        #print("max factors: " + str(maxFactors))
        #print("triangle number: " + str(triangleNum))
        
    return triangleNum
        
        
        
print(triangleNumFactors(500))