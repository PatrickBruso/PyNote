import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("PyNote")

        # Create text box for window
        self.text = tk.Text(self)
        self.text.pack(side="top")

        # Create save button
        self.button = tk.Button(self, text="Save", command=self.saveas)
        self.button.pack(side="bottom")
        self.pack()

    # Save function
    def saveas(self):
        t = self.text.get("1.0", "end-1c")
        save_location = filedialog.asksaveasfilename()
        file1 = open(save_location, "w+")
        file1.write(t)
        file1.close()

# Start program
root = tk.Tk()
app = Application(root)
app.mainloop()