import os
import tkinter as tk
from tkinter import messagebox


def shutdown_computer():
    os.system('shutdown /s /t 1')

def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Shutdown Program")
root.configure(background="lightblue")

# Set the size of the window
root.geometry("400x200")

# Function to handle the choices
def handle_choices(choice):
    if choice == 'shutdown':
        shutdown_computer()
    elif choice == 'exit':
        exit_program()

# Create and place buttons
shutdown_button = tk.Button(root, text="Shutdown", command=lambda: handle_choices('shutdown'))
shutdown_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=lambda: handle_choices('exit'))
exit_button.pack(pady=10)

# Run the GUI
root.mainloop()
