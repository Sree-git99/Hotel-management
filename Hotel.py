from tkinter import*
from PIL import Image,ImageTk
from Customer import cust_win
from room import Roombooking
from details import DetailsRoom




class HotelManagementSystem:
    def __init__(self,root):
     self.root=root
     self.root.title("Hotel Management System")
     self.root.geometry("1550x800+0+0")
     self.bg=ImageTk.PhotoImage(file=r"C:\Users\skrpg\Desktop\HotelManagement\images\hotel.jpg")
     lbl_bg=Label(self.root,image=self.bg)
     lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
     
     
     lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times of roman",30,"bold"),bg="blue",fg="gold",bd=4,relief=RIDGE)
     lbl_title.place(x=0,y=0,width=1400,height=50)
     
     


     main_frame=Frame(self.root,bd=4,relief=RIDGE)
     main_frame.place(x=0,y=50,width=290,height=155)
     
     
     lbl_title=Label(main_frame,text="MENU",font=("times of roman",19,"bold"),bg="blue",fg="gold",bd=1,relief=RIDGE)
     lbl_title.place(x=0,y=0,width=285)

     btn_frame=Frame(main_frame,bd=0,relief=RIDGE)
     btn_frame.place(x=0,y=30,width=300,height=160)
     
     
     
     
     cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=35,font=("times of roman",10,"bold"),bg="blue",fg="gold",bd=1,cursor="hand1")
     cust_btn.grid(row=0,column=0,pady=2 )

     room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=35,font=("times of roman",10,"bold"),bg="blue",fg="gold",bd=1,cursor="hand1")
     room_btn.grid(row=1,column=0,pady=2 )

     details_btn=Button(btn_frame,text="DETAILS",command=self.details,width=35,font=("times of roman",10,"bold"),bg="blue",fg="gold",bd=1,cursor="hand1")
     details_btn.grid(row=2,column=0,pady=2 )
     

     logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=35,font=("times of roman",10,"bold"),bg="blue",fg="gold",bd=1,cursor="hand1")
     logout_btn.grid(row=3,column=0,pady=2 )

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
        
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        
    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
    def logout(self):
        self.root.destroy()





if __name__ =="__main__":
   root=Tk()
   OBJ=HotelManagementSystem(root)
   root.mainloop()     