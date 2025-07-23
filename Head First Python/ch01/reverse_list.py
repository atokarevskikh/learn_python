nums = list(range(11))
print(nums)
k = len(nums) - 1
for i in range(k):
    nums.insert(i, nums.pop())
print(nums)
print(nums[::-1])
