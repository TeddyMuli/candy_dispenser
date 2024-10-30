# 🍬 candy_dispenser
## Overview
This project is meant to test my skills on the stack ADT.

## Stack ADT
This is a Last In First Out **(LIFO)** ADT.
The last element to be added to the stack is the first to be accessed.

### Implementation
I used a list to implement my stack:
```python
stack = []
```

### Operations
1. **Push (Add candy)** 🍭
   This adds an element into the stack.
   ```python
   stack.append(element)
   ```

2. **Pop (Remove candy)** 🍬
   This removes the last element added to the stack.
   ```python
   stack.pop()
   ```

3. **Top (Check top candy)** 🍫
   This checks the topmost element in the stack.
   ```python
   stack[-1]
   ```

4. **IsEmpty (Check if dispenser is empty)** 🍭
   This checks if the stack is empty.
   ```python
   len(stack) == 0
   ```

5. **IsFull (Check if dispenser is full)** 🍬
   This checks if the stack is full.
   I set a hard limit of 10.
   ```python
   len(stack) >= 10
   ```

6. **Len (Number of candies in the dispenser)** 🍫
   This checks the length of the stack.
   ```python
   len(stack)
   ```

### Requirements
1. Install python3 in your system.

### Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/TeddyMuli/candy_dispenser.git
   ```

2. cd into the directory:
   ```bash
   cd candy_dispenser
   ```

3. Run the app:
   ```bash
   python3 src/main.py
   ```
