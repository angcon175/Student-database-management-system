from tkinter import*
import tkinter.messagebox
import std_db

class Students:
        def __init__(self,root):
            self.root =root
            self.root.title("Student Database")
            self.root.geometry("1350x750+0+0")
            self.root.config(bg="cadet blue")
            
            StdID = StringVar()
            FirstName = StringVar()
            LastName = StringVar()
            DoB = StringVar()
            Age = StringVar()
            Gender = StringVar()
            Address = StringVar()
            Mobile = StringVar()
            
            #===================================================Function===================================================
            
            def iExit():
                iExit = tkinter.messagebox.askyesno("Students Database Management System","Confirm if you want to exit")
                if iExit > 0:
                    root.destroy()
                return
            
            def clearData():
                self.txtStdID.delete(0,END)
                self.txtfna.delete(0,END)
                self.txtlna.delete(0,END)
                self.txtDoB.delete(0,END)
                self.txtage.delete(0,END)
                self.txtgen.delete(0,END)
                self.txtadd.delete(0,END)
                self.txtMobile.delete(0,END)

            def addData():
                if(len(StdID.get())!=0):
                        std_db.addStdRec(StdID.get(), FirstName.get(),LastName.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                        studentlist.delete(0,END)
                        studentlist.insert(END,(StdID.get(), FirstName.get(),LastName.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))

            def DisplayData():
                studentlist.delete(0,END)
                for row in std_db.viewData():
                        studentlist.insert(END,row,str(""))

            def StudentRec(event):
                    global sd
                    searchStd = studentlist.curselection()[0]
                    sd = studentlist.get(searchStd)
                    
                    self.txtStdID.delete(0,END)
                    self.txtStdID.insert(END,sd[1])
                    self.txtfna.delete(0,END)
                    self.txtfna.insert(END,sd[2])
                    self.txtlna.delete(0,END)
                    self.txtlna.insert(END,sd[3])
                    self.txtDoB.delete(0,END)
                    self.txtDob.insert(END,sd[4])
                    self.txtage.delete(0,END)
                    self.txtage.insert(END,sd[5])
                    self.txtgen.delete(0,END)
                    self.txtgen.insert(END,sd[6])
                    self.txtadd.delete(0,END)
                    self.txtadd.insert(END,sd[7])
                    self.txtMobile.delete(0,END)
                    self.txtMobile.insert(END,sd[8])

            def DeleteDate():
                if(len(StdID.get())!=0):
                        std_db.deleteRec(sd[0])
                        cleardata()
                        DisplayData()

            def searchDatabase():
                    studentlist.delete(0,END)
                    for row in std_db.searchData(StdID.get(),FirstName.get(),LastName.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()):
                            studentlist.insert(END,row,str(""))

            def update():
                    if(len(StdID.get())!=0):
                            std_db.deleteRec(sd[0])
                    if(len(StdID.get())!=0):
                            std_db.addStdRec(StdID.get(),FirstName.get(),LastName.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                            studentlist.delete(0,END)
                            studentlist.insert(END, (StdID.get(),FirstName.get(),LastName.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))
            #===================================================Frame===================================================
            MainFrame = Frame(self.root,bg="cadet blue")
            MainFrame.grid()
            
            TitFrame = Frame(MainFrame, bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
            TitFrame.pack(side=TOP)
            
            self.lblTit = Label(TitFrame ,font=('arial',47,'bold'),text="Student Database Management System",bg="Ghost White")
            self.lblTit.grid()
            
            ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10,bg="Ghost White", relief=RIDGE)
            ButtonFrame.pack(side=BOTTOM)
            
            DataFrame = Frame(MainFrame, bd=1,width=1300,height=400, padx=20,pady=20, relief=RIDGE, bg="cadet blue")
            DataFrame.pack(side=BOTTOM)
            
            DataFrameLEFT =LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White",font=('arial', 20,'bold'), text="Student Info\n")
            DataFrameLEFT.pack(side=LEFT)
            
            DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="Ghost White",font=('arial', 20,'bold'), text="Student Details\n")
            
            DataFrameRIGHT.pack(side=RIGHT)
            #========================================================Labels=================================================??
            
            self.lblStdID = Label(DataFrameLEFT ,font=('arial', 20,'bold'),text="Student ID:",padx=2,pady=2,bg="Ghost White")
            self.lblStdID .grid(row=0, column=0, sticky=W)
            self.txtStdID = Entry(DataFrameLEFT ,font=('arial', 20,'bold'),textvariable=StdID,width=39)
            self.txtStdID .grid(row=0, column=1)
            
            self.lblfna = Label(DataFrameLEFT ,font=('arial', 20,'bold'),text="First Name:",padx=2,pady=2,bg="Ghost White")
            self.lblfna .grid(row=1, column=0, sticky=W)
            self.txtfna = Entry(DataFrameLEFT ,font=('arial', 20,'bold'),textvariable=FirstName,width=39)
            self.txtfna .grid(row=1, column=1)
            
            self.lbllna = Label(DataFrameLEFT ,font=('arial', 20,'bold'),text="Last Name:",padx=2,pady=2,bg="Ghost White")
            self.lbllna .grid(row=2, column=0, sticky=W)
            self.txtlna = Entry(DataFrameLEFT ,font=('arial', 20,'bold'),textvariable=LastName,width=39)
            self.txtlna .grid(row=2, column=1)
            
            self.lblDoB = Label(DataFrameLEFT ,font=('arial', 20,'bold'),text="Date of Birth:",padx=2,pady=3,bg="Ghost White")
            self.lblDoB .grid(row=3, column=0, sticky=W)
            self.txtDoB = Entry(DataFrameLEFT ,font=('arial', 20,'bold'),textvariable = DoB,width=39)
            self.txtDoB .grid(row=3, column=1)
            
            self.lblage = Label(DataFrameLEFT ,font=('arial', 20,'bold'),text="Age:",padx=2,pady=3,bg="Ghost White")
            self.lblage .grid(row=4, column=0, sticky=W)
            self.txtage = Entry(DataFrameLEFT ,font=('arial', 20,'bold'),textvariable = Age,width=39)
            self.txtage .grid(row=4, column=1)
            
            self.lblgen = Label(DataFrameLEFT ,font=('arial', 20,'bold'),text="Gender:",padx=2,pady=3,bg="Ghost White")
            self.lblgen .grid(row=5, column=0, sticky=W)
            self.txtgen = Entry(DataFrameLEFT ,font=('arial', 20,'bold'),textvariable = Gender,width=39)
            self.txtgen .grid(row=5, column=1)
            
            self.lbladd = Label(DataFrameLEFT ,font=('arial', 20,'bold'),text="Address:",padx=2,pady=3,bg="Ghost White")
            self.lbladd .grid(row=6, column=0, sticky=W)
            self.txtadd = Entry(DataFrameLEFT ,font=('arial', 20,'bold'),textvariable = Address,width=39)
            self.txtadd .grid(row=6, column=1)
            
            self.lblMobile = Label(DataFrameLEFT ,font=('arial', 20,'bold'),text="Mobile:",padx=2,pady=3,bg="Ghost White")
            self.lblMobile .grid(row=7, column=0, sticky=W)
            self.txtMobile = Entry(DataFrameLEFT ,font=('arial', 20,'bold'),textvariable = Mobile,width=39)
            self.txtMobile .grid(row=7, column=1)

#=========================================Listbox===================================


            scrollbar = Scrollbar(DataFrameRIGHT)
            scrollbar.grid(row=0, column=1, sticky='ns')

            studentlist = Listbox(DataFrameRIGHT, width=41, height=16,  font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
            studentlist.bind('<<ListboxSelect>>', StudentRec)
            studentlist.grid(row=0, column=0, padx=8)
            scrollbar.config(command = studentlist.yview)


#================================================Buttons======================================
            
            self.btnAddDate = Button(ButtonFrame, text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,command=addData)
            self.btnAddDate.grid(row=0,column=0)
            self.btnDisplaydata = Button(ButtonFrame, text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
            self.btnDisplaydata.grid(row=0,column=1)
            self.btnClearData = Button(ButtonFrame, text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=clearData)
            self.btnClearData.grid(row=0,column=2)
            self.btnDeleteData = Button(ButtonFrame, text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DeleteDate)
            self.btnDeleteData.grid(row=0,column=3)
            self.btnSearchData = Button(ButtonFrame, text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=searchDatabase)
            self.btnSearchData.grid(row=0,column=4)
            self.btnUpdateData = Button(ButtonFrame, text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=update)
            self.btnUpdateData.grid(row=0,column=5)
            self.btnExit = Button(ButtonFrame, text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=iExit)
            self.btnExit.grid(row=0,column=6)


    
if __name__=='__main__':
    root = Tk()
    application = Students(root)
    root.mainloop()
