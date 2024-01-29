def calculate(nums):
  if not nums:
    return 0
  else:
    return sum(nums[i] for i in range(0, len(nums), 2)) * nums[-1]



print(calculate([0, 1, 7, 2, 4, 8])) ## 88
print(calculate([1, 3, 5]))          ## 30
print(calculate([6]))                ## 36
print(calculate([]))                 ## 0
