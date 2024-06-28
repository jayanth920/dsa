def reverse(x: int) -> int:
    rev_int = int(str(abs(x))[::-1])
    
    if rev_int > 2**31 - 1 or rev_int < -2**31:
        return 0
    
    return rev_int if x > 0 else -rev_int
