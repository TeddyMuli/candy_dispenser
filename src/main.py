#!/usr/bin/env python3

"""
Python module for stack operations
Teddy Muli
SCT211-0023/2022
"""

import tkinter as tk
from tkinter import messagebox, ttk


push = __import__('stack').push
pop = __import__('stack').pop
top = __import__('stack').top
is_empty = __import__('stack').is_empty
stack_length = __import__('stack').stack_length
is_full = __import__('stack').is_full

stack = []

def push_element():
    element = entry.get()
    if not element:
        messagebox.showwarning("Push", "Please enter an element.")
    elif is_full(stack):
        messagebox.showwarning("Push", "The stack is full!")
    else:
        push(stack, element)
        update_progress_bar()
        messagebox.showinfo("Push", f"Element '{element}' pushed to stack.")
        
def pop_element():
    if not is_empty(stack):
        element = pop(stack)
        update_progress_bar()
        messagebox.showinfo("Pop", f"Element '{element}' popped from stack.")
    else:
        messagebox.showwarning("Pop", "Stack is empty.")

def top_element():
    if not is_empty(stack):
        element = top(stack)
        messagebox.showinfo("Top", f"Top element is '{element}'.")
    else:
        messagebox.showwarning("Top", "Stack is empty.")

def check_empty():
    if is_empty(stack):
        messagebox.showinfo("Is Empty", "Stack is empty.")
    else:
        messagebox.showinfo("Is Empty", "Stack is not empty.")

def check_full():
    if is_full(stack):
        messagebox.showinfo("Is Full", "Stack is full.")
    else:
        messagebox.showinfo("Is Full", "Stack is not full.")

def stack_len():
    length = stack_length(stack)
    messagebox.showinfo("Length", f"Stack length is {length}.")

def update_progress_bar():
    max_length = 11
    current_length = max_length - stack_length(stack)
    progress_bar['value'] = (current_length / max_length) * 100
    length_label.config(text=f"Number of candies: {stack_length(stack)}")

root = tk.Tk()
root.title('Candy dispenser')

root.geometry('400x500')

label = tk.Label(root, text='Add candy')
label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

btn_push = tk.Button(root, text="Add candy", command=push_element)
btn_push.grid(row=2, column=0, padx=5, pady=5)

btn_pop = tk.Button(root, text="Remove candy", command=pop_element)
btn_pop.grid(row=2, column=1, padx=5, pady=5)

btn_top = tk.Button(root, text="Check top candy", command=top_element)
btn_top.grid(row=3, column=0, padx=5, pady=5)

btn_is_empty = tk.Button(root, text="Check if dispenser is empty", command=check_empty)
btn_is_empty.grid(row=3, column=1, padx=5, pady=5)

btn_is_full = tk.Button(root, text="Check if dispenser is full", command=check_full)
btn_is_full.grid(row=4, column=0, padx=5, pady=5)

btn_len = tk.Button(root, text="Number of candies", command=stack_len)
btn_len.grid(row=4, column=1, padx=5, pady=5)

progress_bar = ttk.Progressbar(root, orient='vertical', length=200, mode='determinate')
progress_bar.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

length_label = tk.Label(root, text="Stack Length: 0")
length_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

update_progress_bar()

root.mainloop()
