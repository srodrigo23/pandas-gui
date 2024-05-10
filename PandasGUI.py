from tkinter import *
from pandastable import Table, TableModel

class PandasGuiApp(Frame):
    
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Data Frame GUI')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        # df = TableModel.getSampleData()
        self.table = pt = Table(
            f, 
            dataframe=None,
            showtoolbar=True,
            showstatusbar=True
        )
        pt.show()
        return

app = PandasGuiApp()
app.mainloop()