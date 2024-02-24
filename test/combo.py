import tkinter as tk
from tkinter import ttk

# Create a Tkinter window
root = tk.Tk()
root.title("Dropdown Menu with Tkinter Bootstrap")

# Add the Tkinter Bootstrap theme
style = ttk.Style()

# Define the options for the dropdown menu
options = ["JPEG", "PNG", "BMP"]

# Create a Combobox widget with the options
combo_box = ttk.Combobox(root, values=options, state="readonly")
combo_box.pack(pady=20)

# Set the initial value of the Combobox to the first value in the options list
combo_box.set(options[0])


# Function to handle selection
def handle_selection(event):
    selected_option = combo_box.get()
    print("Selected option:", selected_option)


# Bind the selection event to the function
combo_box.bind("<<ComboboxSelected>>", handle_selection)

# Run the Tkinter event loop
root.mainloop()
