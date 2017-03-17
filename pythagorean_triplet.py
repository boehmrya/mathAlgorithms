

#input: a number for which the pythagorean triplet adds up to
#returns: the product of the pytagorean triplet
def find_triplet_product(n):
     a = 1
     b = 1
     c = 1
     while a < n:
          while b < n:
               while c < n:
                    if (a + b + c) == n:
                         if ((a*a) + (b*b)) == (c*c):
                              print "a is currently: ", a
                              print "b is currently: ", b
                              print "c is currently: ", c
                              return a * b * c
                    c += 1
               b += 1
               c = b + 1
          a += 1
          b = a + 1
     return "there are no pythagorean triplets that add up to that number"


print find_triplet_product(1000)
     
