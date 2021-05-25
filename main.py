from tkinter import *
from tkinter import ttk
import pymysql
# for displaying mesagebox ****************************************************************
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1570x750+0+0")

        # for writing a title to the window*********************************************************************

        title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", bd=10, relief=GROOVE,
                      font=("times new roman", 30, "bold"), bg="black", fg="red")
        title.pack(side=TOP, fill=X)

        # variables***********************************************************************************************************************
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # manage frame*************************************************************************************************************
        Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="black")
        Manage_frame.place(x=20, y=100, width=500, height=640)
        # for giving a title in a manage frame**************************************************************************************
        m_title = Label(Manage_frame, text="Manage students", font=("times new roman", 25, "bold"), bg="black",
                        fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        # for writing a lable roll no**********************************************************************************************
        lbl_roll = Label(Manage_frame, text="ROLL NO:-", font=("times new roman", 20, "bold"), bg="black", fg="white")
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        # for making a text box for writhing a roll no*******************************************************************************
        txt_roll = Entry(Manage_frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"),
                         relief=GROOVE, bd=5)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # for writing a lable name*************************************************************************************************
        lbl_name = Label(Manage_frame, text="NAME:-", font=("times new roman", 20, "bold"), bg="black", fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        # for making a text box for entering name************************************************************************************
        txt_name = Entry(Manage_frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), relief=GROOVE,
                         bd=5)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # for writing a lable email*************************************************************************************************
        lbl_email = Label(Manage_frame, text="EMAIL:-", font=("times new roman", 20, "bold"), bg="black", fg="white")
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        # for making a text box for entering email******************************************************************
        txt_email = Entry(Manage_frame, textvariable=self.email_var, font=("times new roman", 15, "bold"),
                          relief=GROOVE, bd=5)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # for making a lable gender********************************************************************************
        lbl_gender = Label(Manage_frame, text="GENDER:-", font=("times new roman", 20, "bold"), bg="black", fg="white")
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        # for making a combobox for selecting any gender***************************************************************************
        combo_gender = ttk.Combobox(Manage_frame, textvariable=self.gender_var, font=("times new roman", 14, "bold"),
                                    state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, padx=20, sticky="w")

        # for making a lable contact*************************************************************************
        lbl_contact = Label(Manage_frame, text="CONTACT:-", font=("times new roman", 20, "bold"), bg="black",
                            fg="white")
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        # for writing a contact no*******************************************************************************************
        txt_contact = Entry(Manage_frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"),
                            relief=GROOVE, bd=5)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # for making a lable dob************************************************************************************************
        lbl_dob = Label(Manage_frame, text="D.O.B.:-", font=("times new roman", 20, "bold"), bg="black", fg="white")
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        # for making a text box for writing dob**********************************************************************
        txt_dob = Entry(Manage_frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), relief=GROOVE,
                        bd=5)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # for making a lable address************************************************************************************
        lbl_address = Label(Manage_frame, text="ADDRESS:-", font=("times new roman", 20, "bold"), bg="black",
                            fg="white")
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        # for making a text box for entering address****************************************
        self.txt_address = Text(Manage_frame, width=25, height=5)
        self.txt_address.grid(row=7, column=1, padx=20, pady=20, sticky="w")

        # button frame***************************************************************************************************
        Btn_frame = Frame(Manage_frame, relief=RIDGE, bg="black")
        Btn_frame.place(x=50, y=550, width=430)
        # for making add button*********************************
        addbtn = Button(Btn_frame, text="ADD", width=10, command=self.add_students)
        addbtn.grid(row=0, column=0, padx=10, pady=10)
        # for making update button**************************************************
        updatebtn = Button(Btn_frame, text="UPDATE", width=10, command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=10, pady=10)
        # for making delete button*********************************************************************
        deletebtn = Button(Btn_frame, text="DELETE", width=10, command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)
        # for making clear button*********************************************************
        clearbtn = Button(Btn_frame, text="CLEAR", width=10, command=self.clear)
        clearbtn.grid(row=0, column=3, padx=10, pady=10)

        # detail frame*****************************
        Detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="black")
        Detail_frame.place(x=600, y=100, width=800, height=640)
        # for writing a lable search******************************
        lbl_search = Label(Detail_frame, text="SEARCH BY:-", font=("times new roman", 20, "bold"), bg="black",
                           fg="white")
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        # for making a combo box for search*******************************************************
        combo_search = ttk.Combobox(Detail_frame, textvariable=self.search_by, width=10,
                                    font=("times new roman", 14, "bold"), state="readonly")
        combo_search["values"] = ("Roll_No", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, sticky="w")
        # for making a text box search************************************************
        txt_search = Entry(Detail_frame, textvariable=self.search_txt, width=15, font=("times new roman", 15, "bold"),
                           relief=GROOVE, bd=5)
        txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")
        # for making a search button*******************************************************
        searchbtn = Button(Detail_frame, text="SEARCH", width=10, pady=5, command=self.search_data)
        searchbtn.grid(row=0, column=3, padx=10, pady=10)
        # for making a showall button**********************************************************
        showallbtn = Button(Detail_frame, text="SHOWALL", width=10, pady=5, command=self.fetch_data)
        showallbtn.grid(row=0, column=4, padx=10, pady=10)

        # table frame*****************************************************************************************

        Table_frame = Frame(Detail_frame, bd=4, relief=RIDGE, bg="black")
        Table_frame.place(x=10, y=70, width=750, height=530)

        # for making a scroll bar*******************************************
        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_frame,
                                          columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        # for entering a heading in rows and columns of row*******************************************************
        self.Student_table.heading("roll", text="ROLL NO")
        self.Student_table.heading("name", text="NAME")
        self.Student_table.heading("email", text="EMAIL")
        self.Student_table.heading("gender", text="GENDER")
        self.Student_table.heading("contact", text="CONTACT")
        self.Student_table.heading("dob", text="D.O.B.")
        self.Student_table.heading("address", text="ADDRESS")
        self.Student_table["show"] = "headings"
        self.Student_table.column("roll", width=50)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=50)
        self.Student_table.column("contact", width=50)
        self.Student_table.column("dob", width=50)
        self.Student_table.column("address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)



    # for making a connection with phpmyadmin database******************************************
    def add_students(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("ERROR", "ALL fields are required!!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="mp")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                              self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txt_address.get('1.0', END)
                                                                              ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    # to show the data added in phpmyadmin on our main window************************************
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="mp")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    # for working of clear button**************************************************
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

    #
    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents["values"]
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])

    # for working of update botton*****************************************************************************
    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="mp")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_address.get('1.0', END),
            self.Roll_No_var.get()
        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    # for working of delete data**********************************************************************
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="mp")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.clear()

    # for working of search button*****************************************************************
    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="mp")
        cur = con.cursor()
        cur.execute("select * from students where " + str(self.search_by.get()) + " LIKE '%" + str(
            self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()
