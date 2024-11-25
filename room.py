from tkinter import*
from tkinter import ttk
from time import strftime
from datetime import datetime
import sqlite3
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
     self.root=root
     self.root.title("Hotel Management System")
     self.root.geometry("1020x600+300+90")
     
     self.var_contact=StringVar()
     self.var_checkin=StringVar()
     self.var_checkout=StringVar()
     self.var_roomtype=StringVar()
     self.var_roomavailable=StringVar()
     self.var_meal=StringVar()
     self.var_noofdays=StringVar()
     self.var_paidtax=StringVar()
     self.var_subtotal=StringVar()
     self.var_total=StringVar()
     
     
     lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times of roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
     lbl_title.place(x=0,y=0,width=1000,height=50)

     labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("times of roman",12,"bold"),padx=2,)
     labelframeleft.place(x=5,y=50,width=400,height=490)
     
     lbl_cust_contact=Label(labelframeleft,text="Customer contact:",font=("arial",12,"bold"),padx=2,pady=6)
     lbl_cust_contact.grid(row=0,column=0,sticky=W)
     entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=15,font=("arial",12,"bold"))
     entry_contact.grid(row=0,column=1,sticky=W)
     
     btnFetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
     btnFetchData.place(x=300,y=4)
     
     check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in_date:",padx=2,pady=6)
     check_in_date.grid(row=1,column=0,sticky=W)
     txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=22,font=("arial",12,"bold"))
     txtcheck_in_date.grid(row=1,column=1)
     
     lbl_check_out_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_out_date:",padx=2,pady=6)
     lbl_check_out_date.grid(row=2,column=0,sticky=W)
     txtcheck_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=22,font=("arial",12,"bold"))
     txtcheck_out_date.grid(row=2,column=1)
     
     label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
     label_RoomType.grid(row=3,column=0,sticky=W)
     
     con=sqlite3.connect(database="hotelmanagement.db")
     cur=con.cursor()
     cur.execute("select RoomType from details")
     ide=cur.fetchall()
     
     combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,width=20, font=("arial",12,"bold"),state="readonly")
     combo_RoomType["value"]=ide
     combo_RoomType.current(0)
     combo_RoomType.grid(row=3,column=1)
     
     lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
     lblRoomAvailable.grid(row=4,column=0,sticky=W)
     #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=22,font=("arial",12,"bold"))
     #txtRoomAvailable.grid(row=4,column=1)
     
     con=sqlite3.connect(database="hotelmanagement.db")
     cur=con.cursor()
     cur.execute("select Roomno from details")
     rows=cur.fetchall()
     
     combo_Roomno=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,width=20, font=("arial",12,"bold"),state="readonly")
     combo_Roomno["value"]=rows
     combo_Roomno.current(0)
     combo_Roomno.grid(row=4,column=1)
     
     
     lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
     lblMeal.grid(row=5,column=0,sticky=W)
     txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=22,font=("arial",12,"bold"))
     txtMeal.grid(row=5,column=1)
     
     lblNoofdays=Label(labelframeleft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
     lblNoofdays.grid(row=6,column=0,sticky=W)
     txtNoofdays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=22,font=("arial",12,"bold"))
     txtNoofdays.grid(row=6,column=1)
     
     lblNoofdays=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
     lblNoofdays.grid(row=7,column=0,sticky=W)
     txtNoofdays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=22,font=("arial",12,"bold"))
     txtNoofdays.grid(row=7,column=1)
     
     lblNoofdays=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
     lblNoofdays.grid(row=8,column=0,sticky=W)
     txtNoofdays=ttk.Entry(labelframeleft,textvariable=self.var_subtotal,width=22,font=("arial",12,"bold"))
     txtNoofdays.grid(row=8,column=1)
     
     lblTotalCost=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
     lblTotalCost.grid(row=9,column=0,sticky=W)
     txtTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=22,font=("arial",12,"bold"))
     txtTotalCost.grid(row=9,column=1)
     
     btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
     btnBill.grid(row=10,column=0,padx=1,sticky=W)

     
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
     Table_frame.place(x=435,y=300,width=800,height=245)

     lblSearchBy=Label( Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
     lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
     
     self.var_search=StringVar()
     combo_Search=ttk.Combobox(Table_frame,width=15,textvariable=self.var_search, font=("arial",12,"bold"),state="readonly")
     combo_Search["value"]=("Contact")
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
     details_table.place(x=0,y=50,width=600,height=120)

     
     Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
     Scroll_Y=ttk.Scrollbar(details_table,orient=VERTICAL)

     self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_Y.set)
     
     Scroll_x.pack(side=BOTTOM,fill=X)
     Scroll_Y.pack(side=RIGHT,fill=Y)

     Scroll_x.config(command=self.room_table.xview)
     Scroll_Y.config(command=self.room_table.yview)
     
     self.room_table.heading("contact",text="Contact")
     self.room_table.heading("checkin",text="Check-in")
     self.room_table.heading("checkout",text="Check-out")
     self.room_table.heading("roomtype",text="Room Type")
     self.room_table.heading("roomavailable",text="Room No") 
     self.room_table.heading("meal",text="Meal")
     self.room_table.heading("noofdays",text="No of Days")

     self.room_table["show"]="headings"

     self.room_table.column("contact",width=100)
     self.room_table.column("checkin",width=100)
     self.room_table.column("checkout",width=100)
     self.room_table.column("roomtype",width=100)
     self.room_table.column("roomavailable",width=100)
     self.room_table.column("meal",width=100)
     self.room_table.column("noofdays",width=100)

     self.room_table.pack(fill=BOTH,expand=1)
     self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
     self.show()
     
     
    def add_data(self):
      con=sqlite3.connect(database="hotelmanagement.db")
      cur=con.cursor()
      try:
        if self.var_contact.get()=="" :
             messagebox.showerror("Error"," All fields are required",parent=self.root)
        else:
           cur.execute("insert into room(contact,checkin,checkout,roomtype,roomavailable,meal,noofdays) values (?,?,?,?,?,?,?)",(
                                                                                                                            
                                                                              self.var_contact.get(),
                                                                              self.var_checkin.get(),
                                                                              self.var_checkout.get(),
                                                                              self.var_roomtype.get(),
                                                                              self.var_roomavailable.get(),
                                                                              self.var_meal.get(),
                                                                              self.var_noofdays.get()
                                                                              
                                                                              ))
           
           con.commit()
           self.show()
           messagebox.showinfo("success","Room Booked",parent=self.root)
        
           
      except Exception as es:
         print(es)
         messagebox.showwarning("warning","some thing went wrong:",parent=self.root)
     
     
    def show(self):
          con=sqlite3.connect(database="hotelmanagement.db")
          cur=con.cursor()
          try:
            cur.execute("select * from room")
            rows=cur.fetchall()
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                  self.room_table.insert("",END,values=row)
          except Exception as ex:
               messagebox.showerror("Error",f"Error due to{str(ex)}")
               
    def get_cursor(self,event=""):
         cursor_row=self.room_table.focus()
         content=self.room_table.item(cursor_row)     
         row=content["values"]
         self.var_contact.set(row[0]),
         self.var_checkin.set(row[1]),
         self.var_checkout.set(row[2]),
         self.var_roomtype.set(row[3]),
         self.var_roomavailable.set(row[4]),
         self.var_meal.set(row[5]),
         self.var_noofdays.set(row[6])   
         
         
    def update(self):
         if self.var_contact.get()=="":
              messagebox.showerror("Error","please enter mobile number",parent=self.root)
         else:
              con=sqlite3.connect(database="hotelmanagement.db")
              cur=con.cursor()
              cur.execute("update room set checkin=?,checkout=?,roomtype=?,roomavailable=?,meal=?,noofdays=? where contact=?",(
                   
                                                                                                                                           self.var_checkin.get(),
                                                                                                                                           self.var_checkout.get(),
                                                                                                                                           self.var_roomtype.get(),
                                                                                                                                           self.var_roomavailable.get(),
                                                                                                                                           self.var_meal.get(),
                                                                                                                                           self.var_noofdays.get(),
                                                                                                                                           self.var_contact.get()
                   
                                                                                                                                       ))
         
         
              con.commit()
              self.show()
              messagebox.showinfo("update","Room details has been updated successfully",parent=self.root)
                     
    def delete(self):
         delete=messagebox.askyesno("Hotel Mnagement System","Do you want to delete this room details",parent=self.root)   
         if delete>0:
              con=sqlite3.connect(database="hotelmanagement.db")
              cur=con.cursor()
              query="delete from room where contact=?"
              value=(self.var_contact.get(),)
              cur.execute(query,value)
         else:
              if not delete:
                   return
         con.commit()
         self.show()
    def reset(self):
         self.var_contact.set(""),
         self.var_checkin.set(""),
         self.var_checkout.set(""),
         self.var_roomtype.set(""),
         self.var_roomavailable.set(""),
         self.var_meal.set(""),
         self.var_noofdays.set("")            
         self.var_paidtax.set("")
         self.var_subtotal.set("")
         self.var_total.set("")
               
    
     
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter contact number",parent=self.root)
        else:
            con=sqlite3.connect(database="hotelmanagement.db")
            cur=con.cursor()
            query=("select Name from Customer where mobile=?")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            
            
            if row==None:
                messagebox.showerror("Error","this number is not found",parent=self.root)
            else:
                con.commit()
                
            showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataframe.place(x=450,y=55,width=300,height=180)
            
            lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))    
            lbl.place(x=80,y=0)
            
            con=sqlite3.connect(database="hotelmanagement.db")
            cur=con.cursor()
            query=("select Gender from Customer where mobile=?")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            
            lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=30)
            lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))    
            lbl2.place(x=80,y=30)
            
            con=sqlite3.connect(database="hotelmanagement.db")
            cur=con.cursor()
            query=("select Email from Customer where mobile=?")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            
            lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
            lblEmail.place(x=0,y=60)
            lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))    
            lbl3.place(x=80,y=60)
            
            con=sqlite3.connect(database="hotelmanagement.db")
            cur=con.cursor()
            query=("select Nationality from Customer where mobile=?")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            
            lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
            lblNationality.place(x=0,y=90)
            lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))    
            lbl4.place(x=90,y=90)
            
            con=sqlite3.connect(database="hotelmanagement.db")
            cur=con.cursor()
            query=("select Address from Customer where mobile=?")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            
            lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
            lblAddress.place(x=0,y=120)
            lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))    
            lbl4.place(x=80,y=120)
            
    def search(self):
         con=sqlite3.connect(database="hotelmanagement.db")
         cur=con.cursor()
         cur.execute(f"select * from room where contact LIKE '%{self.var_search.get()}%'")
         
     
         rows=cur.fetchall()
         if len(rows)!=0:
              self.room_table.delete(*self.room_table.get_children())
              for i in rows:
                   self.room_table.insert("",END,values=i)
              con.commit()
         
            
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")    
        outDate=datetime.strptime(outDate,"%d/%m/%Y")    
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_meal.get()=="Breakfast" and self .var_roomtype.get()=="Single"):
            q1=float (300)
            q2=float (700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self. var_subtotal.set(ST)
            self. var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxary"):
            q1=float (700)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+((q5)*0.09)))
            self. var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float (500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+((q5)*0.09)))
            self. var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float (500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+((q5)*0.09)))
            self. var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        
        
     
     
     
     
     
     
     
if __name__ =="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()       