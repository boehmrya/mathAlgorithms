
def sum_square_difference(n):
     n_sum = n
     n_square = n
     #sum of squares for all numbers less than or equal to n
     current_square = 0
     sum_of_squares = 0
     n_sum = n
     while n_sum > 0:
          current_square = n_sum * n_sum
          sum_of_squares += current_square
          n_sum -= 1
     #square of the sum of all numbers less than or equal to n
     current_sum = 0
     square_of_sum = 0
     while n_square > 0:
          current_sum += n_square
          n_square -= 1
     square_of_sum = current_sum * current_sum
     #calculate the difference
     difference = square_of_sum - sum_of_squares
     return difference

print sum_square_difference(100)
