def minSubArrayLen(target, nums):
    left = right = 0
    currSum = 0
    minLen = float("inf")

    while right < len(nums):
        currSum += nums[right]

        while currSum >= target:
            minLen = min(minLen, right - left + 1)
            currSum -= nums[left]
            left += 1 
        
        right += 1

    return minLen if minLen != float("inf") else 0