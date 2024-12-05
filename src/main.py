#!/usr/bin/env python3
"""
Python module for stack operations
Teddy Muli
SCT211-0023/2022
"""

import tkinter as tk
from tkinter import messagebox
from stack import push, pop, is_empty, stack_length, is_full, top

stack = []
max_stack_size = 7
candy_colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

def push_element():
    if is_full(stack):
        messagebox.showwarning("Push", "The stack is full!")
    else:
        element = len(stack) + 1 
        push(stack, element)
        update_stack_display()

def pop_element():
    if not is_empty(stack):
        popped_element = pop(stack)
        update_stack_display()
        messagebox.showinfo("Pop", f"Popped element: {popped_element}")
    else:
        messagebox.showwarning("Pop", "Stack is empty.")

def top_element():
    if not is_empty(stack):
        top_candy = top(stack)
        messagebox.showinfo("Top", f"Top element: {top_candy}")
    else:
        messagebox.showwarning("Top", "Stack is empty.")

def check_empty():
    if is_empty(stack):
        messagebox.showinfo("Empty Check", "The stack is empty.")
    else:
        messagebox.showinfo("Empty Check", "The stack is not empty.")

def check_full():
    if is_full(stack):
        messagebox.showinfo("Full Check", "The stack is full.")
    else:
        messagebox.showinfo("Full Check", "The stack is not full.")

def stack_len():
    length = stack_length(stack)
    messagebox.showinfo("Stack Length", f"Stack length: {length}")

def update_stack_display():
    canvas.delete("all")
    
    spring_bottom = 300
    spring_top = spring_bottom - (max_stack_size * 40)

    if stack:
        spring_top += (len(stack) * 40)

    num_coils = 10
    coil_spacing = (spring_bottom - spring_top) / num_coils
    
    for i in range(num_coils):
        x1, y1 = 100, spring_bottom - i * coil_spacing
        x2, y2 = 140, spring_bottom - (i + 0.5) * coil_spacing
        canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)
        canvas.create_line(x2, y2, x1, y1 - coil_spacing, fill="gray", width=2)
    
    for i, candy in enumerate(stack):
        x1, y1 = 100, spring_top - (i + 1) * 40
        x2, y2 = x1 + 40, y1 + 40
        canvas.create_oval(x1, y1, x2, y2, fill=candy_colors[candy - 1], outline="black")
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(candy), fill="white", font=("Arial", 14))
    
    length_label.config(text=f"Number of candies: {len(stack)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Candy Dispenser')
    root.geometry('400x500')

    btn_push = tk.Button(root, text="Add candy", command=push_element)
    btn_push.grid(row=0, column=0, padx=5, pady=5)

    btn_pop = tk.Button(root, text="Remove candy", command=pop_element)
    btn_pop.grid(row=0, column=1, padx=5, pady=5)

    btn_top = tk.Button(root, text="Peek top", command=top_element)
    btn_top.grid(row=1, column=0, padx=5, pady=5)

    btn_is_empty = tk.Button(root, text="Is empty?", command=check_empty)
    btn_is_empty.grid(row=1, column=1, padx=5, pady=5)

    btn_is_full = tk.Button(root, text="Is full?", command=check_full)
    btn_is_full.grid(row=2, column=0, padx=5, pady=5)

    btn_len = tk.Button(root, text="Stack length", command=stack_len)
    btn_len.grid(row=2, column=1, padx=5, pady=5)

    canvas = tk.Canvas(root, width=200, height=400, bg="white")
    canvas.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

    length_label = tk.Label(root, text="Number of candies: 0")
    length_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    root.rowconfigure(3, weight=1)

    update_stack_display()

    root.mainloop()
