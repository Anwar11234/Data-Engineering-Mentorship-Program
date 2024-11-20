Problem Link: https://leetcode.com/problems/minimum-size-subarray-sum/

## Solution:

- To solve this problem I used the sliding window technique by initializing 2 pointers `left` and `right` to represent the bounderies of the sliding window. Both variables start at 0. 

- Then a variable `currSum` is created to track the sum of the current subarray with numbers between `left` and `right`, and a variable `minLen` to track the minimum possible subarray length with sum >= target. 

- The main idea is to keep expanding the window by incrementing `right` pointer and adding `nums[right]` to `currSum` until `currSum` is greater than or equal to `target`. 

- When that happens we have a subarray with sum >= `target`. But since we want the minimum length subarray that meets this condition we keep shrinking the window by incrementing `left` pointer and subtracting `nums[left]` from `currSum` and updating `minLen` variable. `minLen` is updated to be the minimum of its current value and `r - l + 1` which is the length of the current window.

- We keep shrinking until `currSum` is no longer >= `target`, at this point we don't have a valid window so we need to expand the window again. 

- We keep repeating these steps until `right` pointer exceeds the given array's length, at this point we return `minLen`. 