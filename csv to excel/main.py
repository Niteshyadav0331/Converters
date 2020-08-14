from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd 


class Converter:
    def __init__(self,root):
        self.root = root
        self.root.geometry('460x370+420+120')
        self.root.title("Billing Software")
        self.root.resizable(0, 0)
        bg_color = "#074463"
        title = Label(self.root,text="CSV to Excel Converter",bd=12,relief=GROOVE,bg=bg_color,fg="Gold",font=("times new roman",20,"bold"),pady=2).pack(fill = X)
        F1 = LabelFrame(self.root,bd=12,relief=GROOVE,bg=bg_color)
        F1.place(x=1,y=65, width = 457, height = 304)

        def getCSV():
            global read_file

            import_file_path = filedialog.askopenfilename()

            read_file = pd.read_csv(import_file_path)


        browsebutton = Button(F1, text = "      Import CSV File      ", command = getCSV, bg = 'DarkSlateGrey', fg = 'SandyBrown', font=('helvetica', 12, 'bold'), bd = 8, relief = GROOVE)
        browsebutton.grid(row = 0, column = 0, pady = 40, padx = 125)

        def convertToExcel():
            global read_file

            export_file_path = filedialog.asksaveasfilename(defaultextension = ".xlsx")
            read_file.to_excel(export_file_path, index = None, header = True)

        saveasbutton = Button(F1, text = "Convert CSV to Excel", command = convertToExcel, bg = 'DarkSlateGrey', fg = 'SandyBrown', font=('helvetica', 12, 'bold'), bd = 7, relief = GROOVE)
        saveasbutton.grid(row = 1, column = 0, padx = 125)

        def exit_application():
            msgbox = messagebox.askquestion('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if msgbox == "yes":
                root.destroy()

        exitbutton = Button(F1, text = "      Exit Application      ",command = exit_application, bg = 'DarkSlateGrey', fg = 'SandyBrown', font=('helvetica', 12, 'bold'), bd = 7, relief = GROOVE)
        exitbutton.grid(row = 2, column = 0, pady = 40, padx = 125)



root = Tk()
obj = Converter(root)


root.mainloop()