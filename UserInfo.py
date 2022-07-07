
from doctest import master
from tkinter import *

def save_info():
    Username_info = firstname.get()
    Email_info = Email.get()
    Password_info = lastname.get()
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
    file.write("1- No Comon names or names related to you")
    file.write("\n")
    file.write("2- should be 14 characters long , containing at least one capital letter and numbers")
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
    file.write("should be 6 characters long , can`t start with number")


app = Tk()
 
app.geometry("500x500")



app.title("New User Information")
 
heading = Label(text="New User Information",fg="black",bg="yellow",width="500",height="3",font="10")
 
heading.pack()
 
firstname_text = Label(text="Windows Username : ")
Email_text = Label(text="Email : ")
lastname_text = Label(text="Password : ")
GreenScreen_text = Label(text="Green Screen Username : ")
GsPassword_text = Label(text="Green Screen Password : ")
 
firstname_text.place(x=15,y=80)
Email_text.place(x=15,y=140)
lastname_text.place(x=15,y=200)
GreenScreen_text.place(x=15,y=260)
GsPassword_text.place(x=15,y=320)

firstname = StringVar()
lastname = StringVar()
Email = StringVar()
GreenScreen = StringVar()
GsPassword = StringVar()

first_name_entry = Entry(textvariable=firstname,width="30")
last_name_entry = Entry(textvariable=lastname,width="30")
Email_entry = Entry(textvariable=Email,width="30")
GreenScreen_entry = Entry(textvariable=GreenScreen,width="30")
GsPassword_entry = Entry(textvariable=GsPassword,width="30")
 
first_name_entry.place(x=15,y=100)
last_name_entry.place(x=15,y=160)
Email_entry.place(x=15,y=220)
GreenScreen_entry.place(x=15,y=280)
GsPassword_entry.place(x=15,y=340)
 
button = Button(app,text="Submit Data",command=save_info,width="20",height="2",bg="grey")
 
button.place(x=15,y=450)
 
 
mainloop()