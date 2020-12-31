from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('loandb.db')
cur = conn.cursor()

def CreateDatabase():
  cur.execute("""
        CREATE TABLE tbl_credit
        (
          credit_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          first_name VARCHAR(30) NOT NULL,
          last_name VARCHAR(30) NOT NULL,
          gender VARCHAR(20) NOT NULL,
          contact INTEGER NOT NULL,
          home_address VARCHAR(255) NOT NULL,
          status VARCHAR(20) NOT NULL,
          products_taken VARCHAR(255) NOT NULL,
          total_cost INTEGER NOT NULL
        );
""")

def FetchData():

  sql = "SELECT * FROM tbl_credit"

  for rows in cur.execute(sql):
    print(rows)

#FetchData()
#CreateDatabase()

class CreditApplication:
  def __init__(self, master):
    self.master = master

    conn = sqlite3.connect('loandb.db')
    cur = conn.cursor()

    self.title = Label(root, text="CREDIT MANAGEMENT SYSTEM", width=66, height=2, relief=GROOVE, bd=5, font=('arial 25 bold'), fg='cyan', bg='darkgreen')
    self.title.place(x = 17, y = 10)

    self.firstname = Label(root, text="First Name:", font=('arial 18 bold'), fg='white', bg='darkcyan')
    self.firstname.place(x = 20, y = 160)
    self.fname_entry = Entry(root, font=('arial 18 bold'), justify="center", fg='darkcyan')
    self.fname_entry.place(x = 20, y = 190)

    self.lastname = Label(root, text="Last Name:", font=('arial 18 bold'), fg='white', bg='darkcyan')
    self.lastname.place(x = 20, y = 250)
    self.lname_entry = Entry(root, font=('arial 18 bold'), justify="center", fg='darkcyan')
    self.lname_entry.place(x = 20, y = 280)

    self.contact = Label(root, text="Contact:", font=('arial 18 bold'), fg='white', bg='darkcyan')
    self.contact.place(x = 20, y = 340)
    self.contact_entry = Entry(root, font=('arial 18 bold'), justify="center", fg='darkcyan')
    self.contact_entry.place(x = 20, y = 370)

    self.status = Label(root, text="Status:", font=('arial 18 bold'), fg='white', bg='darkcyan')
    self.status.place(x = 350, y = 250)
    self.status_entry = ttk.Combobox(root, font=('arial 18 bold'), width=18)
    self.status_entry['values'] = ("Paid", "Unpaid")
    self.status_entry.place(x = 350, y = 280)

    self.gender = Label(root, text="Gender:", font=('arial 18 bold'), fg='white', bg='darkcyan')
    self.gender.place(x = 350, y = 340)
    self.gender_cmb = ttk.Combobox(root, font=('arial 18 bold'), width=18)
    self.gender_cmb['values'] = ("Male", "Female", "Others")
    self.gender_cmb.place(x = 350, y = 370)

    self.total = Label(root, text="Total Cost:", font=('arial 18 bold'), fg='white', bg='darkcyan')
    self.total.place(x = 350, y = 160)
    self.total_entry = Entry(root, font=('arial 18 bold'), justify="center", fg='darkcyan')
    self.total_entry.place(x = 350, y = 190)

    self.address = Label(root, text="Address:", font=('arial 18 bold'), fg='white', bg='darkcyan')
    self.address.place(x = 680, y = 160)
    self.address_entry = Entry(root, font=('arial 18 bold'), fg='darkcyan', width=30)
    self.address_entry.place(x = 680, y = 190)

    self.item = Label(root, text="Items taken:", font=('arial 18 bold'), fg='white', bg='darkcyan')
    self.item.place(x = 680, y = 250)
    self.item_entry = Entry(root, font=('arial 18 bold'), fg='darkcyan', width=30)
    self.item_entry.place(x = 680, y = 280)


    self.search_entry =  Entry(root, font=('arial 30 bold'), justify="center", width=8, fg='red')
    self.search_entry.place(x = 188, y = 467)


    def DataTable():
      db_table = ttk.Treeview(root)
      db_table['column'] = ("CreditId", "Firstname", "Lastname", "Gender", "Contact", "Address", "Status", "Items", "Total")
      db_table.column("#0", width=0, stretch=NO)
      db_table.column("CreditId", width=80)
      db_table.column("Firstname", width=120)
      db_table.column("Lastname", width=120)
      db_table.column("Gender", width=80)
      db_table.column("Contact", width=125)
      db_table.column("Address")
      db_table.column("Status", width=80)
      db_table.column("Items", width=430)
      db_table.column("Total", width=80)
      
      db_table.heading("#0")
      db_table.heading("CreditId",  text="CREDIT ID")
      db_table.heading("Firstname",  text="FIRST NAME")
      db_table.heading("Lastname", text="LAST NAME")
      db_table.heading("Gender", text="GENDER")
      db_table.heading("Contact", text="CONTACT")
      db_table.heading("Address", text="ADDRESS")
      db_table.heading("Status", text="STATUS")
      db_table.heading("Items", text="ITEMS")
      db_table.heading("Total", text="TOTAL")

      count = 0
      sql = "SELECT * FROM tbl_credit"
      for rows in cur.execute(sql):
        db_table.insert(parent='', index='end', iid=count, text="", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rows[8]))
        count += 1

      db_table.place(x = 20, y = 520)

    #CRUD FUNCTIONS
    def CloseApp():
      self.message = messagebox.askyesno("Warning", "Are you sure you want to close the application?")
      if self.message == True:
        root.destroy()
      else:
        pass


    def SaveData():
      self.firstname = self.fname_entry.get()
      self.lastname = self.lname_entry.get()
      self.gender = self.gender_cmb.get()
      self.contact = self.contact_entry.get()
      self.address = self.address_entry.get()
      self.status = self.status_entry.get()
      self.item = self.item_entry.get()
      self.total = self.total_entry.get()

      if self.firstname == "" or self.lastname == "" or self.contact == "" or self.status == "" or self.gender == "" or self.total == "":
        messagebox.showinfo("Info", "No empty field is allowed, fill all!")
      else:
        sql = "INSERT INTO tbl_credit(first_name, last_name, gender, contact, home_address, status, products_taken, total_cost) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(sql, (self.firstname, self.lastname, self.gender, self.contact, self.address, self.status, self.item, self.total ))
        conn.commit()
        messagebox.showinfo("Info", "You have successfully saved a new record")
        ClearForm()
        DataTable()


    def ClearForm():
      self.search_entry.delete(0, END)
      self.fname_entry.delete(0, END)
      self.lname_entry.delete(0, END)
      self.gender_cmb.delete(0, END)
      self.contact_entry.delete(0, END)
      self.address_entry.delete(0, END)
      self.status_entry.delete(0, END)
      self.item_entry.delete(0, END)
      self.total_entry.delete(0, END)


    def ResetForm():
      ClearForm()
      DataTable()
      self.btn_save['state'] = NORMAL

    def SearchData():
      self.search_id = self.search_entry.get()
      if self.search_id == "":
        messagebox.showinfo("Warning", "You have enter the ID of the record you want to fetch")
      else:
        sql = "SELECT * FROM tbl_credit WHERE credit_id = ?"
        rows = cur.execute(sql, (self.search_id, ))
        for row in rows:
          self.val_1 = row[1]
          self.val_2 = row[2]
          self.val_3 = row[3]
          self.val_4 = row[4]
          self.val_5 = row[5]
          self.val_6 = row[6]
          self.val_7 = row[7]
          self.val_8 = row[8]

          self.fname_entry.delete(0, END)
          self.fname_entry.insert(END, self.val_1)
          self.lname_entry.delete(0, END)
          self.lname_entry.insert(END, self.val_2)   
          self.gender_cmb.delete(0, END) 
          self.gender_cmb.insert(END, self.val_3)
          self.contact_entry.delete(0, END)  
          self.contact_entry.insert(END, self.val_4)
          self.address_entry.delete(0, END)
          self.address_entry.insert(END, self.val_5)
          self.status_entry.delete(0, END)
          self.status_entry.insert(END, self.val_6)
          self.item_entry.delete(0, END)     
          self.item_entry.insert(END, self.val_7)
          self.total_entry.delete(0, END)
          self.total_entry.insert(END, self.val_8)

          self.btn_save['state'] = DISABLED


    def UpdateData():
      self.id_num = self.search_entry.get()
      self.firstname = self.fname_entry.get()
      self.lastname = self.lname_entry.get()
      self.gender = self.gender_cmb.get()
      self.contact = self.contact_entry.get()
      self.address = self.address_entry.get()
      self.status = self.status_entry.get()
      self.item = self.item_entry.get()
      self.total = self.total_entry.get()

      if self.id_num == "":
        messagebox.showinfo("Info", "Enter the ID for the record you want to update")
      else:
        sql = "UPDATE tbl_credit SET first_name = ?, last_name = ?, gender = ?, contact = ?, home_address = ?, status = ?, products_taken = ?, total_cost = ? WHERE credit_id = ?"
        cur.execute(sql, (self.firstname, self.lastname, self.gender, self.contact, self.address, self.status, self.item, self.total, self.id_num))
        conn.commit()
        messagebox.showinfo("Info", "You have successfully updated the selected record")
        ClearForm()
        DataTable()


    def DeleteData():
      self.id_num = self.search_entry.get()
      if self.id_num == "":
        messagebox.showinfo("Info", "Please enter ID for the record you want to delete!")
      else:
        self.message = messagebox.askyesno("Qquestion", "Are you sure you want to delete the selected record?")
        if self.message == True:
          sql = "DELETE FROM tbl_credit WHERE credit_id = ?"
          cur.execute(sql, (str(self.id_num), ))
          conn.commit()
          messagebox.showinfo("Info", "You have successfully deleted the selected record")
          ClearForm()
          DataTable()
        else:
          pass


    #BUTTONS FOR CRUD OPERATIONS
    DataTable()
    self.btn_save = Button(root, text="SAVE", command = SaveData, font=('arial 17 bold'), fg='white', bg='green', width=13)
    self.btn_save.place(x = 1150, y = 200)

    self.btn_update = Button(root, text="UPDATE", command = UpdateData, font=('arial 17 bold'), fg='white', bg='blue', width=13)
    self.btn_update.place(x = 1150, y = 260)

    self.btn_delete = Button(root, text="DELETE", command = DeleteData, font=('arial 17 bold'), fg='white', bg='red', width=13)
    self.btn_delete.place(x = 1150, y = 320)

    self.btn_reset = Button(root, text="RESET FORM", command = ResetForm, font=('arial 17 bold'), fg='white', bg='purple', width=13)
    self.btn_reset.place(x = 1150, y = 380)

    self.btn_close = Button(root, text="CLOSE APP", command = CloseApp, font=('arial 17 bold'), fg='white', bg='darkorange', width=13)
    self.btn_close.place(x = 1150, y = 440)

    self.btn_search = Button(root, text="Search by ID:", command = SearchData, font=('arial 17 bold'), fg='white', bg='green')
    self.btn_search.place(x = 20, y = 470)



root = Tk()
root.configure(bg='darkcyan')
root.wm_attributes("-fullscreen", True)
root.geometry("1200x700")
conn = CreditApplication(root)


root.mainloop()