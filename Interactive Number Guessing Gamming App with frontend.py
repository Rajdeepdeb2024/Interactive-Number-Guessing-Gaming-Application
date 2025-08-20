import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
pythonr_number = random.randint(1, 10)

# Initialize guess tracking
chance = 3

# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.resizable(True, True)
root.configure(bg="#f0f8ff")

# ---------------- Functions ----------------
def check_guess():
    global chance
    user_input = entry.get()

    if not user_input.isdigit():
        status_label.config(text="❌ Please enter a valid number between 1 and 10.", fg="red")
        return

    guess = int(user_input)
    entry.delete(0, tk.END)

    if guess == pythonr_number:
        status_label.config(text="✅ Correct guess! You win!", fg="green")
        disable_game()
    else:
        chance_left = chance - 1
        if chance_left > 0:
            status_label.config(
                text=f"❌ Wrong guess. Try again! Chances left: {chance_left}", fg="orange"
            )
            chance_display.config(text=f"Chances left: {chance_left}")
        else:
            status_label.config(
                text=f"❌ Game Over! The correct number was {pythonr_number}.", fg="red"
            )
            messagebox.showinfo("Game Over", "Better luck next time!")
            disable_game()
        chance -= 1

def disable_game():
    entry.config(state="disabled")
    guess_button.config(state="disabled")

def reset_game():
    global pythonr_number, chance
    pythonr_number = random.randint(1, 10)
    chance = 3
    entry.config(state="normal")
    guess_button.config(state="normal")
    entry.delete(0, tk.END)
    status_label.config(text="Enter a number between 1 and 10 to begin.", fg="black")
    chance_display.config(text="Chances left: 3")

# ---------------- Widgets ----------------
title_label = tk.Label(root, text="🎯 Number Guessing Game", font=("Helvetica", 18, "bold"), bg="#f0f8ff")
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", font=("Helvetica", 12, "bold"), command=check_guess, bg="#4CAF50", fg="white", width=10)
guess_button.pack(pady=5)

status_label = tk.Label(root, text="Enter a number between 1 and 10 to begin.", font=("Helvetica", 12), bg="#f0f8ff")
status_label.pack(pady=10)

chance_display = tk.Label(root, text="Chances left: 3", font=("Helvetica", 12, "bold"), bg="#f0f8ff", fg="blue")
chance_display.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 10), command=reset_game, bg="#2196F3", fg="white")
reset_button.pack(pady=10)

# ---------------- Start App ----------------
entry.focus()
root.mainloop()

