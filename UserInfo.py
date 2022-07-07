
from doctest import master
from tkinter import *

def save_info():
    Username_info = username.get()
    Email_info = Email.get()
    Password_info = password.get()
    GreenScreen_info = GreenScreen.get()
    GsPassword_info = GsPassword.get()
    
    
    print(Username_info,Password_info,Email_info,GreenScreen_info,GsPassword_info)
    
    file = open("user.txt","w")
    
    file.write("Your Windows Username is : " + Username_info)
    
    file.write("\n")
    
    file.write("Your Email is : " + Email_info)
    
    file.write("\n")
    
    file.write("Your Windows & Email Password is :" + Password_info)
    
    file.write("\n")
    file.write("\n")
    file.write("The criterias to change your windows  password are:")
    file.write("\n")
    file.write("1- criterias")
    file.write("\n")
    file.write(" write your criteries ")
    file.write("\n")
    file.write("\n")


    file.write("Your Green Screen Username is : " + GreenScreen_info)
    
    file.write("\n")
    
    file.write("Your Green Screen Password is : " + GsPassword_info)
    
    file.write("\n")
    file.write("\n")
    file.write("It will ask you to change the password once you log in")
    file.write("\n")
    file.write("the Criterias are :")
    file.write("\n")
    file.write("criteria")


app = Tk()
 
app.geometry("500x500")



app.title("New User Information")
 
heading = Label(text="New User Information",fg="black",bg="yellow",width="500",height="3",font="10")
 
heading.pack()
 
firstname_text = Label(text="Windows Username : ")
Email_text = Label(text="Email : ")
password_text = Label(text="Password : ")
GreenScreen_text = Label(text="Green Screen Username : ")
GsPassword_text = Label(text="Green Screen Password : ")
 
firstname_text.place(x=15,y=80)
Email_text.place(x=15,y=140)
password_text.place(x=15,y=200)
GreenScreen_text.place(x=15,y=260)
GsPassword_text.place(x=15,y=320)

firstname = StringVar()
password = StringVar()
Email = StringVar()
GreenScreen = StringVar()
GsPassword = StringVar()

username_entry = Entry(textvariable=firstname,width="30")
password_name_entry = Entry(textvariable=lastname,width="30")
Email_entry = Entry(textvariable=Email,width="30")
GreenScreen_entry = Entry(textvariable=GreenScreen,width="30")
GsPassword_entry = Entry(textvariable=GsPassword,width="30")
 
username_entry.place(x=15,y=100)
Password_entry.place(x=15,y=160)
Email_entry.place(x=15,y=220)
GreenScreen_entry.place(x=15,y=280)
GsPassword_entry.place(x=15,y=340)
 
button = Button(app,text="Submit Data",command=save_info,width="20",height="2",bg="grey")
 
button.place(x=15,y=450)
 
 
mainloop()
