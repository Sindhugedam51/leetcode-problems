import tkinter as tk
from tkinter import messagebox

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

def show_primes():
    primes_list = get_primes(1, 20)
    messagebox.showinfo("Prime Numbers", f"Prime numbers from 1 to 20: {primes_list}")

root = tk.Tk()
root.title("Prime Number Checker")

tk.Label(root, text="Click the button to check prime numbers in range 1-20").pack(pady=10)
tk.Button(root, text="Check Primes", command=show_primes).pack(pady=5)

root.mainloop()
