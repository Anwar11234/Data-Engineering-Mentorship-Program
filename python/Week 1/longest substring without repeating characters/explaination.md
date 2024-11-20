Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Solution:

- To solve this problem I used the sliding window technique, two pointers `left` and `right` are used to track the current substring.

- A variable called `maxLen` is used to track the length of longest substring without repeating characters. 

- To detect repeating characters in the current window, a `set` data structure is used. 

- Before adding a charachter to the window we check if it's in the `set`: 
    -- If it isn't we add it to the `set` and expand the window and update `maxLen` if
       the new window size is greater than `maxLen`
    -- If it's in the `set` we remove it and shrink the window