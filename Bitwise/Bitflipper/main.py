def bitflipper(start,goal):
    c = 0
    start = list(bin(start))[2:]
    goal = list(bin(goal))[2:]
    
    
    if len(start) > len(goal):
        while len(goal) < len(start):
            goal.insert(0,"0")
    else:
        while len(goal) > len(start):
            start.insert(0,"0")
            
    for i in range(len(goal)-1,-1,-1):
        if start[i] != goal[i]:
            c += 1
            start[i] = goal[i]
    return c
    
print(bitflipper(10, 7))
print(bitflipper(3, 4))