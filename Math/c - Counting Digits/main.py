#-----------------------Most Optimal - O(1)---------------------
import math

# Calculate the count of digits in 'n'
# using logarithmic operation log10(n) + 1.
def countDigits(n):
    # Initialize a variable 'cnt' to
    # store the count of digits.
    cnt = int(math.log10(n) + 1)

    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
    # Return the count of digits in 'n'.
    return cnt


# ---------------------O(logn(base 10) + 1)----------------------------
def countDigits(n):
    # Initialize a counter variable
    # 'cnt' to store the count of digits.
    cnt = 0
    # While loop iterates until 'n'
    # becomes 0 (no more digits left).
    while n > 0:
        # Increment the counter
        # for each digit encountered.
        cnt = cnt + 1
        # Divide 'n' by 10 to
        # remove the last digit.
        n = n // 10
    # Return the
    # count of digits.
    return cnt

print(countDigits(489237))