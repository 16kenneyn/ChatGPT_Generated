import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tkinter App")

        self.label = tk.Label(self.root, text="Hello, World!")
        self.label.pack()

        self.button = tk.Button(self.root, text="Quit", command=self.quit)
        self.button.pack()

    def quit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
