def solve(nums):
    # METHOD 1
    # counter = 0
    # # 0-9 = ph num,10 - gender,11-12 - age,seat - 13,14
    # for item in details:
    #     if int(item[11:13]) > 60:
    #         counter+=1
    # return counter
    
    # METHOD 2
    return sum(int(x[11:13]) > 60 for x in nums)


print(solve(["7868190130M7522","5303914400F9211","9273338290F4010"]))
print(solve(["1313579440F2036","2921522980M5644"]))