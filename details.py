from tkinter import*
from tkinter import ttk
from time import strftime
from datetime import datetime
import sqlite3
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
     self.root=root
     self.root.title("Hotel Management System")
     self.root.geometry("1020x600+300+90")
     
     lbl_title=Label(self.root,text="ROOM DETAILS",font=("times of roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
     lbl_title.place(x=0,y=0,width=1000,height=50)

     labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text=" New Room Add",font=("times of roman",12,"bold"),padx=2,)
     labelframeleft.place(x=5,y=50,width=450,height=350)
     
     lbl_Floor=Label(labelframeleft,text="Floor:",font=("arial",12,"bold"),padx=2,pady=6)
     lbl_Floor.grid(row=0,column=0,sticky=W)
     
     self.var_Floor=StringVar()
     entry_Floor=ttk.Entry(labelframeleft,textvariable=self.var_Floor,width=18,font=("arial",12,"bold"))
     entry_Floor.grid(row=0,column=1,sticky=W)
     
     lbl_Roomno=Label(labelframeleft,text="Room No:",font=("arial",12,"bold"),padx=2,pady=6)
     lbl_Roomno.grid(row=1,column=0,sticky=W)
     self.var_Roomno=StringVar()
     entry_Roomno=ttk.Entry(labelframeleft,textvariable=self.var_Roomno,width=18,font=("arial",12,"bold"))
     entry_Roomno.grid(row=1,column=1,sticky=W)
     
     
     lbl_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
     lbl_RoomType.grid(row=2,column=0,sticky=W)
     self.var_RoomType=StringVar()
     entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=18,font=("arial",12,"bold"))
     entry_RoomType.grid(row=2,column=1,sticky=W)
     
     btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
     btn_frame.place(x=0,y=200,width=385,height=40)

     btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
     btnAdd.grid(row=0,column=0,padx=1)

     btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
     btnUpdate.grid(row=0,column=1,padx=1)

     btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
     btnDelete.grid(row=0,column=2,padx=1)

     btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
     btnReset.grid(row=0,column=3,padx=1)
     
     Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times of roman",12,"bold"),padx=2,)
     Table_frame.place(x=500,y=60,width=500,height=350)
     
     Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
     Scroll_Y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

     self.room_table=ttk.Treeview(Table_frame,column=("floor","roomno","roomtype"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_Y.set)
     Scroll_x.pack(side=BOTTOM,fill=X)
     Scroll_Y.pack(side=RIGHT,fill=Y)

     Scroll_x.config(command=self.room_table.xview)
     Scroll_Y.config(command=self.room_table.yview)
     
     self.room_table.heading("floor",text="Floor")
     self.room_table.heading("roomno",text="Roomno")
     self.room_table.heading("roomtype",text="RoomType")

     self.room_table["show"]="headings"

     self.room_table.column("floor",width=100)
     self.room_table.column("roomno",width=100)
     self.room_table.column("roomtype",width=100)
     self.room_table.pack(fill=BOTH,expand=1)
     self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
     self.show()
     
    def add_data(self):
      con=sqlite3.connect(database="hotelmanagement.db")
      cur=con.cursor()
      try:
        if self.var_Floor.get()=="" :
             messagebox.showerror("Error"," All fields are required",parent=self.root)
        else:
           cur.execute("insert into details(Floor,Roomno,RoomType) values (?,?,?)",(
                                                                                                                            
                                                                              self.var_Floor.get(),
                                                                              self.var_Roomno.get(),
                                                                              self.var_RoomType.get(),
                                                                            
                                                                    
                                                                        
                                                        
                                                                              
                                                                              ))
           
           con.commit()
           self.show()
    
           messagebox.showinfo("success","New Room Added Successfully",parent=self.root)
        
           
      except Exception as es:
         print(es)
         messagebox.showwarning("warning","some thing went wrong:",parent=self.root)
     
     
    def show(self):
          con=sqlite3.connect(database="hotelmanagement.db")
          cur=con.cursor()
          try:
            cur.execute("select * from details")
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
         self.var_Floor.set(row[0]),
         self.var_Roomno.set(row[1]),
         self.var_RoomType.set(row[2])
         
    def update(self):
         if self.var_Floor.get()=="":
              messagebox.showerror("Error","please enter floor ",parent=self.root)
         else:
              con=sqlite3.connect(database="hotelmanagement.db")
              cur=con.cursor()
              cur.execute("update details set Floor=?,RoomType=? where Roomno=?",(
                   
                                                                     self.var_Floor.get(),
                                                                     self.var_RoomType.get(),
                                                                     self.var_Roomno.get(),
                                                                                                                                           
                                                                                                                                       
                                                                                                                                       
                                                                                                                                           
                   
                                                                                                                                       ))
         
         
              con.commit()
              self.show()
              messagebox.showinfo("update","Room details has been updated successfully",parent=self.root)
                     
           
    def delete(self):
         delete=messagebox.askyesno("Hotel Mnagement System","Do you want to delete this room details",parent=self.root)   
         if delete>0:
              con=sqlite3.connect(database="hotelmanagement.db")
              cur=con.cursor()
              query="delete from details where Roomno=?"
              value=(self.var_Roomno.get(),)
              cur.execute(query,value)
         else:
              if not delete:
                   return
         con.commit()
         self.show()
    def reset(self):
         self.var_Floor.set(""),
         self.var_Roomno.set(""),
         self.var_RoomType.set("")
                   
     
     
     
     
if __name__ =="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop() 