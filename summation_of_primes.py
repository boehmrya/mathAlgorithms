
import math

#checks if a given number is prime.  Returns True if so, otherwise returns False
def is_prime(n):
     if n == 2:
          return True
     i = 2
     while i <= math.sqrt(n):
          if (n % i) == 0:
               return False
          i += 1
     return True


#input: a number n to below which to find the sum of all primes
#returns: the sum of the primes below n
def summation_of_primes(n):
     current_num = 2
     summation = 0
     while current_num < n:
          if is_prime(current_num):
               summation += current_num
          current_num += 1
     return summation


print summation_of_primes(2000000)
               

