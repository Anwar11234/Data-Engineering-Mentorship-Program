def hIndex(citations) :
    n = len(citations)
    freq = [0] * (n + 1)
            
    for num in citations:
        if num >= n:
            freq[n] += 1
        else:
            freq[num] += 1
    
    total = 0
    for i in range(n, -1, -1):
        total += freq[i]
        if total >= i:
            return i
    
    return 0