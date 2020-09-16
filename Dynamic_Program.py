
#Knapsack problem - DP

# Longest Increasing Subsequence
def lengthOfLIS(nums):
    if not nums:
        return 0

    long = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                long[i] = max(long[i],long[j]+1)
    return max(long)

#house robber problem
def rob(nums):
    nums = [0,0,0] + nums
    for i in range(3,len(nums)):
        before3, before2 = nums[i-3] + nums[i], nums[i-2] + nums[i]
        nums[i] = max(before3, before2)
    return max(nums)
