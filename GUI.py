from tkinter import *
from tkinter import messagebox


def about():
    messagebox.showinfo(title="SRA Helper Tool v. 1.0", message="In order for this to work, you have to provide the signals in an excel file that has first column called 'Signal', second column called 'Threshold'. \n\nFor any problems write me at: irimescu_bogdan@yahoo.com")


root = Tk()
root.iconbitmap(True, 'C:\Users\irimescub\Desktop\SRAhelper\SRAhelperTOOL\Jonathan-Rey.ico')

root.title("SRA Helper Tool")
root.geometry("500x400+10+20")
lbl = Label(root, text="Please select the folder of your MDF files:", fg='black', font=("Helvetica", 16))
lbl.place(x=3, y=30)
btn = Button(root, text="Browse", fg='blue')
btn.place(x=10, y=65)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About", command=about)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Help", menu=filemenu)
status = Label(root, text=folder_selected, bd=1, relief=SUNKEN, anchor=W)
status.place(x=0, y=375)

root.config(menu=menubar)
root.mainloop()

