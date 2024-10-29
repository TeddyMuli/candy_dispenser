#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, ttk

push = __import__('stack').push
pop = __import__('stack').pop
top = __import__('stack').top
is_empty = __import__('stack').is_empty
stack_length = __import__('stack').stack_length

stack = []

def push_element():
    element = entry.get()
    if element:
        push(stack, element)
        update_progress_bar()
        messagebox.showinfo("Push", f"Element '{element}' pushed to stack.")
    else:
        messagebox.showwarning("Push", "Please enter an element.")

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

def stack_len():
    length = stack_length(stack)
    messagebox.showinfo("Length", f"Stack length is {length}.")

def update_progress_bar():
    max_length = 10  # Define the maximum length of the stack for the progress bar
    current_length = stack_length(stack)
    progress_bar['value'] = (current_length / max_length) * 100
    length_label.config(text=f"Stack Length: {current_length}")

root = tk.Tk()
root.title('Candy dispenser')

entry = tk.Entry(root)
entry.pack(pady=10)

label = tk.Label(root, text='Candy dispenser')
label.pack()

btn_push = tk.Button(root, text="Push", command=push_element)
btn_push.pack(pady=5)

btn_pop = tk.Button(root, text="Pop", command=pop_element)
btn_pop.pack(pady=5)

btn_top = tk.Button(root, text="Top", command=top_element)
btn_top.pack(pady=5)

btn_is_empty = tk.Button(root, text="Is Empty", command=check_empty)
btn_is_empty.pack(pady=5)

btn_len = tk.Button(root, text="Length", command=stack_len)
btn_len.pack(pady=5)

progress_bar = ttk.Progressbar(root, orient='vertical', length=200, mode='determinate')
progress_bar.pack(pady=10)

length_label = tk.Label(root, text="Stack Length: 0")
length_label.pack(pady=5)

update_progress_bar()

root.mainloop()
