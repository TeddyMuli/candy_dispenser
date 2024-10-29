#!/usr/bin/env python3
from typing import List, Any

"""
Python module for stack operations
Teddy Muli
SCT211-0023/2022
"""


def push(stack: List, element: Any) -> List:
    """Insert an element in a stack."""
    stack.append(element)
    return stack

def pop(stack: List) -> Any:
    """Remove the last element from the stack."""
    element = stack.pop()
    return element

def top(stack: List) -> Any:
    """Show the last element in the stack without removing it."""
    element = stack[-1]
    return element

def is_empty(stack: List) -> bool:
    """
    Check if the stack is empty.
    Returns True, else False.
    """
    return len(stack) == 0

def stack_length(stack: List) -> List:
    """Returns the length of a stack"""
    return len(stack)

