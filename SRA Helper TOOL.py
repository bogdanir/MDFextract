"""
Bogdan Irimescu
"""

import os
import sys
import mdfreader
import webbrowser
import pandas as pd
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from mdfreader import Mdf
import xlsxwriter


ratie = 0.01
location = os.getcwd()


def import_signal_data():
    global v
    global signals_file_path

    signals_file_path = filedialog.askopenfilename()
    print(signals_file_path)
    v.set(signals_file_path)
    if not signals_file_path.endswith('.xlsx'):
        lb = Label(root, text="Unsupported format, or corrupt file. Please use '.xlsx' file format!", fg='red', font=("Helvetica", 11))
        lb.place(x=10, y=359)
        lb.after(2000, lambda: lb.destroy())
    else:
        lb = Label(root, text="File format OK!", fg='forest green', font=("Helvetica", 11))
        lb.place(x=10, y=359)
        lb.after(3000, lambda: lb.destroy())
    return


def citeste_semnale():
    global config
    global lista_semnale
    global df
    global df2
    global df3

    lista_semnale = []
    lista_threshold = []
    df = pd.ExcelFile(v.get()).parse(sheet_name=0)
    df.index = df.index.map(str)
    df2 = df['Signal']
    df3 = df['Threshold']
    for val_signal in df2:
        lista_semnale.append(val_signal)
    for val_threshold in df3:
        lista_threshold.append(val_threshold)
    # my_dataframe = pd.DataFrame(lista_semnale, lista_threshold)
    return lista_semnale


def selection_of_folder():
    global folder_selected
    global z

    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    return folder_selected


def execute():
    global v, folder_selected
    global mysignals
    global lista
    global csv_file_path
    global main_folder

    lista = citeste_semnale()
    main_folder = selection_of_folder()
    for (here, subFolders, files) in os.walk(main_folder, topdown=True):
        for name in files:
            file_path = os.path.join(here, name)
            lb = Label(root, text="Reading MDF         ", fg='black', font=("Helvetica", 11))
            lb.place(x=10, y=359)
            lb.after(4000, lambda: lb.destroy())

            if name.endswith('.mdf'):
                mysignals = mdfreader.Mdf(file_path, channel_list=lista, convert_after_read=True)  # type: Mdf
                mysignals.export_to_csv(sampling=float(ratie))
            else:
                lb = Label(root, text="No MDF files found.", fg='black', font=("Helvetica", 11))
                lb.place(x=10, y=359)
                lb.after(10000, lambda: lb.destroy())
    messagebox.showinfo(title="SRA Helper Tool v. 1.0",
                        message="RUNNING! \n\nPlease make sure as much as possbile not to have other files in the folder than .mdf (in specially .csv), or the script might not work!")

    global df

    t = -1
    semnale = []
    maximele = []
    timpul_aparitie = []
    lista_threshold = []
    lista_status = []
    lista_percentage = []
    filenaming = []

    for (here, subFolders, files) in os.walk(main_folder, topdown=True):
        for name in files:

            file_path = os.path.join(here, name)

            fieldnames2 = ["File_name", "Signal", "Max Value", "Time", "Threshold", "Status", "Percentage%"]
            if name.endswith('.csv'):
                t = 0
                for i in df2:
                    filenaming.append(file_path)
                    # df2.index = df2.index.map(str)
                    semnale.append(i)
                    poz = df2.index[t]
                    t = t + 1
                    df4 = pd.read_csv(file_path)
                    p = df4[i].max()
                    maximele.append(p)
                    pos = df4[i].idxmax()
                    sec = df4.iloc[pos, 2]
                    timpul_aparitie.append(sec)
                    j = df.loc[poz, 'Threshold']
                    lista_threshold.append(j)
                    if p <= j:
                        status = "OK"
                    else:
                        status = "Failed"
                    lista_status.append(status)
                    perc_from_threshold = (p/j)*100
                    lista_percentage.append(perc_from_threshold)
                    # print('MAX:', i, '=', p, " ", df4.iloc[pos, 2], "threshold = ", j, status, perc_from_threshold)
                    fieldnames = pd.DataFrame(
                        {"File_name": filenaming, "Signal": semnale, "Max Value": maximele,
                         "Time": timpul_aparitie,
                         "Threshold": lista_threshold, "Status": lista_status, "Percentage%": lista_percentage},
                        columns=fieldnames2)
                    with open('Resultfile.xlsx', 'wb+') as excelfile:
                        writer = pd.ExcelWriter(excelfile, engine='xlsxwriter')
                        fieldnames.to_excel(writer, startrow=True, header=True)
                        writer.save()

            else:
                pass
    webbrowser.open("Resultfile.xlsx")


def about():
    messagebox.showinfo(title="SRA Helper Tool v. 1.0", message="In order for this to work, you have to provide the signals in an excel file that has first column called 'Signal', second column called 'Threshold'. \n\nFor any problems write me at: irimescu_bogdan@yahoo.com")


if __name__ == '__main__':

    root = Tk()
    #root.iconbitmap(True, 'C:\Users\irimescub\Desktop\SRAhelper\SRAhelperTOOL\Jonathan-Rey.ico')

    root.title("SRA Helper Tool")
    root.geometry("500x400+10+20")
    lbl = Label(root, text="Please select your signals file:", fg='black', font=("Helvetica", 12))
    lbl.place(x=110, y=50, anchor='n')

    signal_address = Label(root, text='Signals File Path:')
    signal_address.place(x=0, y=100, anchor='w')
    v = StringVar()
    entry = Entry(root, textvariable=v, width=40)
    entry.place(x=110, y=100, anchor='w')
    entry1 = Button(root, text='Browse File', command=import_signal_data)
    entry1.place(x=10, y=135, anchor='w')
    # entry.after(25000, lambda: entry.destroy())

    lbl = Label(root, text="Please select the folder of your MDF files:", fg='black', font=("Helvetica", 16))
    lbl.place(x=200, y=200, anchor='n')
    btn = Button(root, text="Browse", fg='blue', command=execute)
    btn.place(x=20, y=240)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="About", command=about)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Help", menu=filemenu)
    status = Label(root, text="v. 1.0", bd=1, relief=SUNKEN, anchor=E)
    status.place(relx=1.0, rely=1.0, anchor='se')

    root.config(menu=menubar)

    root.mainloop()
