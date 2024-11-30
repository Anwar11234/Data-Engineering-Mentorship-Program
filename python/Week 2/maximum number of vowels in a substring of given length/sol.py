def maxVowels(s, k):
    vowels = 'aeiou'
    currRes = 0
    res = 0
    
    for i in range(len(s)):
        if i >= k and s[i - k] in vowels:
            currRes -= 1
        if s[i] in vowels:
            currRes += 1
        res = max(currRes, res)

    return res