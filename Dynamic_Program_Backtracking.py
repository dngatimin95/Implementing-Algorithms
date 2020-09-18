
# Coin change
def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)

    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]

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

# House robber problem
def rob(nums):
    nums = [0,0,0] + nums
    for i in range(3,len(nums)):
        before3, before2 = nums[i-3] + nums[i], nums[i-2] + nums[i]
        nums[i] = max(before3, before2)
    return max(nums)

# Maximum subarray
def maxSubArray(nums):
    maxSum = currSum = nums[0]
    for i in range(1,len(nums)):
        currSum = max(nums[i], currSum + nums[i])
        maxSum = max(maxSum, currSum)
    return maxSum

# Best time to Buy and Sell Stock
def maxProfit(prices):
    maxProfit = 0
    lowPrice = float('inf')

    for i in prices:
        if i < lowPrice:
            lowPrice = i
        if i - lowPrice > maxProfit:
            maxProfit = i-lowPrice
    return maxProfit

# Generate Paranthesis
def generateParenthesis(n):
    res = []
    self.dfs(n, n, "", res)
    return res

def dfs(self, leftRemain, rightRemain, path, res):
    if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
        return
    if leftRemain == 0 and rightRemain == 0:
        res.append(path)
        return
    self.dfs(leftRemain-1, rightRemain, path+"(", res)
    self.dfs(leftRemain, rightRemain-1, path+")", res)
