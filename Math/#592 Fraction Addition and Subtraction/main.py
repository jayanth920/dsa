def solve(expr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    res_num = 0  # Numerator of the result
    res_den = 1  # Denominator of the result
    i = 0
    while i < len(expr):
        sign = 1  # Positive by default
        if expr[i] == "-":
            sign = -1
            i += 1
        elif expr[i] == "+":
            i += 1

        # Find numerator
        j = i
        while expr[j] != "/":
            j += 1
        num = int(expr[i:j])

        # Find denominator
        i = j + 1
        j = i
        while j < len(expr) and expr[j].isdigit():
            j += 1
        den = int(expr[i:j])
        i = j

        # Convert to a common denominator
        common_den = lcm(res_den, den)
        res_num = res_num * (common_den // res_den) + sign * num * (common_den // den)
        res_den = common_den

        # Simplify the fraction
        divisor = gcd(abs(res_num), res_den)
        res_num //= divisor
        res_den //= divisor

    # Return the fraction in the form "numerator/denominator"
    return f"{res_num}/{res_den}"


print(solve("-1/2+1/2"))
print(solve("-1/2+1/2+1/3"))
print(solve("1/3-1/2"))
