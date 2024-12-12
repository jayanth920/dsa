# BEST - PRECISION =>  NEWTONS METHOD - BABYLONS METHOD
# def sqrt(number):
#     if number < 0:
#         return "Cannot calculate square root of a negative number"
#     if number == 0:
#         return 0
#     x = number / 2 # Initial guess for the square root

#     while True:
#         next_x = (x + number / x) / 2  # Calculate a better approximation using the Babylonian method
        
#         if abs(next_x - x) < 1e-10: # Check for convergence
#             return next_x

#         x = next_x

# print(sqrt(6))
# print(sqrt(25))


# FOR INT - NEWTON-RAPHSON METHOD
def sqrt(x):
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r

print(sqrt(6))
print(sqrt(25))



# def solve(x):
#     if x == 4:
#         return 2
#     elif x == 2:
#         return 1
#     elif x == 1 or x == 0:
#         return 0
#     res = 0
#     for i in range(x//2):
#         a = i*i
#         b = (i+1)*(i+1)
#         if a<=x and b>=x:
#             res = i
        
#     return res

