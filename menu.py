from tkinter import Frame, Tk, BOTH, Menu, END, Label, font, CENTER
from tkinter import filedialog
from pandastable import Table, TableModel

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.parent.title("Pandas GUI")
        self.pack(side="top", fill=BOTH, expand=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_font = font.Font(
            family='Helvetica', size=18,
            weight="bold", 
            # slant="italic"
        )

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        # self.txt = Text(self)
        # self.txt.pack(fill=BOTH, expand=1)
        
        self.buildPandasTableFrame()
        self.buildWhiteFrame(text="Cargar CSV desde el menu")
    

    def buildPandasTableFrame(self)->None:
        self.pandasTableFrame = Frame(self)
        # self.pandasTableFrame.pack(fill=BOTH, expand=1)
        # self.label = Label(self.pandasTableFrame,
        #     text="Pandas Data Table",
        #     font=self.title_font
        # )
        # self.label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.pandasTableFrame.grid(row=0, column=0, sticky="nsew")
        # df = TableModel.getSampleData()
        # self.table = pt = Table(
        #     self.pandasTableFrame, 
        #     dataframe=df,
        #     showtoolbar=True,
        #     showstatusbar=True
        # )
        # pt.show()

    def buildWhiteFrame(self, text:str) ->None:
        self.whiteFrame = Frame(self)
        # self.whiteFrame.pack(fill=BOTH, expand=1)
        label = Label(self.whiteFrame,
            text=text, 
            font=self.title_font
        )
        # label.pack(side="", fill="x", pady=10)
        label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.whiteFrame.grid(row=0, column=0, sticky="nsew")
        # relx = 0.5, rely = 0.5, anchor = CENTER

    def onOpen(self):
        ftypes = [('CSV files', '*.csv')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        filename = dlg.show()
        if filename != '':
            file_path = self.readFile(filename)
            # self.label['text']=file_path
            df = TableModel.getSampleData()
            self.table = pt = Table(
                self.pandasTableFrame, 
                dataframe=df,
                showtoolbar=True,
                showstatusbar=True
            )
            pt.show()
            self.pandasTableFrame.tkraise()
            # self.txt.insert(END, text)

    def readFile(self, filename) -> str:
        f = open(filename, "r")
        return f.name

def main():
    root = Tk()
    Example(root)
    root.geometry("500x400+300+300")
    root.mainloop()  

if __name__ == '__main__':
    main()