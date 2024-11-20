def lengthOfLongestSubstring(s):
    left = right = 0
    maxLen = 0
    currSubstr = set()
    
    while right < len(s):
        if s[right] not in currSubstr:
            currSubstr.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            right += 1
        else:
            currSubstr.remove(s[left])
            left += 1
    
    return maxLen