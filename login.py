from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
from Hotel import HotelManagementSystem

class loginwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\skrpg\Desktop\HotelManagement\images\login1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=150,width=340,height=450)
        
        get_str=Label(frame,text="Login",font=("times new roman",20,"bold"),bg="white",fg="black")
        get_str.place(x=125,y=30)
        
        usernamelbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white",fg="black")
        usernamelbl.place(x=40,y=90)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=140,width=280,height=30)
        
        passwordlbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        passwordlbl.place(x=40,y=200)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=240,width=280,height=30)
        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="skyblue")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        

        
        
    
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "12345":
            messagebox.showinfo("Success", "Welcome to Hostel Management System, You are logged in as admin")
            self.Hotel()
        else:
            messagebox.showerror("Invalid", "Invalid username and password")
            
            
    def Hotel(self):
        self.new_window = Toplevel(self.root)
        self.app = HotelManagementSystem(self.new_window)
            


if __name__ =="__main__":
     if __name__ == "__main__":
       root = Tk()
       obj = loginwindow(root)
       root.mainloop()