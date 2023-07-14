import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class GradeCalc():
    def __init__(self):        
        self.root = tk.Tk()        
        self.root.title("CMSC 437 Calculator")   # page title
        self.root.geometry('300x180')    # stock dimension

        # variables that will store user input
        self.bio_var = tk.StringVar()
        self.math_var = tk.StringVar()

        self.content = ttk.Frame(self.root)

        # sio section
        self.bio_frame = ttk.Frame(self.content)
        self.bio_frame.pack(side='top', pady=10)

        self.label_bio = ttk.Label(self.bio_frame, text='Bio:')
        self.entry_bio = ttk.Entry(self.bio_frame, textvariable=self.bio_var)

        self.label_bio.pack(side='left', padx=5)
        self.entry_bio.pack(side='left', padx=5)

        # math section
        self.math_frame = ttk.Frame(self.content)
        self.math_frame.pack(side='top', pady=10)

        self.label_math = ttk.Label(self.math_frame, text='Math:')
        self.entry_math = ttk.Entry(self.math_frame, textvariable=self.math_var)

        self.label_math.pack(side='left', padx=5)
        self.entry_math.pack(side='left', padx=5)

        # average section
        self.avg_label = tk.Label(self.content, text="Average: ")
        self.avg_label.pack(side='top', pady=10)

        # new frame for buttons
        self.button_frame = ttk.Frame(self.content)
        self.button_frame.pack(side='top', pady=10)

        self.calcButton = ttk.Button(self.button_frame, text='Calculate', command=self.saveInput)   # when clicked, go to saveInput function
        self.quitButton = ttk.Button(self.button_frame, text='Quit', command=self.quit)             # when clicked, go to quit function (destroy)

        # buttons will appear next to each other
        self.calcButton.pack(side='left')
        self.quitButton.pack(side='left')

        self.content.pack()
        self.root.mainloop()

    def saveInput(self):
        # retrieve the value from the entry variable
        self.bio_input = self.bio_var.get()
        self.math_input = self.math_var.get()

        # validate inputs
        if self.isFloat(self.bio_input) and self.isFloat(self.math_input):
            bio_float = float(self.bio_input)
            math_float = float(self.math_input)

            avg_value = self.average(bio_float, math_float)
            self.avg_label.config(text="Average: {:.2f}".format(avg_value))
        else:
            self.errorBox()    # show error box

    def isFloat(self, value):  # input validation
        try:
            float(value)    # if number, return True
            return True
        except ValueError:  # else, if error, return False
            return False

    def errorBox(self):  # popup error box
        messagebox.showinfo('Error', 'The grades are not correct!')

    def average(self, bio, math):
        average = (bio + math) / 2.0    # average calculation
        return average

    def quit(self):  # closes window
        self.root.destroy()

app = GradeCalc()