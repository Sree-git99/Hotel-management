from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class cust_win:
    def __init__(self,root):
     self.root=root
     self.root.title("Hotel Management System")
     self.root.geometry("1020x600+300+90")
     self.var_ref=StringVar()
     
     
     self.var_name=StringVar()
     self.var_gender=StringVar()
     self.var_postcode=StringVar()
     self.var_mobile=StringVar()
     self.var_email=StringVar()
     self.var_nationality=StringVar()
     self.var_idproof=StringVar()
     self.var_idnumber=StringVar()
     self.var_address=StringVar()




     lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times of roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
     lbl_title.place(x=0,y=0,width=1000,height=50)

     labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times of roman",12,"bold"),padx=2,)
     labelframeleft.place(x=5,y=50,width=400,height=490)

    # lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
    
    # lbl_cust_ref.grid(row=0,column=0,sticky=W)
    # entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=22,font=("arial",12,"bold"),state="readonly")
     #entry_ref.grid(row=0,column=1)
    
     

     name=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
     name.grid(row=1,column=0,sticky=W)
     txtname=ttk.Entry(labelframeleft,textvariable=self.var_name,width=22,font=("arial",12,"bold"))
     txtname.grid(row=1,column=1)

     label_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
     label_gender.grid(row=2,column=0,sticky=W)
     combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=20, font=("arial",12,"bold"),state="readonly")
     combo_gender["value"]=("Male","Female","Other")
     combo_gender.current(0)
     combo_gender.grid(row=2,column=1)
     
     lblpostcode=Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
     lblpostcode.grid(row=3,column=0,sticky=W)
     txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_postcode,width=22,font=("arial",12,"bold"))
     txtpostcode.grid(row=3,column=1)


     lblmobile=Label(labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
     lblmobile.grid(row=4,column=0,sticky=W)
     txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=22,font=("arial",12,"bold"))
     txtmobile.grid(row=4,column=1)
     
     lblemail=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
     lblemail.grid(row=5,column=0,sticky=W)
     txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=22,font=("arial",12,"bold"))
     txtemail.grid(row=5,column=1)
     
     label_nationality=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
     label_nationality.grid(row=6,column=0,sticky=W)
     combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,width=20, font=("arial",12,"bold"),state="readonly")
     combo_nationality["value"]=("Indian","Britis","American")
     combo_nationality.current(0)
     combo_nationality.grid(row=6,column=1)
     
     label_idproof=Label(labelframeleft,text="Idproof:",font=("arial",12,"bold"),padx=2,pady=6)
     label_idproof.grid(row=7,column=0,sticky=W)
     combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,width=20, font=("arial",12,"bold"),state="readonly")
     combo_idproof["value"]=("Adharcard","Driving licence","Passport")
     combo_idproof.current(0)
     combo_idproof.grid(row=7,column=1)
     
     lblidnumber=Label(labelframeleft,text="Idnumber:",font=("arial",12,"bold"),padx=2,pady=6)
     lblidnumber.grid(row=8,column=0,sticky=W)
     txtidnumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=22,font=("arial",12,"bold"))
     txtidnumber.grid(row=8,column=1)

     

     lblAddress=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
     lblAddress.grid(row=9,column=0,sticky=W)
     txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=22,font=("arial",12,"bold"))
     txtAddress.grid(row=9,column=1)

     btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
     btn_frame.place(x=0,y=398,width=385,height=40)

     btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
     btnAdd.grid(row=0,column=0,padx=1)

     btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
     btnUpdate.grid(row=0,column=1,padx=1)

     btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
     btnDelete.grid(row=0,column=2,padx=1)

     btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
     btnReset.grid(row=0,column=3,padx=1)

     Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times of roman",12,"bold"),padx=2,)
     Table_frame.place(x=435,y=50,width=860,height=490)

     lblSearchBy=Label( Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
     lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
     
     self.var_search=StringVar()
     combo_Search=ttk.Combobox(Table_frame,width=15,textvariable=self.var_search, font=("arial",12,"bold"),state="readonly")
     combo_Search["value"]=("Mobile")
     combo_Search.current(0)
     combo_Search.grid(row=0,column=1,padx=2)
     self.var_search=StringVar()
     txtSearch=ttk.Entry(Table_frame,width=15,textvariable=self.var_search,font=("arial",12,"bold"))
     txtSearch.grid(row=0,column=2,padx=2)

     btnSearch=Button(Table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=5)
     btnSearch.grid(row=0,column=3,padx=2)

     btnShowAll=Button(Table_frame,text="ShowAll",command=self.show,font=("arial",12,"bold"),bg="black",fg="gold",width=6)
     btnShowAll.grid(row=0,column=4,padx=2)

     details_table=Frame(Table_frame,bd=2,relief=RIDGE)
     details_table.place(x=0,y=50,width=600,height=350)

     
     Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
     Scroll_Y=ttk.Scrollbar(details_table,orient=VERTICAL)

     self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","gender","postcode","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_Y.set)
     
     Scroll_x.pack(side=BOTTOM,fill=X)
     Scroll_Y.pack(side=RIGHT,fill=Y)

     Scroll_x.config(command=self.Cust_Details_Table.xview)
     Scroll_Y.config(command=self.Cust_Details_Table.yview)
     
     self.Cust_Details_Table.heading("ref",text="Refer No")
     self.Cust_Details_Table.heading("name",text="Name")
     self.Cust_Details_Table.heading("gender",text="Gender")
     self.Cust_Details_Table.heading("postcode",text="Postcode")
     self.Cust_Details_Table.heading("mobile",text="Mobile Number")
     self.Cust_Details_Table.heading("email",text="Email")
     self.Cust_Details_Table.heading("nationality",text="Nationality")
     self.Cust_Details_Table.heading("idproof",text="Idproof")
     self.Cust_Details_Table.heading("idnumber",text="Idnumber")
     self.Cust_Details_Table.heading("address",text="Address")

     self.Cust_Details_Table["show"]="headings"

     self.Cust_Details_Table.column("ref",width=100)
     self.Cust_Details_Table.column("name",width=100)
     self.Cust_Details_Table.column("gender",width=100)
     self.Cust_Details_Table.column("postcode",width=100)
     self.Cust_Details_Table.column("mobile",width=100)
     self.Cust_Details_Table.column("email",width=100)
     self.Cust_Details_Table.column("nationality",width=100)
     self.Cust_Details_Table.column("idproof",width=100)
     self.Cust_Details_Table.column("idnumber",width=100)
     self.Cust_Details_Table.column("address",width=100)
     self.Cust_Details_Table.pack(fill=BOTH,expand=1)
     self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
     self.show()


    def add_data(self):
      con=sqlite3.connect(database="hotelmanagement.db")
      cur=con.cursor()
      try:
        
        if self.var_mobile.get()=="" :
             messagebox.showerror("Error"," All fields are required",parent=self.root)
        else:
           cur.execute("insert into customer(name,gender,postcode,mobile,email,nationality,idproof,idnumber,address) values (?,?,?,?,?,?,?,?,?)",(
                                                                                                                            
                                                                              self.var_name.get(),
                                                                              self.var_gender.get(),
                                                                              self.var_postcode.get(),
                                                                              self.var_mobile.get(),
                                                                              self.var_email.get(),
                                                                              self.var_nationality.get(),
                                                                              self.var_idproof.get(),
                                                                              self.var_idnumber.get(),
                                                                              self.var_address.get()
                                                                              
                                                                              ))
           
           con.commit()
           messagebox.showinfo("success","customer has been updated",parent=self.root)
           self.show()
           
      except Exception as es:
         messagebox.showwarning("warning","some thing went wrong:",parent=self.root)
    def show(self):
          con=sqlite3.connect(database="hotelmanagement.db")
          cur=con.cursor()
          try:
            cur.execute("select * from Customer")
            rows=cur.fetchall()
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for row in rows:
                  self.Cust_Details_Table.insert("",END,values=row)
          except Exception as ex:
               messagebox.showerror("Error",f"Error due to{str(ex)}")
    def get_cursor(self,event=""):
         cursor_row=self.Cust_Details_Table.focus()
         content=self.Cust_Details_Table.item(cursor_row)     
         row=content["values"]
         
         self.var_ref.set(row[0]),
         self.var_name.set(row[1]),
         self.var_gender.set(row[2]),
         self.var_postcode.set(row[3]),
         self.var_mobile.set(row[4]),
         self.var_email.set(row[5]),
         self.var_nationality.set(row[6]),
         self.var_idproof.set(row[7]),
         self.var_idnumber.set(row[8]),
         self.var_address.set(row[9])  
    def update(self):
         if self.var_mobile.get()=="":
              messagebox.showerror("Error","please enter mobile number",parent=self.root)
         else:
              con=sqlite3.connect(database="hotelmanagement.db")
              cur=con.cursor()
              cur.execute("update customer set name=?,gender=?,postcode=?,mobile=?,email=?,nationality=?,idproof=?,idnumber=?,address=? where ref=?",(
                   
                                                                                                                                           self.var_name.get(),
                                                                                                                                           self.var_gender.get(),
                                                                                                                                           self.var_postcode.get(),
                                                                                                                                           self.var_mobile.get(),
                                                                                                                                           self.var_email.get(),
                                                                                                                                           self.var_nationality.get(),
                                                                                                                                           self.var_idproof.get(),
                                                                                                                                           self.var_idnumber.get(),
                                                                                                                                           self.var_address.get(),
                                                                                                                                           self.var_ref.get()
                   
                                                                                                                                       ))
         
         
              con.commit()
              self.show()
              messagebox.showinfo("update","customer details has been updated successfully",parent=self.root)
               
    def delete(self):
         delete=messagebox.askyesno("Hotel Mnagement System","Do you want to delete this customer",parent=self.root)   
         if delete>0:
              con=sqlite3.connect(database="hotelmanagement.db")
              cur=con.cursor()
              query="delete from Customer where ref=?"
              value=(self.var_ref.get(),)
              cur.execute(query,value)
         else:
              if not delete:
                   return
         con.commit()
         self.show()
    def reset(self):
         self.var_ref.set(""),
         self.var_name.set(""),
         self.var_gender.set(""),
         self.var_postcode.set(""),
         self.var_mobile.set(""),
         self.var_email.set(""),
         self.var_nationality.set(""),
         self.var_idproof.set(""),
         self.var_idnumber.set(""),
         self.var_address.set("")  
    def search(self):
         con=sqlite3.connect(database="hotelmanagement.db")
         cur=con.cursor()
         cur.execute(f"select * from Customer where mobile LIKE '%{self.var_search.get()}%'")
         #cur.execute(f"select * from Customer where ref LIKE '%{self.var_search.get()}%'")
     
         rows=cur.fetchall()
         if len(rows)!=0:
              self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
              for i in rows:
                   self.Cust_Details_Table.insert("",END,values=i)
              con.commit()
         
         
          
              
          
     
if __name__ =="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()         
          
          
          
          
          




