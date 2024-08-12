def sortJumbled(mapping, nums):
    def map_number(num: int) -> int:
        numstr = str(num)
        mappedstr = "".join(str(mapping[int(digit)]) for digit in numstr)
        return int(mappedstr)

    return sorted(nums, key=lambda num: map_number(num))
