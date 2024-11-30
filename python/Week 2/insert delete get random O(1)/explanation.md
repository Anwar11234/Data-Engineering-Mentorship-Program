Problem Link: https://leetcode.com/problems/insert-delete-getrandom-o1/

## Solution

- This problem requires building a data structure called `RandimizedSet` where you can insert, delete, and get a random value in `O(1)` average time. 

- The insertion and deletion can be achieved in `O(1)` average time by using a `set`, the problem is in getting a random value, this will take `O(n)` to convert the `set` to a `list` and choose a random value. 

- We can achieve getting a random value in `O(1)` by using a `list` alongside a hash map, the hash map will map each value to its index in the values list.

- To insert a value, we first make sure the value doesn't already exist, then we append the value to the values list, and put the value as a key in the hash map with its index in the values list as the value for the key. 

- To remove a value, we have to make sure this happens in `O(1)` average time, we first need to know if the value exists or not before deleting. If it exists, we swap it with the last value in the values list, then we pop the values list and delete the value from the hash map. We also need to update the index of the last value in the hash map to be the index of the last value to be the index of the removed value.

- To get a random value, we just use `random.choice` on the values list.