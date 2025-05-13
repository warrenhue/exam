def count_digits(number):
    nums = {}
    for digit in number:
        if digit not in nums.keys():
            nums[digit] = 1
        else:
            nums[digit] += 1
    return nums
print(count_digits(input()))