
#input: any positive integer
#returns: the smallest multiple evenly divisible by all numbers 1 - n
def smallest_multiple(n):
     i = 29579180
     #stop the loop at an arbitrarily large number
     while i < 1000000000000000:
          j = n
          while j > 0:
               if i % j != 0:
                    break
               j -= 1
          if j == 0:
               return i
          i += n
     return "no multiple divisible by all 20 numbers"


print smallest_multiple(20)
          
     
     
