

import math

#checks if a given number is prime.  Returns True if so, otherwise returns False
def is_prime(n):
     if n == 2:
          return True
     i = 2
     while i < math.sqrt(n):
          if n % i == 0:
               return False
          i += 1
     return True


#input: any non-negative integer
#returns: a list of possible prime factors of the input
def possible_prime_factors(n):
     i = 1
     factors = []
     while i < math.sqrt(n):
          if n % i == 0:
               factors.append(i)
          i += 1
     return factors
               
          

#input: any non-negative integer
#returns: the highest prime factor
def largest_prime_factor(n):
     upper_bound = int(math.sqrt(n))
     i = 3
     highest_prime = 0
     while i < upper_bound:
          #Check if prime factor
          if (is_prime(i)) and ((n % i) == 0):
               highest_prime = i
          i += 2
     return highest_prime


print largest_prime_factor(600851475143)

               
           
           
