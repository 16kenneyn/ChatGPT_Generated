import tkinter as tk

# Create the root window
root = tk.Tk()

# Create a table with some data
data = [
    ["Name", "Age", "Gender"],
    ["John", "25", "Male"],
    ["Jane", "32", "Female"],
    ["Joe", "40", "Male"],
]

# Create a Tkinter table with the data
table = tk.Table(root, data=data)
table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a simple entry box
entry = tk.Entry(root)
entry.pack(side=tk.RIGHT)

# Create a simple response label
response = tk.Label(root, text="")
response.pack(side=tk.RIGHT)

# Define a function to update the response label
# when the user enters something in the entry box
def update_response(*args):
    response.configure(text="You entered: " + entry.get())

# Update the response label when the user types something in the entry box
entry.bind("<Key>", update_response)

# Start the main event loop
root.mainloop()
