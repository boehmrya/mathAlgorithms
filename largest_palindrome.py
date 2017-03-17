
#input: any string or integer of at least one digit or character
#returns True if the string is a palindrome.  Otherwise returns False.
def is_palindrome(s):
     s = str(s)
     while len(s) > 0:
          if s[0] == s[-1]:
               s = s[1:-1]
          else:
               return False
     return True



#input: no input
#returns a list of all products (formatted as strings) of any two 3 digit numbers, 
def three_digit_products():
     products = []
     i = 100
     while i < 1000:
          j = 100
          while j < 1000:
               current_product = i * j
               #print current_product
               products.append(current_product)
               j += 1
               #print i, j
          i += 1
          #print i, j
     return products



def largest_palindrome():
     products = sorted(three_digit_products())
     for i in reversed(products):
          if is_palindrome(i):
               return i
     return "there are no palindromes"



print largest_palindrome()
     
          
     



