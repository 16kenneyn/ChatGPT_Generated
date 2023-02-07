import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Tkinter App")

        # Create a label
        self.label = tk.Label(self.root, text="Enter two numbers:")
        self.label.pack()

        # Create two entry fields
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        # Create a submit button
        self.button = tk.Button(self.root, text="Submit", command=self.submit)
        self.button.pack()

        # Create a label to display the result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def submit(self):
        # Get the numbers from the entry fields
        num1 = int(self.entry1.get())
        num2 = int(self.entry2.get())

        # Add the numbers and set the text of the result label
        result = num1 + num2
        self.result_label.config(text=f"The result is: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
