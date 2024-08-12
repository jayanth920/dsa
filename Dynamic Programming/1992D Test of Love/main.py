""" 
take in n,m,k
pos = 0
LWLLLW
for i in range(n):
    if river[i] == 'C':
        return 'NO'
    jump_possible = False
    for jump in range(1,m+1):
        if position + jump >=n+1:
            return 'YES'
        if river[position+jump] != 'C':
            position += jump
            jump_possible = True
            break
        
        
"""