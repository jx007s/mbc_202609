nums = [34,56,78,86,23,46,17,83,22,64,75]

tot = 0
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        tot += nums[i]
    print(i, nums[i], tot)
    i+=1 

print(tot)