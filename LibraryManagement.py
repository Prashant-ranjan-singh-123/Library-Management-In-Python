import webbrowser
from tkinter import *
import tkinter.messagebox as mess
from PIL import ImageTk, Image
import os
import shutil


class LibraryManagement:
    libName = []
    def __init__(self):
        self.defaultListOfBooks = ['In Search of Lost Time by Marcel Proust', 'Ulysses by James Joyce',
                              'Don Quixote by Miguel de Cervantes',
                              'One Hundred Years of Solitude by Gabriel Garcia Marquez',
                              'The Great Gatsby',
                              'Moby Dick by Herman Melville',
                              'War and Peace by Leo Tolstoy', 'Hamlet by William Shakespeare',
                              'Madame Bovary by Gustave Flaubert',
                              'The Odyssey by Homer', 'The Divine Comedy by Dante Alighieri',
                              'Lolita by Vladimir Nabokov',
                              'The Brothers Karamazov by Fyodor Dostoyevsky',
                              'Crime and Punishment by Fyodor Dostoyevsky',
                              'Wuthering Heights by Emily Brontë',
                              'The Catcher in the Rye by J. D. Salinger',
                              'Pride and Prejudice by Jane Austen',
                              'The Adventures of Huckleberry Finn by Mark Twain',
                              'Anna Karenina by Leo Tolstoy',
                              'Alice\'s Adventures in Wonderland by Lewis Carroll']

        self.how_this_program_work_string = '''Rules to make Books.txt file are:- 

1) It only contain book name nothing else

2) Each book are in new line

3) At last line no extra line tolerated

4) Name of file should be Books.txt nothing else

5) Books.txt must have reading writing 
permission.

6) It should be inside users Library Folder 
(~/Library Management/xyz Library/Books.txt)'''

        while(True):
            # This Will refresh all Library folder in libname list
            # -----------------------------------------------------------#
            if os.path.isdir("Library Management"):
                for root, dir, file in os.walk("Library Management"):
                    self.libName = dir
                    break
            for count, Libraries in enumerate(self.libName):
                if Libraries.endswith("Library") == False:
                    del self.libName[count]
            # -----------------------------------------------------------#

            if os.path.exists('Information how to add books in program') == False:
                os.makedirs('Information how to add books in program')

            with open('Information how to add books in program/Rules for making File.txt', 'w') as f:
                f.write(self.how_this_program_work_string)

            with open('Information how to add books in program/Books(Example).txt', 'w') as f1:
                str = '\n'.join(self.defaultListOfBooks)
                f1.write(str)


            selection = self.home_screen()
            if selection == 1:
                while(True):
                    is_rerun_1 = self.show_all_books()
                    if is_rerun_1 == False:
                        break
            elif selection == 2:
                  self.add_a_book()
            elif selection == 3:
                 self.del_a_library()
            elif selection == 4:
                while True:
                    is_stop = self.manage_library()
                    if is_stop:
                        break
                 # self.del_a_library()
            elif selection == 5:
                break

    def home_screen(self):
        selection_of_main_menu = None
        root = Tk()
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def submit():
            nonlocal selection_of_main_menu
            nonlocal root
            if v1.get() == 0:
                mess.showerror(title='Null Selection', message='Please select any one option.')
            elif v1.get() == 1:
                root.destroy()
                selection_of_main_menu = 1
            elif v1.get() == 2:
                root.destroy()
                selection_of_main_menu = 2
            elif v1.get() == 3:
                root.destroy()
                selection_of_main_menu = 3
            elif v1.get() == 4:
                root.destroy()
                selection_of_main_menu = 4
        def exit_button():
            nonlocal selection_of_main_menu
            nonlocal root
            root.destroy()
            selection_of_main_menu = 5

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.grid(row=0, column=1, sticky=NE, padx=20)

        # Label
        self.what_to_do = Label(root, text='Options for managing Library are given below',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.grid(row=1, column=1, sticky=N, columnspan=2, padx=100, pady=15)

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.grid(row=1, column=0, rowspan=10)

        # Radiobutton
        v1 = IntVar()
        Radiobutton(root, text='List Total Library', value=1, variable=v1, bg=self.background, highlightthickness=0, fg='#000099',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue').grid(row=2, column=1, columnspan=4,
                                                                    sticky=NW, padx=100)
        Radiobutton(root, text='Add a Library', value=2, variable=v1, bg=self.background,highlightthickness=0, fg='#000099',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue').grid(row=3, column=1, columnspan=4,
                                                                     sticky=NW, padx=100)
        Radiobutton(root, text='Delete a Library', value=3, variable=v1, bg=self.background,highlightthickness=0,fg='#000099',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue').grid(row=4, column=1, columnspan=4,
                                                                     sticky=NW, padx=100, pady=8)
        Radiobutton(root, text='Manage a Library', value=4, variable=v1, bg=self.background,highlightthickness=0,fg='#000099',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue').grid(row=5, column=1, columnspan=4,
                                                                    sticky=NW, padx=100)

        # Button
        submit = Button(text='Submit', bg='#66d9ff', padx=30, borderwidth=2, highlightbackground='black',
                        activebackground='#1a8cff', command=submit)
        submit.grid(row=2, column=1, columnspan=10, padx=350, pady=0)
        exit_button = Button(text='Exit', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_button)
        exit_button.grid(row=3, column=1, columnspan=10, rowspan=7, padx=350, pady=45)
        root.mainloop()
        return selection_of_main_menu

    def show_all_books(self):
        root = Tk()
        is_rerun = True
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)
        def exit_command():
            nonlocal root, is_rerun
            root.destroy()
            is_rerun = False

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Listbox and Scrollbar
        scroll_bar = Scrollbar(root,width=0)
        all_library_list_box = Listbox(root, selectbackground=self.background, borderwidth=0, width=48, activestyle='none', fg='#3333ff', selectforeground='#3333ff')
        for num, dir in enumerate(self.libName):
            all_library_list_box.insert(0, f'{dir}')

        all_library_list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=all_library_list_box.yview)
        all_library_list_box.place(x=380, y=100)
        scroll_bar.place(x=765, y=100,height=182, width=12)


        # Label
        self.what_to_do = Label(root, text=f'All Libraries are listed below (Total: {len(self.libName)}):-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=420, y=70)

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_command)
        exit_button.place(x=480, y=300)
        root.mainloop()
        return is_rerun

    def add_a_book(self):
        root = Tk()
        # is_rerun = True
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def previous_menu():
            nonlocal root
            root.destroy()

        def add_library_button():
            nonlocal root  # , is_rerun
            nameOfLibraryToBeAdd = libname.get()
            if nameOfLibraryToBeAdd.endswith(" "):
                nameOfLibraryToBeAdd = nameOfLibraryToBeAdd.lower()
                nameOfLibraryToBeAdd = nameOfLibraryToBeAdd.replace(' ', '')
            if nameOfLibraryToBeAdd.find("Library") or nameOfLibraryToBeAdd.find("library"):
                nameOfLibraryToBeAdd = nameOfLibraryToBeAdd.replace("Library", "")
                nameOfLibraryToBeAdd = nameOfLibraryToBeAdd.replace("library", "")

            if nameOfLibraryToBeAdd.startswith(' ') or nameOfLibraryToBeAdd == '':
                mess.showerror(title='Null value Found', message='Sorry Invalid Input Found')
                libname.delete(0, END)
            else:
                nameOfLibraryToBeAdd = nameOfLibraryToBeAdd + " Library"
                if os.path.isdir(f"Library Management/{nameOfLibraryToBeAdd}") is False:
                    add_lib_bool = mess.askokcancel(title='Confirmation Message', message=f'Do you wan\'t to add {nameOfLibraryToBeAdd}?')
                    if add_lib_bool:
                        os.makedirs(f"Library Management/{nameOfLibraryToBeAdd}")
                        root.destroy()
                    else:
                        libname.delete(0, END)

                else:
                    mess.showerror(title='Library already exist', message=f'{nameOfLibraryToBeAdd} is already there')
                    libname.delete(0, END)


        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Label
        self.what_to_do = Label(root, text=f'(#) Name of Library',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=350, y=150)

        # Entry
        libname = Entry(borderwidth=2, background='#ffffe6',fg='blue')
        libname.focus()
        libname.place(x=550 ,y=150)

        # Button
        add_button = Button(text='Add library', bg='#4dff4d', padx=40, borderwidth=2, activeforeground='black',
                            activebackground='#00e600', foreground='black', command=add_library_button)
        add_button.place(x=340, y=250)

        preview_button = Button(text='Previous Menu', bg='#1a53ff', padx=40, borderwidth=2, activeforeground='white',
                                activebackground='#0000e6', foreground='white', command=previous_menu)
        preview_button.place(x=600, y=250)

        root.mainloop()

    def del_a_library(self):
        root = Tk()
        # is_rerun = True
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def exit_command():
            nonlocal root#, is_rerun
            root.destroy()
            # is_rerun = False

        def del_command():
            nonlocal root#, is_rerun
            if str(all_library_list_box.curselection()) == '()':
                mess.showwarning(title='Null Selection', message='You haven\'t selected any library')
            else:
                index_starting_from_zero = int((str(all_library_list_box.curselection())).split('(')[1].split(',')[0])
                bool_con = mess.askokcancel(title='Delete confirmation', message='Do you wan\'t to remove this Library')
                if bool_con:
                    shutil.rmtree(f"{os.getcwd()}/Library Management/{self.libName[index_starting_from_zero]}")
                root.destroy()
            # is_rerun = False

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Listbox and Scrollbar
        scroll_bar = Scrollbar(root, width=0)
        all_library_list_box = Listbox(root, selectbackground='red', borderwidth=0, width=48, activestyle='underline',selectforeground='white')

        for num, dir in enumerate(self.libName):
            all_library_list_box.insert(0, f'{dir}')
        self.libName.reverse()


        all_library_list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=all_library_list_box.yview)
        all_library_list_box.place(x=380, y=100)
        scroll_bar.place(x=765, y=100, height=182, width=12)

        # Label
        self.what_to_do = Label(root, text=f'All Libraries are listed below, select library you want to delete :-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=330, y=70)

        # Button
        del_button = Button(text='Delete library', bg='#ff4d4d', padx=40, borderwidth=2, activeforeground='white',
                             activebackground='#ff0000', command=del_command, foreground='white')
        del_button.place(x=340, y=300)


        preview_button = Button(text='Previous Menu', bg='#1a53ff', padx=40, borderwidth=2,activeforeground='white',
                                activebackground='#0000e6', command=exit_command , foreground='white')
        preview_button.place(x=600, y=300)

        root.mainloop()

    def manage_library(self):
        root = Tk()
        is_stop = None
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def exit_command():
            nonlocal root, is_stop
            root.destroy()
            is_stop = True

        def BitePlayWithTxtFile(pathOfTxt, isTxtToByte):
            dataInsideFile = None
            writeToFileIs = ' '

            def StrToByte():
                nonlocal writeToFileIs
                res = ''.join(format(ord(i), '08b') for i in dataInsideFile)
                res = str(res)
                writeToFileIs = res

            def BytoToString():
                nonlocal writeToFileIs
                split_strings = []
                n = 8
                for index in range(0, len(dataInsideFile), n):
                    split_strings.append(dataInsideFile[index: index + n])

                temp = " ".join(split_strings)

                a_binary_string = temp

                binary_values = a_binary_string.split()

                ascii_string = ""
                for binary_value in binary_values:
                    an_integer = int(binary_value, 2)
                    ascii_character = chr(an_integer)
                    ascii_string += ascii_character

                writeToFileIs = ascii_string

            def readData():
                nonlocal dataInsideFile
                with open(pathOfTxt, "r") as read:
                    dataInsideFile = read.read()

            def writeToFileFunction():
                with open(pathOfTxt, "w+") as write:
                    write.write(writeToFileIs)

            if isTxtToByte:
                readData()
                StrToByte()
                writeToFileFunction()
            else:
                readData()
                BytoToString()
                writeToFileFunction()

        def textOfTxtToDist(path):
            listOfBooks = []
            listOfIssuer = []
            distOfBookAndIssuer = {}
            # path = f"Library Management/mhhvvjh Library/Library Books Info.txt"
            try:
                BitePlayWithTxtFile(path, False)
                with open(path, "rt") as f:
                    allInfoInList = f.readlines()
                    for i in range(len(allInfoInList)):
                        if allInfoInList[i].startswith("Book is: "):
                            allInfoInList[i] = allInfoInList[i].replace(str("\n"), '')
                            allInfoInList[i] = allInfoInList[i].replace(str("Book is: "), '')
                            listOfBooks.append(allInfoInList[i])

                        elif allInfoInList[i].startswith("Issued by: "):
                            allInfoInList[i] = allInfoInList[i].replace(str("\n"), '')
                            allInfoInList[i] = allInfoInList[i].replace(str("Issued by: "), '')
                            listOfIssuer.append(allInfoInList[i])
                    for i in range(len(listOfBooks)):
                        distOfBookAndIssuer[listOfBooks[i]] = listOfIssuer[i]
            except:
                pass
            else:
                BitePlayWithTxtFile(path, True)

            return listOfBooks, listOfIssuer, distOfBookAndIssuer

        def manage_command():
            nonlocal root  # , is_rerun
            if str(all_library_list_box.curselection()) == '()':
                mess.showwarning(title='Null Selection', message='You haven\'t selected any library')
            else:
                manageLib_index_from_0 = int((str(all_library_list_box.curselection())).split('(')[1].split(',')[0])
                sel_lib_to_manage_name = self.libName[manageLib_index_from_0]

                path = f"Library Management/{self.libName[manageLib_index_from_0]}/Library Books Info.txt"
                nameOfLib = self.libName[manageLib_index_from_0]


                # path = f"Library Management/{nameOfLib}/Books.txt"
                # BitePlayWithTxtFile(path, False)


                if os.path.exists(path):
                    listOfBooks, listOfIssuer, distOfIssuerAndBook = textOfTxtToDist(path)
                    root.destroy()
                    obj1 = Library(nameOfLib, True, listOfBooks, distOfIssuerAndBook)
                    obj1.option_menu()
                else:
                    root.destroy()
                    option_of_how_to_add_book = self.book_selection()
                    if option_of_how_to_add_book == 1:
                        nullDist = {}
                        obj2 = Library(library_name=nameOfLib, is_by_list=False, list_of_books=self.defaultListOfBooks,
                                       dist=nullDist)
                        obj2.option_menu()
                    elif option_of_how_to_add_book == 2:
                        path = f"Library Management/{nameOfLib}/Books.txt"
                        if os.path.exists(path):
                            # self.BitePlayWithTxtFile(path,False)
                            try:
                                with open(path, "rt") as f:
                                    allInfoInList = f.readlines()
                                    for i in range(len(allInfoInList)):
                                        if allInfoInList[i].endswith("\n"):
                                            allInfoInList[i] = allInfoInList[i].replace(str("\n"), '')

                                os.renames(f"Library Management/{nameOfLib}/Books.txt",
                                           f"Library Management/{nameOfLib}/Books_bak.txt")
                                obj3 = Library(nameOfLib, False, allInfoInList, {})
                                obj3.option_menu()



                            except FileNotFoundError:
                                mess.showerror(title='File Not Found', message='Something Wrong with the file please read the Rules to make the Books.txt')
                        else:
                            path = os.getcwd()+f"/Library Management/{nameOfLib}/Books.txt"
                            mess.showerror(title='File Not Found', message=f'There isn\'t any Books.txt File\n\n'
                                                                           f'Location :-\n'
                                                                           f'{path}\n\n'
                                                                           f'If you wan\'t to use this option please read about it.')



                    elif option_of_how_to_add_book == 3:
                        while True:
                            is_stop_rules_section = self.rules_for_creating_file()
                            if is_stop_rules_section:
                                break



        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Listbox and Scrollbar
        scroll_bar = Scrollbar(root, width=0)
        all_library_list_box = Listbox(root, selectbackground='red', borderwidth=0, width=48, activestyle='underline',
                                       selectforeground='white')

        for num, dir in enumerate(self.libName):
            all_library_list_box.insert(0, f'{dir}')
        self.libName.reverse()

        all_library_list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=all_library_list_box.yview)
        all_library_list_box.place(x=380, y=100)
        scroll_bar.place(x=765, y=100, height=182, width=12)

        # Label
        self.what_to_do = Label(root, text=f'All Libraries are listed below, select library you want to Manage :-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=330, y=70)

        # Button
        manage_button = Button(text='Manage library', bg='#00ff00', padx=40, borderwidth=2, activeforeground='#00001a',
                            activebackground='#33cc33', command=manage_command, foreground='#00001a')
        manage_button.place(x=340, y=300)

        preview_button = Button(text='Previous Menu', bg='#1a53ff', padx=40, borderwidth=2, activeforeground='white',
                                activebackground='#0000e6', command=exit_command, foreground='white')
        preview_button.place(x=600, y=300)

        root.mainloop()
        return is_stop

    def book_selection(self):
        selection_of_main_menu = None
        root = Tk()
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def submit():
            nonlocal selection_of_main_menu
            nonlocal root
            if v1.get() == 0:
                mess.showerror(title='Null Selection', message='Please select any one option.')
            elif v1.get() == 1:
                root.destroy()
                selection_of_main_menu = 1
            elif v1.get() == 2:
                root.destroy()
                selection_of_main_menu = 2
            elif v1.get() == 3:
                root.destroy()
                selection_of_main_menu = 3

        def previous_menu_button():
            nonlocal selection_of_main_menu
            nonlocal root
            root.destroy()
            selection_of_main_menu = 4

        # Heading Label

        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Label
        self.what_to_do = Label(root, text='Options for Choosing books are given below',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=390, y=70)

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Radiobutton
        v1 = IntVar()
        Radiobutton(root, text='Defaults Books (for testing purpose)', value=1, variable=v1, bg=self.background, fg='#000099',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(x=390, y=110)
        Radiobutton(root, text='Import Books from File', value=2, variable=v1, bg=self.background, fg='#000099',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(x=390, y=150)
        Radiobutton(root, text='Rules for creating files with book\'s name', value=3, variable=v1, bg=self.background, fg='#000099',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(x=390, y=190)

        # Button
        submit = Button(text='Submit', bg='#66d9ff', padx=30, borderwidth=2, highlightbackground='black',
                        activebackground='#1a8cff', command=submit)
        submit.place(x=410, y=250)

        previous_menu_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=previous_menu_button, width=4, foreground='white', activeforeground='white')
        previous_menu_button.place(x=610, y=250)
        root.mainloop()
        return selection_of_main_menu

    def rules_for_creating_file(self):
        root = Tk()
        is_stop = False
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def previous_menu_command():
            nonlocal is_stop
            nonlocal root
            root.destroy()
            is_stop = True

        def prevent_from_editing(event):
            nonlocal root
            mess.showwarning(title='Restricted Edit', message='You can\'t edit message box')
            info_how_program_run.config(state=DISABLED)
            info_how_program_run.unbind('<Button-1>')

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Textbox and Scrollbar
        scroll_bar = Scrollbar(root, width=0)
        info_how_program_run = Text(root, borderwidth=0, width=47, height=10.5, foreground='#404040')
        info_how_program_run.insert(END, self.how_this_program_work_string)
        info_how_program_run.bind('<Button-1>', prevent_from_editing)

        info_how_program_run.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=info_how_program_run.yview)
        info_how_program_run.place(x=380, y=100)
        scroll_bar.place(x=765, y=100, height=183, width=12)

        # Label
        self.what_to_do = Label(root, text=f'Rules for creating File are :-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=480, y=70)

        # Button
        preview_button = Button(text='Previous Menu', bg='#1a53ff', padx=40, borderwidth=2,
                                activeforeground='white',
                                activebackground='#0000e6', foreground='white', command=previous_menu_command)
        preview_button.place(x=470, y=300)

        root.mainloop()
        return is_stop

    def file_missing(self):
        root = Tk()
        is_rerun = True
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def exit_command():
            nonlocal root, is_rerun
            root.destroy()
            is_rerun = False

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Label
        self.what_to_do = Label(root, text=f'You wont have essential component\'s for proper execution of program please download it from official github repo',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=420, y=70)

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_command)
        exit_button.place(x=480, y=300)
        root.mainloop()


class Library:
    nameOfLibrary = None
    listOfBooksInLibrary = []
    dist_info_of_booked_issued = {}

    def __init__(self, library_name, is_by_list, list_of_books, dist):
        self.nameOfLibrary = library_name
        self.listOfBooksInLibrary = list_of_books

        if is_by_list:
            self.dist_info_of_booked_issued = dist
        else:
            for i in range(len(self.listOfBooksInLibrary)):
                self.dist_info_of_booked_issued[self.listOfBooksInLibrary[i]] = "None"

        self.saveIssuerInfo()

    def saveIssuerInfo(self):
        self.ritIssuerInfo2file("Library Management", self.nameOfLibrary, "Library Books Info.txt")

    def ritIssuerInfo2file(self, dirName, libName, fileName):
        dirName = dirName+"/"+libName
        if os.path.isdir(f"{dirName}") is False:
            os.makedirs(dirName)
        if os.path.isfile(f"{dirName}/{fileName}") == False:
            f = open(os.path.join(dirName, fileName), 'w+')
            f.close()

        with open(f"{dirName}/{fileName}", "w+") as f:
            for books, issuer in self.dist_info_of_booked_issued.items():
                str = f"Book is: {books}\nIssued by: {issuer}\n\n"
                f.write(str)

        path = f"{dirName}/{fileName}"
        self.BitePlayWithTxtFile(path,True)

    def BitePlayWithTxtFile(self, pathOfTxt, isTxtToByte):
        dataInsideFile = None
        writeToFileIs = ' '

        def StrToByte():
            nonlocal writeToFileIs
            res = ''.join(format(ord(i), '08b') for i in dataInsideFile)
            res = str(res)
            writeToFileIs = res

        def BytoToString():
            nonlocal writeToFileIs
            split_strings = []
            n = 8
            for index in range(0, len(dataInsideFile), n):
                split_strings.append(dataInsideFile[index: index + n])

            temp = " ".join(split_strings)

            a_binary_string = temp

            binary_values = a_binary_string.split()

            ascii_string = ""
            for binary_value in binary_values:
                an_integer = int(binary_value, 2)
                ascii_character = chr(an_integer)
                ascii_string += ascii_character

            writeToFileIs = ascii_string

        def readData():
            nonlocal dataInsideFile
            with open(pathOfTxt, "r") as read:
                dataInsideFile = read.read()

        def writeToFileFunction():
            with open(pathOfTxt, "w+") as write:
                write.write(writeToFileIs)

        if isTxtToByte:
            readData()
            StrToByte()
            writeToFileFunction()
        else:
            readData()
            BytoToString()
            writeToFileFunction()

    def option_menu(self):
        root = Tk()

        def previous_menu_command():
            nonlocal root
            root.destroy()

        def close_button_pressed():
            self.saveIssuerInfo()
            root.destroy()

        def submit_button():
            nonlocal root
            option_menu_selection = v1.get()
            if option_menu_selection == 1:
                root.destroy()
                self.display_all_books()
                self.option_menu()

            elif option_menu_selection == 2:
                root.destroy()
                self.display_issued_books()
                self.option_menu()

            elif option_menu_selection == 3:
                root.destroy()
                self.function_of_issue_books()
                self.option_menu()

            elif option_menu_selection == 4:
                root.destroy()
                self.return_a_book()
                self.option_menu()

            elif option_menu_selection == 5:
                root.destroy()
                self.add_a_book()
                self.option_menu()

            if option_menu_selection == 6:
                root.destroy()
                self.remove_a_book()
                self.option_menu()

            if option_menu_selection == 7:
                self.export_info()

            if option_menu_selection == 8:
                self.del_export_info()

            # self.optionMenu()

        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title(f'{self.nameOfLibrary} -by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Label
        self.what_to_do = Label(root, text=f'Viewing Related Work',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=340, y=100)

        self.what_to_do = Label(root, text=f'Student Related Work',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=600, y=100)

        self.what_to_do = Label(root, text=f'Staff Related Work',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=340, y=200)

        self.what_to_do = Label(root, text=f'Files Export',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=600, y=200)

        # Radiobutton
        v1 = IntVar()
        Radiobutton(root, text='All Book Names', value=1, variable=v1, bg=self.background, fg='blue',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(
            x=330, y=130)
        Radiobutton(root, text='Issued Book\'s', value=2, variable=v1, bg=self.background, fg='blue',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(
            x=330, y=160)
        Radiobutton(root, text='Issue Book\'s', value=3, variable=v1, bg=self.background, fg='blue',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(
            x=590, y=130)
        Radiobutton(root, text='Return Book\'s', value=4, variable=v1, bg=self.background, fg='blue',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(
            x=590, y=160)
        Radiobutton(root, text='Add Book', value=5, variable=v1, bg=self.background, fg='blue',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(
            x=330, y=230)
        Radiobutton(root, text='Delete Book\'s', value=6, variable=v1, bg=self.background, fg='blue',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(
            x=330, y=260)
        Radiobutton(root, text='Export Information\'s', value=7, variable=v1, bg=self.background, fg='blue',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(
            x=590, y=230)
        Radiobutton(root, text='Delete Export\'s', value=8, variable=v1, bg=self.background, fg='blue',
                    borderwidth=2, activebackground='#ffffb3', activeforeground='blue', highlightthickness=0).place(
            x=590, y=260)

        # Button
        preview_button = Button(text='Previous Menu', bg='#1a53ff', padx=40, borderwidth=2, activeforeground='white',
                                activebackground='#0000e6', foreground='white', command=previous_menu_command, width=8)
        preview_button.place(x=610, y=300)

        submit_button = Button(text='Submit', bg='#4dff4d', padx=40, borderwidth=2, activeforeground='black',
                               activebackground='#00e600', foreground='black', command=submit_button)
        submit_button.place(x=340, y=300)

        root.protocol('WM_DELETE_WINDOW', close_button_pressed)
        root.mainloop()

    def display_all_books(self):
        root = Tk()
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def close_button_pressed():
            self.saveIssuerInfo()
            root.destroy()
            return '1'

        def previous_menu():
            nonlocal root
            self.saveIssuerInfo()
            root.destroy()

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Listbox and Scrollbar
        scroll_bar = Scrollbar(root, width=0)
        all_library_list_box = Listbox(root, selectbackground=self.background, borderwidth=0, width=48,
                                       activestyle='none', fg='#3333ff', selectforeground='#3333ff')
        for count, self.books in enumerate(self.dist_info_of_booked_issued):
            all_library_list_box.insert(END, f'{count + 1}) {self.books}')

        all_library_list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=all_library_list_box.yview)
        all_library_list_box.place(x=380, y=100)
        scroll_bar.place(x=765, y=100, height=182, width=12)

        # Label
        self.what_to_do = Label(root,
                                text=f'Total Number of Books in Library are: {len(self.dist_info_of_booked_issued)} :-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=400, y=70)

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2,
                             highlightbackground='black',
                             activebackground='#ff0000', command=previous_menu)
        exit_button.place(x=480, y=300)

        root.protocol('WM_DELETE_WINDOW', close_button_pressed)
        root.mainloop()

    def add_a_book(self):
        root = Tk()
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def close_button_pressed():
            self.saveIssuerInfo()
            root.destroy()

        def previous_menu():
            nonlocal root
            root.destroy()

        def add_book_button():
            nonlocal root
            book_name_is = book_name.get()
            if len(book_name_is) == 0 or book_name_is.startswith(' '):
                mess.showerror(title='Null Value', message='Please type name of the book')
            else:
                book_name_is = book_name_is.capitalize()
                book_author = author_name.get()
                book_author.capitalize()

                if len(book_author) == 0 or book_author.startswith(' '):
                    book_detail_selected = book_name_is

                    if book_detail_selected in self.dist_info_of_booked_issued:
                        mess.showerror(title='Book already there', message='This book name is already there in our library')
                        author_name.delete(0, END)
                        book_name.delete(0, END)
                        book_name.focus()
                    else:
                        is_ok = mess.askokcancel(title='Confirmation message', message=f'Do you wan\'t to add\n\n'
    
                                                                                       f'1) Book name is :-'
                                                                                       f'\n{book_detail_selected}')

                        if is_ok:
                            self.dist_info_of_booked_issued[book_detail_selected] = "None"
                            self.listOfBooksInLibrary.append(book_detail_selected)
                            root.destroy()
                else:
                    book_detail_selected = book_name_is + " by " + book_author

                    if book_detail_selected in self.dist_info_of_booked_issued:
                        mess.showerror(title='Book already there', message='This book name is already there in our library')
                        author_name.delete(0, END)
                        book_name.delete(0, END)
                        book_name.focus()

                    else:
                        is_ok = mess.askokcancel(title='Confirmation message', message=f'Do you wan\'t to add :-\n\n'
    
                                                                                       f'1) Book name is :-\n'
                                                                                       f'{book_detail_selected}\n\n'
                                                                                       f''
                                                                                       f'2) Book author is :-\n'
                                                                                       f'{book_author}')
                        if is_ok:
                            self.dist_info_of_booked_issued[book_detail_selected] = "None"
                            self.listOfBooksInLibrary.append(book_detail_selected)
                            root.destroy()

                self.saveIssuerInfo()

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Label
        self.detail_to_add_book = Label(root, text=f'Details to add book to library :-',
                                        font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.detail_to_add_book.place(x=470, y=70)

        self.first_name_of_issuer = Label(root, text=f'(#) Name of Book',
                                          font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.first_name_of_issuer.place(x=380, y=150)

        self.last_name_of_issuer = Label(root, text=f'(#) Author (Optional)',
                                         font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.last_name_of_issuer.place(x=380, y=200)

        # Entry
        book_name = Entry(borderwidth=2, background='#ffffe6', fg='blue')
        book_name.focus()
        book_name.place(x=580, y=150)

        author_name = Entry(borderwidth=2, background='#ffffe6', fg='blue')
        author_name.place(x=580, y=200)

        # Button
        add_book = Button(text='Add Book', bg='#4dff4d', padx=40, borderwidth=2, activeforeground='black',
                          activebackground='#00e600', foreground='black', command=add_book_button)
        add_book.place(x=340, y=280)

        previous_button = Button(text='Previous Menu', bg='#1a53ff', padx=40, borderwidth=2, activeforeground='white',
                                 activebackground='#0000e6', foreground='white', command=previous_menu)
        previous_button.place(x=600, y=280)

        root.protocol('WM_DELETE_WINDOW', close_button_pressed)
        root.mainloop()

    def remove_a_book(self):
        del_book_name = None
        book_index_is = None

        root = Tk()
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def close_button_pressed():
            self.saveIssuerInfo()
            root.destroy()

        def previous_menu_button():
            nonlocal root
            self.saveIssuerInfo()
            root.destroy()

        def rem_book_button():
            nonlocal root, del_book_name, book_index_is
            if str(all_library_list_box.curselection()) == '()':
                mess.showerror(title='Null Selection', message='Please select one parameter')
            else:
                del_book_index = int((str(all_library_list_box.curselection())).split('(')[1].split(',')[0])
                only_sel_book_name = str(str(all_library_list_box.get(del_book_index)).split(': ')[1])
                if self.dist_info_of_booked_issued[only_sel_book_name] == 'None':
                    con_bool = mess.askokcancel(title='Confirmation', message=f'Are you sure to remove :-\n'
                                                                              f'{only_sel_book_name}')
                    if con_bool:
                        # root.destroy()
                        # del_book_name = sel_book_name
                        book_index_is = del_book_index

                        for num, (book, issueBy) in enumerate(self.dist_info_of_booked_issued.items()):
                            if num == book_index_is:
                                del_book_name = book

                        if self.dist_info_of_booked_issued[only_sel_book_name] == "None":
                            del self.dist_info_of_booked_issued[only_sel_book_name]
                            # self.saveIssuerInfo()

                        else:
                            mess.showerror(title='Already Issued warning',
                                           message=f"{only_sel_book_name} can't be removed because it is issued by: "
                                                   f"{self.dist_info_of_booked_issued[only_sel_book_name]}")

                        root.destroy()
                else:
                    mess.showerror(title='Already Issued warning',
                                   message=f"{only_sel_book_name} can't be removed because it is issued by:"
                                           f" {self.dist_info_of_booked_issued[only_sel_book_name]}")
                    root.destroy()

                self.saveIssuerInfo()

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Listbox and Scrollbar
        scroll_bar = Scrollbar(root, width=0)
        all_library_list_box = Listbox(root, selectbackground='red', borderwidth=0, width=48,
                                       fg='#3333ff', selectforeground='white', selectborderwidth=0)

        for count, self.books in enumerate(self.dist_info_of_booked_issued):
            all_library_list_box.insert(END, f"Books is: {self.books}")

        all_library_list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=all_library_list_box.yview)
        all_library_list_box.place(x=380, y=100)
        scroll_bar.place(x=765, y=100, height=182, width=12)

        # Label
        self.what_to_do = Label(root,
                                text=f'Total Number of Books in Library are: {len(self.dist_info_of_booked_issued)} :-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=400, y=70)

        # Button
        del_button = Button(text='Delete Book', bg='#4dff4d', padx=40, borderwidth=2, activeforeground='black',
                            activebackground='#00e600', foreground='black', command=rem_book_button)
        del_button.place(x=340, y=310)

        preview_button = Button(text='Previous Menu', bg='#1a53ff', padx=40, borderwidth=2, activeforeground='white',
                                activebackground='#0000e6', foreground='white', command=previous_menu_button)
        preview_button.place(x=600, y=310)

        root.protocol('WM_DELETE_WINDOW', close_button_pressed)
        root.mainloop()

    def function_of_issue_books(self):
        del_book_name_is = None
        book_index_is = None

        root = Tk()
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def close_button_pressed():
            self.saveIssuerInfo()
            root.destroy()

        def issue_book_info_taking(issue_book_name):
            root = Tk()
            self.background = 'white'
            root.geometry('850x400')
            root.resizable(False, False)
            root.title('Library Management System by Prashant Singh')
            root.config(background=self.background, borderwidth=30)

            def previous_menu_inner_page():
                nonlocal root
                root.destroy()

            def issue_a_book_button_function():
                nonlocal root
                first_name = str(entry_first_name_of_issuer.get())
                second_name = str(entry_second_name_of_issuer.get())

                if len(first_name) != 0 and not entry_first_name_of_issuer.get().startswith(' ') != False:
                    first_name = first_name.capitalize()
                    second_name = second_name.capitalize()
                    if len(second_name) == 0 or second_name.startswith(' '):
                        full_name = first_name

                        if self.dist_info_of_booked_issued[issue_book_name] != 'None':
                            mess.showerror(title='Book already issued error',
                                           message='This book is already issued in our library')
                            entry_first_name_of_issuer.delete(0, END)
                            entry_second_name_of_issuer.delete(0, END)
                            entry_first_name_of_issuer.focus()
                        else:
                            is_ok = mess.askokcancel(title='Confirmation message', message=f'Please check info:-\n\n'
                                                                                           f''
                                                                                           f'1) Name of Issuer :-\n'
                                                                                           f'{full_name}\n\n'
                                                                                           f''
                                                                                           f'2) Book name is :-\n'
                                                                                           f'{issue_book_name}')

                            if is_ok:
                                self.dist_info_of_booked_issued[issue_book_name] = full_name
                                root.destroy()
                    else:
                        full_name = first_name + " " + second_name

                        if self.dist_info_of_booked_issued[issue_book_name] != 'None':
                            mess.showerror(title='Book already issued error',
                                           message='This book is already issued in our library')
                            entry_first_name_of_issuer.delete(0, END)
                            entry_second_name_of_issuer.delete(0, END)
                            entry_first_name_of_issuer.focus()
                        else:
                            is_ok = mess.askokcancel(title='Confirmation message', message=f'Please check info:-\n\n'
                                                                                           f''
                                                                                           f'1) Name of Issuer :-\n'
                                                                                           f'{full_name}\n\n'
                                                                                           f''
                                                                                           f'2) Book name is :-\n'
                                                                                           f'{issue_book_name}')

                            if is_ok:
                                self.dist_info_of_booked_issued[issue_book_name] = full_name
                                root.destroy()
                else:
                    mess.showerror(title='Invalid name', message='First name is mandatory')

                self.saveIssuerInfo()

            # image
            self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
            self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
            self.image.place(x=0, y=30)

            # Heading Label
            self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                            background=self.background)
            self.L1.place(x=380, y=0)

            # Label
            self.detail_to_add_book = Label(root, text=f'Details of issuer :-',
                                            font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
            self.detail_to_add_book.place(x=470, y=70)

            self.book_detail = Label(root, text=f'Book selected: {issue_book_name}',
                                     font=('arial', 8,), justify=RIGHT, bg=self.background)
            self.book_detail.place(x=370, y=110)

            self.first_name_of_issuer = Label(root, text=f'(#) First name of Issuer',
                                              font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
            self.first_name_of_issuer.place(x=380, y=150)

            self.last_name_of_issuer = Label(root, text=f'(#) Last name (Optional)',
                                             font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
            self.last_name_of_issuer.place(x=380, y=200)

            # Entry
            entry_first_name_of_issuer = Entry(borderwidth=2, background='#ffffe6', fg='blue')
            entry_first_name_of_issuer.focus()
            entry_first_name_of_issuer.place(x=580, y=150)

            entry_second_name_of_issuer = Entry(borderwidth=2, background='#ffffe6', fg='blue')
            entry_second_name_of_issuer.place(x=580, y=200)

            # Button
            button_issue_a_book = Button(text='Issue Book', bg='#4dff4d', padx=40, borderwidth=2,
                                         activeforeground='black',
                                         activebackground='#00e600', foreground='black',
                                         command=issue_a_book_button_function)
            button_issue_a_book.place(x=340, y=280)

            main_menu_button = Button(text='Home Menu', bg='#1a53ff', padx=40, borderwidth=2,
                                      activeforeground='white',
                                      activebackground='#0000e6', foreground='white', command=previous_menu_inner_page)
            main_menu_button.place(x=600, y=280)

            root.protocol('WM_DELETE_WINDOW', close_button_pressed)
            root.mainloop()

        def previous_menu_button():
            nonlocal root
            root.destroy()

        def issue_book_button():
            nonlocal root, del_book_name_is, book_index_is
            if str(all_library_list_box.curselection()) == '()':
                mess.showerror(title='Null selection', message='You haven\'t selected anything')
            else:
                issue_book_index = int((str(all_library_list_box.curselection())).split('(')[1].split(',')[0])
                sel_book_name = str(str(all_library_list_box.get(issue_book_index)).split(': ')[1])

                if self.dist_info_of_booked_issued[sel_book_name] == 'None':
                    con_bool = mess.askokcancel(title='Confirmation', message=f'Are you sure to issue :-\n'
                                                                              f'{sel_book_name}')
                    if con_bool:
                        root.destroy()
                        issue_book_info_taking(sel_book_name)
                else:
                    mess.showerror(title='Already Issued', message='This book you are trying to access is already issued')

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Listbox and Scrollbar
        scroll_bar = Scrollbar(root, width=0)
        all_library_list_box = Listbox(root, selectbackground='red', borderwidth=0, width=48,
                                       fg='#3333ff', selectforeground='white', selectborderwidth=0)

        for self.books, issued_by in self.dist_info_of_booked_issued.items():
            if issued_by.find('None') == 0:  # change to -1 for issued book info
                all_library_list_box.insert(END, f"Books is: {self.books}")

        all_library_list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=all_library_list_box.yview)
        all_library_list_box.place(x=380, y=100)
        scroll_bar.place(x=765, y=100, height=182, width=12)

        # Label
        self.what_to_do = Label(root,
                                text=f'Select a book you want to issue :-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=400, y=70)

        # Button
        issue_button = Button(text='Issue Book', bg='#4dff4d', padx=40, borderwidth=2, activeforeground='black',
                              activebackground='#00e600', foreground='black', command=issue_book_button)
        issue_button.place(x=340, y=310)

        preview_button = Button(text='Previous Menu', bg='#1a53ff', padx=40, borderwidth=2, activeforeground='white',
                                activebackground='#0000e6', foreground='white', command=previous_menu_button)
        preview_button.place(x=600, y=310)

        root.protocol('WM_DELETE_WINDOW', close_button_pressed)
        root.mainloop()

    def display_issued_books(self):
        root = Tk()
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def close_button_pressed():
            self.saveIssuerInfo()
            root.destroy()

        def previous_menu():
            nonlocal root
            self.saveIssuerInfo()
            root.destroy()

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Listbox and Scrollbar
        scroll_bar = Scrollbar(root, width=0)
        all_library_list_box = Listbox(root, selectbackground=self.background, borderwidth=0, width=48,
                                       activestyle='none', fg='#3333ff', selectforeground='#3333ff')
        issuer_info_dist = {book: names for (book, names) in self.dist_info_of_booked_issued.items() if
                            self.dist_info_of_booked_issued[book] != 'None'}
        for count, (book, name) in enumerate(issuer_info_dist.items()):
            all_library_list_box.insert(END, f'{count + 1}) Book name: {book}')
            all_library_list_box.insert(END, f'Issuer name: {name}')
            all_library_list_box.insert(END, f'')

        all_library_list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=all_library_list_box.yview)
        all_library_list_box.place(x=380, y=100)
        scroll_bar.place(x=765, y=100, height=182, width=12)

        # Label
        self.what_to_do = Label(root,
                                text=f'Total Number Issued Books Library are: {len(issuer_info_dist)} :-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=400, y=70)

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2,
                             highlightbackground='black',
                             activebackground='#ff0000', command=previous_menu)
        exit_button.place(x=480, y=300)

        root.protocol('WM_DELETE_WINDOW', close_button_pressed)
        root.mainloop()

    def return_a_book(self):

        def close_button_pressed():
            self.saveIssuerInfo()
            root.destroy()

        root = Tk()
        self.background = 'white'
        root.geometry('850x400')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=self.background, borderwidth=30)

        def previous_menu():
            nonlocal root
            self.saveIssuerInfo()
            root.destroy()

        def return_book():
            nonlocal root
            if str(all_library_list_box.curselection()) == '()':
                mess.showerror(title='Null selection', message='You haven\'t selected anything')
            else:
                return_book_index = int((str(all_library_list_box.curselection())).split('(')[1].split(',')[0])
                return_book_name = str(str(all_library_list_box.get(return_book_index)).split(': ')[1])
                is_return = mess.askyesno(title='Confirmation', message=f'Do you wan\'t to return {return_book_name}')
                if is_return:
                    self.dist_info_of_booked_issued[return_book_name] = 'None'
                    root.destroy()
                self.saveIssuerInfo()

        # image
        self.lib_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/library.jpg"))
        self.image = Label(root, width=300, height=300, image=self.lib_image, borderwidth=0)
        self.image.place(x=0, y=30)

        # Heading Label
        self.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=self.background)
        self.L1.place(x=380, y=0)

        # Listbox and Scrollbar
        scroll_bar = Scrollbar(root, width=0)
        all_library_list_box = Listbox(root, selectbackground='red', borderwidth=0, width=48,
                                       fg='#3333ff', selectforeground='white', selectborderwidth=0)
        issuer_info_dist = {book: names for (book, names) in self.dist_info_of_booked_issued.items() if
                            self.dist_info_of_booked_issued[book] != 'None'}
        for count, (book, name) in enumerate(issuer_info_dist.items()):
            all_library_list_box.insert(END, f'{count + 1}) Book name: {book}')

        all_library_list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=all_library_list_box.yview)
        all_library_list_box.place(x=380, y=100)
        scroll_bar.place(x=765, y=100, height=182, width=12)

        # Label
        self.what_to_do = Label(root,
                                text=f'Total Number Issued Books Library are: {len(issuer_info_dist)} :-',
                                font=('arial', 12, 'bold'), justify=RIGHT, bg=self.background)
        self.what_to_do.place(x=400, y=70)

        # Button
        button_issue_a_book = Button(text='Return Book', bg='#4dff4d', padx=40, borderwidth=2, activeforeground='black',
                                     activebackground='#00e600', foreground='black', command=return_book)

        button_issue_a_book.place(x=340, y=300)

        main_menu_button = Button(text='Home Menu', bg='#1a53ff', padx=40, borderwidth=2,
                                  activeforeground='white',
                                  activebackground='#0000e6', foreground='white', command=previous_menu)
        main_menu_button.place(x=600, y=300)

        root.protocol('WM_DELETE_WINDOW', close_button_pressed)
        root.mainloop()

    def export_info(self):
        path_is = os.getcwd()+f'/Library Management/{self.nameOfLibrary}/Exported Data'
        is_yes = mess.askyesno(title='Confirmation', message='Do you want to export library data in unencrypted Manner\n'
                                                             'path :-\n'
                                                             f'{path_is}')
        if is_yes:
            if os.path.exists(f'Library Management/{self.nameOfLibrary}/Exported Data') == False:
                os.makedirs(f'Library Management/{self.nameOfLibrary}/Exported Data')

            with open(f'Library Management/{self.nameOfLibrary}/Exported Data/1) Exported Book\'s List.txt', 'w') as f:
                f.write(f"{' ' * 26}*---------------------------------------------*\n")
                f.write(f"{' ' * 26}|{f'Total Number of Books in Library are: {len(self.dist_info_of_booked_issued)}':^45}|\n")
                f.write(f"{' ' * 26}*---------------------------------------------*\n\n")
                f.write(f'*' + "-" * 19 + "*" + "-" * 76 + "*\n")
                f.write(f"|{'Book Number':^19}|{str('Book Name'):^76}|\n")
                f.write(f'*' + "-" * 19 + "*" + "-" * 76 + "*\n")
                i = 1
                for count, self.books in enumerate(self.dist_info_of_booked_issued):
                    f.write(f"|{i:^19d}|{self.books:<76s}|\n")
                    i += 1

                f.write(f'*' + "-" * 19 + "*" + "-" * 76 + "*\n")


            totalBooks = 0
            books = []
            issuerInformations = []
            totalIssueBook = 0
            for count, (book, issuerInformation) in enumerate(self.dist_info_of_booked_issued.items()):
                if self.dist_info_of_booked_issued[book] != "None":
                    books.append(book)
                    issuerInformations.append(issuerInformation)
                    totalBooks += 1
            for count in range(totalBooks):
                totalIssueBook += 1


            with open(f'Library Management/{self.nameOfLibrary}/Exported Data/3) Exported Issued Books.txt', 'w') as f1:
                f1.write(f"{' ' * 26}*--------------------------------------*\n")
                f1.write(f"{' ' * 26}|{f'Total number Books issued are: {totalIssueBook}':^38}|\n")
                f1.write(f"{' ' * 26}*--------------------------------------*\n\n")
                f1.write(f'*' + "-" * 70 + "*" + "-" * 25 + "*\n")
                f1.write(f"|{'Book Name':^70}|{str('Issuer Name'):^25}|\n")
                f1.write(f'*' + "-" * 70 + "*" + "-" * 25 + "*\n")
                for count in range(totalBooks):
                    f1.write(f"|{books[count]:^70s}|{issuerInformations[count]:^25s}|\n")
                f1.write(f'*' + "-" * 70 + "*" + "-" * 25 + "*\n")


            with open(f'Library Management/{self.nameOfLibrary}/Exported Data/2) Exported All Books issuer Info.txt', 'w') as f2:
                f2.write(f"{' ' * 28}*-----------------------------------------*\n")
                f2.write(f"{' ' * 28}|{f'Total number Books in library is: {len(self.dist_info_of_booked_issued.items())}':^41}|\n")
                f2.write(f"{' ' * 28}*-----------------------------------------*\n\n")
                f2.write(f'*' + "-" * 70 + "*" + "-" * 25 + "*\n")
                f2.write(f"|{'Book Name':^70}|{str('Issuer Name'):^25}|\n")
                f2.write(f'*' + "-" * 70 + "*" + "-" * 25 + "*\n")
                for count, (book, issueBy) in enumerate(self.dist_info_of_booked_issued.items()):
                    f2.write(f"|{book:<70s}|{issueBy:^25s}|\n")

                f2.write(f'*' + "-" * 70 + "*" + "-" * 25 + "*\n")

    def del_export_info(self):
        if os.path.exists(f'Library Management/{self.nameOfLibrary}/Exported Data'):
            is_yes = mess.askyesno(title='Confirmation', message=f'Do you want to Delete all the exports of {self.nameOfLibrary}')
            if is_yes:
                shutil.rmtree(f'Library Management/{self.nameOfLibrary}/Exported Data')
        else:
            mess.showerror(title='File not Found', message='There are no Exports currently.')


class AskingWhatToDo:
    def __init__(self):
        self.run_next_program = False
        self.programmer_description_string = '''(#)This Program is made on July 2, 2022
by Prashant Ranjan Singh.


(#) This Program is basically an offline
Library Management System


(#) Linkedin Profile of mine :-'''
        self.working_of_program_explain_str = '''
--> It is an Offline Library manager program, which will manage all your
Libraries.

--> By the help of this program you can create as many library as you
want and manage it through this program.

--> All libraries file's are stored in Library Management folder which 
further divided into sub-folders of all library which are managed by this 
program, the data inside will be in binary format so anyone cant read it.
'''
        background = 'white'

        # Screen
        self.screen = Tk()
        self.screen.geometry('600x620')
        self.screen.minsize(600, 620)
        self.screen.maxsize(600, 620)
        self.screen.title('Library Management By Prashant Ranjan Singh')
        self.screen.config(bg=background, padx=50, pady=50)
        self.screen.resizable(False, False)

        # image
        self.password_image = ImageTk.PhotoImage(Image.open("Images (Do not  Rename or edit anything)/Mine_photo.jpg"))
        self.image = Label(width=250, height=250, image=self.password_image, borderwidth=0)

        # Label
        self.text = Label()
        self.about_programmer = Label(text='About Programmer', font=('LatinModernRomanDunhill', 12, 'bold'),
                                      background=background)
        self.text.configure(text=self.programmer_description_string, bg='white', justify=LEFT)
        self.link = Label(text="www.linkedin.com", fg="blue", cursor="hand2", bg=background)
        self.link.bind("<Button-1>", lambda e: self.callback("www.linkedin.com/in/prashant-ranjan-singh-b9b6b9217"))
        self.working_heading = Label(text='Working of Program', font=('LatinModernRomanDunhill', 12, 'bold'),
                                     bg=background)
        self.working_of_program_explain = Label(text=self.working_of_program_explain_str, bg='white', justify=LEFT)

        # Button
        self.exit_button = Button(text='Exit', command=self.exit_button_command, background='red', foreground='white',
                                  activeforeground='black', activebackground='red', borderwidth=6)
        self.continue_button = Button(text='Continue', command=self.continue_button_command, background='blue',
                                      foreground='white',
                                      activeforeground='black', activebackground='blue', borderwidth=6)

        # Create a Label to display the link
        self.image.grid(column=0, row=0)
        self.about_programmer.grid(column=1, row=0, sticky=NE, padx=70)
        self.text.grid(column=1, row=0, sticky=NW, pady=50, padx=10)
        self.link.grid(column=1, row=0, sticky=SW, padx=35, pady=30)
        self.working_heading.grid(column=0, row=1, padx=50, columnspan=2, pady=5)
        self.working_of_program_explain.grid(column=0, row=2, columnspan=3, sticky=W)
        self.exit_button.grid(column=0, row=3, sticky=NW, ipadx=35, pady=0)
        self.continue_button.grid(column=1, row=3, sticky=S, ipadx=35, pady=0, columnspan=3, padx=25)
        self.screen.mainloop()

    @staticmethod
    def callback(url):
        webbrowser.open_new_tab(url)

    def exit_button_command(self):
        self.screen.destroy()

    def continue_button_command(self):
        self.screen.destroy()
        self.run_next_program = True


class Errors:
    def file_missing(cls, url = 'https://github.com/Prashant-ranjan-singh-123/MyAllProgramsInOneRepo/tree/main/4)%20Python%20Language/GUI%20Program/Library%20Management',show_name_of_url='www.github.com'):
        def callback(url):
            webbrowser.open_new_tab(url)

        root = Tk()
        cls.background = 'white'
        root.geometry('500x310')
        root.resizable(False, False)
        root.title('Library Management System by Prashant Singh')
        root.config(background=cls.background, borderwidth=30)

        def exit_command():
            nonlocal root
            root.destroy()
            is_rerun = False

        # Heading Label
        cls.L1 = Label(root, text='Library Management System', font='LatinModernRomanDunhill 20 bold',
                        background=cls.background)
        cls.L1.pack(anchor='center')

        # Label
        cls.error = Label(root, text='Error', foreground='red', font='arial 30 bold', justify=CENTER, background=cls.background)
        cls.error.pack(anchor='center', pady=20)

        cls.what_to_do = Label(root, text=f'You wont have essential component\'s for proper \n'
                                          f'execution of program please download it from \n'
                                          f'official github repository from below link :-',
                                font=('arial', 12, 'bold'), justify=CENTER, bg=cls.background)
        cls.what_to_do.pack()

        cls.link = Label(text=show_name_of_url, fg="blue", cursor="hand2", bg=cls.background,font=('arial', 12, 'bold'))
        cls.link.bind("<Button-1>", lambda e: callback(url))
        cls.link.pack(anchor='center')


        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_command)
        exit_button.place(x=480, y=300)
        root.mainloop()


if __name__ == '__main__':
    current_dir = os.getcwd()
    if os.path.exists('Images (Do not  Rename or edit anything)') and os.path.exists('Images (Do not  Rename or edit anything)/Mine_photo.jpg') and os.path.exists('Images (Do not  Rename or edit anything)/library.jpg'):
        if os.access(current_dir, os.F_OK) and os.access(current_dir, os.R_OK) and os.access(current_dir, os.W_OK):
            ask = AskingWhatToDo()
            if ask.run_next_program:
                l1 = LibraryManagement()
        else:
            mess.showerror(title='Permission Issue', message='You won\'t have reading Reading/Writing Permission.')

    else:
        Errors().file_missing()
