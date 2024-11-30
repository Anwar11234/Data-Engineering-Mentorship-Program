Problem Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/. 

## Solution

- The problem requires finding the maximum number of vowel letters in any substring with length `k`, this can be achieved using the sliding window technique.

- Since we need to find the max number of vowels in a substring with length `k`, the window's size will be fixed, it will always be `k`.

- We loop through all the characters of `s`, for the initial `k` elements we just count the number of vowels. Then we move the window to the rigt by decrementing the number of vowels in the current window by 1 if the first character in the window was a vowel and incrementing the number of vowels in the current window by 1 if the new character in the window was a vowel. 

- While looping we keep track of the maximum number of vowels reached so far, this will be the result returned at the end.