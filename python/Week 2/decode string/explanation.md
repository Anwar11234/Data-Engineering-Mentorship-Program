Problem Link:https://leetcode.com/problems/decode-string/


## Solution
1. **Setup**:
   - `stack`: Keeps track of strings and numbers when encountering brackets.
   - `currStr`: The current string being built.
   - `currNum`: The current number, it represents the number of times the next string will be repeated

2. **Processing the string (`s`)**:
   - **If the character is `'['`**:
     - Push the current string (`currStr`) and the current number (`currNum`) onto the stack.
     - Reset `currStr` to an empty string and `currNum` to 0.  
       This prepares for decoding the substring inside the brackets.

   - **If the character is `']'`**:
     - Pop the last number (`num`) from the stack (indicating how many times to repeat the current string).
     - Pop the last string (`prevStr`) from the stack (the string built before this level).
     - Combine them: Repeat `currStr` `num` times, then add it to `prevStr`.  
       Update `currStr` to this combined result.

   - **If the character is a digit (`c.isdigit()`)**:
     - Update `currNum` to handle multi-digit numbers.  
       (E.g., for `"23"`, it builds the number as `2 * 10 + 3 = 23`.)

   - **If the character is a letter**:
     - Add the letter to `currStr` (builds the string inside the current bracket level).

3. **Return the result**:
   - After processing all characters, `currStr` will hold the final decoded string.


### **Key Ideas**:
- Use a **stack** to keep track of the context (current string and repetition count) for each nested level of brackets.
- Build the result step by step, handling numbers, strings, and nested patterns efficiently.