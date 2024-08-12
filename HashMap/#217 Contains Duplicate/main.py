def containsDuplicate(nums):
    my = {}

    for i in range(len(nums)):
        if nums[i] in my:
            return True
        else:
            my[nums[i]] = i

    return False
