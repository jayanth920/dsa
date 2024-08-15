class TwoSum:
    def __init__(self):
        self.myarr = []
        
    def add(self, num):
        self.myarr.append(num)
        
    def findSum(self,target):
        self.myarr.sort()
        x = 0
        y = len(self.myarr) - 1
        while x<y:
            sum = self.myarr[x] + self.myarr[y]
            if sum > target:
                y-=1
            elif sum < target:
                x+=1
            elif sum == target:
                return True
        return False
            
        
    def printall(self):
        self.myarr.sort()
        for item in self.myarr:
            print(item)
            
            
hello = TwoSum()
hello.add(10)
hello.add(50)
hello.add(900)
hello.add(20)
hello.add(2)
print(hello.findSum(23))