
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


#input: positive integer n
#returns: the nth prime number
def reveal_nth_prime(n):
     i = 1
     num_prime = 0
     while num_prime < n:
          i += 1
          if is_prime(i):
               num_prime += 1
               #print "number of primes is: ", num_prime
               #print "current prime number is: ", i
     return i

print reveal_nth_prime(10001)             
     
