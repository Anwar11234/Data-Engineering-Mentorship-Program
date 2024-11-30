Problem Link: https://leetcode.com/problems/h-index/

## Solution

- The solution to this problem inspires some ideas from [counting sort](https://www.youtube.com/watch?v=1618cb-oA1o). 

- The logic is to a create a frequency array of citations such that each index in this frequency array is the number of occurances for a given number of citations. 

- The size of the frequency array will be the length of the `citations` array - which is the total number of papers - plus one. The indices will range from 0 to `n` where `n` is the length of the `citations` array. The frequency array is initialized with zeros.

- Whenever we encounter a number of citations `num` greater than `n` we increment the frequency at the `nth` index by one, otherwise we increment the frequency at index `num` by one.

```Python
    for num in citations:
        if num >= n:
            freq[n] += 1
        else:
            freq[num] += 1
```

- After filling the frequency array, we loop through it starting from its end to its start, we create a variable called `total` to track the number of citations greater than the current number by adding `freq[i]` value to total as we move from the end of frequency array to the beginning. Whenever we find an element with `total` greater than or equal to its value then that's our h-index, if there's no such number we return 0. 

- The reason to scan from the end of the array is that we are looking for the greatest `h` with at least `h` papers cited at least `h` times, so we check numbers from greatest to smallest.

``` Python
    total = 0
    for i in range(n, -1, -1):
        total += freq[i]
        if total >= i:
            return i
```