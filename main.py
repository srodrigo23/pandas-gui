from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog

import tkinter as tk   
from tkinter import font as tkfont
import pandas as pd
from tkinter import ttk

class My_GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18,
            weight="bold", slant="italic"
        )

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page_2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to....", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Option selected",
                            command=lambda: controller.show_frame("Page_2"))
        button1.pack()

class Page_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="The payment options are displayed below", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        global df
        tk.Label(self, text='Select option:').pack()
        self.options = ttk.Combobox(self, values=list(df.columns))
        self.options.pack()
        tk.Button(self, text='Show option', command=self.show_option).pack()

        self.text = tk.Text(self)
        self.text.pack()

        tk.Button(self, text="Restart",
                  command=lambda: controller.show_frame("StartPage")).pack()

    def show_option(self):
        identifier = self.options.get() # get option
        self.text.delete(1.0, tk.END)   # empty widget to print new text
        self.text.insert(tk.END, str(df[identifier]))

# class Page_2(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="The payment options are displayed below", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)

#         #I want the able to be display the dataframe here

#         button = tk.Button(self, text="Restart",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()

a = {'Option_1':[150,82.50,150,157.50,78.75],
     'Option2':[245,134.75,245,257.25,128.63]}
df = pd.DataFrame(a,index=['a',
                    'b',
                    'c',
                    'd',
                    'e']) 

print(df.iloc[:6,1:2])

if __name__ == "__main__":
    app = My_GUI()
    app.mainloop()