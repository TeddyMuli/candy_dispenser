#!/usr/bin/env python3
"""
Python module for stack operations
Teddy Muli
SCT211-0023/2022
"""


def push(stack, element):
    """Insert an element in a stack."""
    stack.append(element)
    return stack

def pop(stack) :
    """Remove the last element from the stack."""
    element = stack.pop()
    return element

def top(stack) :
    """Show the last element in the stack without removing it."""
    element = stack[-1]
    return element

def is_empty(stack) -> bool:
    """
    Check if the stack is empty.
    Returns True, else False.
    """
    return len(stack) == 0

def is_full(stack) -> bool:
    """
    Check if the stack is full.
    Return True, else False
    """
    return len(stack) >= 7

def stack_length(stack):
    """Returns the length of a stack"""
    return len(stack)
