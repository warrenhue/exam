def countNums(nums):
    counter = {}
    for num in nums:
        if num not in counter.keys():
            counter[num] = 1
        else:
            counter[num] += 1
    return counter

def twoDimArray(nums):
    if not nums:
        return []
    count = countNums(nums)
    twodim = [[] for _ in range (max(count.values()))]
    for value, frequency in count.items():
        for row in range(frequency):
            twodim[row].append(value)
    return twodim

print(twoDimArray([1,2,3,4,1,2,2,3]))

