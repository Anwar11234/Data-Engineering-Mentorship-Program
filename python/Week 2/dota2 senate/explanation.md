Problem Link: https://leetcode.com/problems/dota2-senate/description/

### Problem Summary
- The senate consists of two parties: **Radiant (R)** and **Dire (D)**.
- The game proceeds in rounds. Each senator can:
  1. Ban a senator from the opposing party (eliminating their ability to vote in future rounds).
  2. Remain in the game to participate in the next round.
- The party that manages to ban all senators of the other party wins.

Our task is to determine which party will win based on the given initial sequence of senators.

### Thought Process
1. **Understand the Dynamics of the Problem**
   - Each senator takes turns, starting from the first in the sequence.
   - If a senator from one party bans a senator from the other party, that banned senator cannot participate in future rounds.
   - The sequence repeats cyclically until one party is eliminated.

2. **Challenges**
   - Senators need to take turns cyclically.
   - The ban decision affects future turns, so we need a way to track which senators are still in the game.

3. **Key Observations**
   - We can model this problem as a **queue-based simulation**, where:
     - Each senator's index is stored in a queue, representing their position in the original sequence.
     - Senators take turns in order of the queue.
     - A senator bans the closest senator from the opposing party and moves to the back of the queue if they survive.
   - By comparing the indices of the senators from the two parties, we can simulate who bans whom.

4. **Approach**
   - Use two queues:
     - One for the indices of all **Radiant** senators.
     - Another for the indices of all **Dire** senators.
   - Process the queues in a round-robin manner:
     - Compare the **front indices** of the two queues.
     - The senator with the smaller index bans the senator with the larger index (closer to the front acts first).
     - Move the winning senator to the end of their queue (simulating them taking a turn in the next round).

5. **Simulation Logic**
   - **If a Radiant senator bans a Dire senator**:
     - Remove the Dire senator from the queue.
     - Move the Radiant senator to the back of their queue with an updated index (their next turn is after all senators currently in the queue).
   - **If a Dire senator bans a Radiant senator**:
     - Similarly, remove the Radiant senator and move the Dire senator to the back.
   - Repeat until one queue is empty.


### Walkthrough of the Code

1. **Initialization**:
   - Two queues, `radiant` and `dire`, store the indices of Radiant and Dire senators, respectively.

2. **Simulation**:
   - Use a while loop to process senators until one queue is empty.
   - For each round, compare the indices of the first senators in both queues.
     - The senator with the smaller index survives and gets re-added to the back of their queue with an updated index.

3. **Termination**:
   - When one of the queues becomes empty, the game ends.
   - If `radiant` is empty, Dire wins; otherwise, Radiant wins.

This approach models the problem as a queue-based simulation, which simplifies handling the circular nature of the sequence. It ensures fairness in processing and handles bans systematically, leading to an efficient and intuitive solution.