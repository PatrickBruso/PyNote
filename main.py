import tkinter as tk
from tkinter import filedialog
from custom_widgets.custom_prompt import CustomPrompt

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("PyNote")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Save file location for opened files
        self.file_location = None
        self.saved_t = ""

        # Create menu bar
        self.menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.master.config(menu=self.menu_bar)
        file_menu.add_command(label="New", command=self.new)
        file_menu.add_command(label="Open", command=self.open)
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_command(label="Save as...", command=self.saveas)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Create text box for window
        self.text = tk.Text(self)
        self.text.pack(side="top")
        
        self.pack()

    #Check if the text was changed (True if was - otherwise False)
    def text_is_changed(self):
        t = self.text.get("1.0", "end-1c")
        if(t == self.saved_t):
            return False
        else:
            return True

    # New Function
    def new(self):
        self.text.delete("1.0", "end")

    #Save function
    def save(self):
        if(self.file_location is None):
            self.saveas()
        else:
            self.saved_t = self.text.get("1.0", "end-1c")
            file1 = open(self.file_location, "w+")
            file1.write(self.saved_t + "\n")
            file1.close()

    # Save as function
    def saveas(self):
        self.saved_t = self.text.get("1.0", "end-1c")
        save_location = filedialog.asksaveasfilename()
        if(save_location != ''):
            self.file_location = save_location
            file1 = open(save_location, "w+")
            file1.write(self.saved_t + "\n")
            file1.close()

    # Open function
    def open(self):
        # Placeholder for future CommandPrompt class call

        # Find location of file to open
        open_location = filedialog.askopenfilename(title='Open Text File', filetypes=[('text files', '*.txt')])
        
        if (open_location != ''): # Check file was selected and .txt file
            opened_file = open(open_location, "r") # Open file
            opened_text = opened_file.read() # Read file and save text
            self.text.delete("1.0", "end-1c") # Delete old text
            self.text.insert("1.0", opened_text) # Insert text to text box at line 1, character 0
            opened_file.close() # Close file
            self.file_location = open_location # Set file_location variable to opened file location

    def save_and_close(self):
        self.save()
        self.master.destroy()

    def on_closing(self):
        if(self.text_is_changed()):
            cp = CustomPrompt(self, "PyNote", "Do you want to save the changes?", ["Save", "Don't save", "Cancel"], [self.save_and_close, self.master.destroy, None])
        else:
            self.master.destroy()

# Start program
root = tk.Tk()
app = Application(root)
app.mainloop()
