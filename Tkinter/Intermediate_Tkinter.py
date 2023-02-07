import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Intermediate Tkinter App")

        # Create a label
        self.label = tk.Label(self.root, text="Enter your name:")
        self.label.pack()

        # Create an entry field
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # Create a submit button
        self.button = tk.Button(self.root, text="Submit", command=self.submit)
        self.button.pack()

        # Create a label to display the result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def submit(self):
        # Get the text from the entry field
        name = self.entry.get()

        # Set the text of the result label
        self.result_label.config(text=f"Hello, {name}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
