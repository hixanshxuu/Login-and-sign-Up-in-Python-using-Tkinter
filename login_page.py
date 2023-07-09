import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import mysql.connector


def validate_login():
    username = songInfo1.get()
    password = songInfo2.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter username and password.")
        return False

    # Check if the username and password exist in the database
    query = "SELECT * FROM login WHERE username = %s AND password = %s"
    values = (username, password)

    cur.execute(query, values)
    result = cur.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful.")
        #root.destroy()
        mainpage()

    else:
        messagebox.showerror("Error", "Invalid username or password.")


def mainpage():
    root.destroy()
    os.system("python hotel.py")


def forgot_password():
    global root_forgot

    root_forgot = tk.Tk()
    root_forgot.title("FORGOT PASSWORD")
    root_forgot.geometry("1550x800+0+0")

    forgot_frame = tk.Frame(root_forgot, bg="#2f2e2e", bd=25)
    forgot_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.2)

    forgot_label = tk.Label(forgot_frame, text="Forgot Password", font='Helvetica 14 bold', bg="#FAFAD2", fg='black')
    forgot_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    username_label = tk.Label(root_forgot, text="Username:", font='Helvetica 12 bold')
    username_label.place(relx=0.1, rely=0.4, relheight=0.1)

    username_entry = tk.Entry(root_forgot)
    username_entry.place(relx=0.35, rely=0.4, relwidth=0.5, relheight=0.1)

    password_label = tk.Label(root_forgot, text="Password:", font='Helvetica 12 bold')
    password_label.place(relx=0.1, rely=0.5, relheight=0.1)

    password_entry = tk.Entry(root_forgot)
    password_entry.place(relx=0.35, rely=0.5, relwidth=0.5, relheight=0.1)

    confirm_password_label = tk.Label(root_forgot, text="Confirm Password:", font='Helvetica 12 bold')
    confirm_password_label.place(relx=0.1, rely=0.6, relheight=0.1)

    confirm_password_entry = tk.Entry(root_forgot)
    confirm_password_entry.place(relx=0.35, rely=0.6, relwidth=0.5, relheight=0.1)

    def reset_password():
        if username_entry.get() == '' or password_entry.get() == '' or confirm_password_entry.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required', parent=root_forgot)
        elif password_entry.get() != confirm_password_entry.get():
            messagebox.showerror('Error', 'Password and confirm password do not match', parent=root_forgot)
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="kaushik@2918", database="python_connector")
            mycursor = con.cursor()
            query = 'SELECT * FROM login WHERE username=%s'
            mycursor.execute(query, (username_entry.get(),))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Incorrect Username', parent=root_forgot)
            else:
                query = 'UPDATE login SET password=%s WHERE username=%s'
                mycursor.execute(query, (password_entry.get(), username_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password has been reset. Please login with the new password',
                                    parent=root_forgot)
                root_forgot.destroy()

    reset_button = tk.Button(root_forgot, text="Reset Password", font='Helvetica 14 bold', bg='#FF5733', fg='white', command=reset_password)
    reset_button.place(relx=0.35, rely=0.7, relwidth=0.2, relheight=0.1)
    cancel_button = tk.Button(root_forgot, text="Cancel", font='Helvetica 14 bold',  bg='#FF5733', fg='white',command=root_forgot.destroy)
    cancel_button.place(relx=0.65, rely=0.7, relwidth=0.2, relheight=0.1)

    root_forgot.mainloop()


def login_pa():
    root.destroy()
    os.system("python signup.py")


def login_page():
    global img, songInfo1, songInfo2, con, cur, root

    root = tk.Tk()
    root.title("LOGIN PAGE")
    root.geometry("1550x800+0+0")

    con = mysql.connector.connect(host="localhost", user="root", password="kaushik@2918", database="python_connector")
    cur = con.cursor()

    headingFrame1 = tk.Frame(root, bg="#2f2e2e", bd=15)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = tk.Label(headingFrame1, text="Login to continue", font='Helvetica 14 bold', bg="#FAFAD2", fg='black')
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Frame(root, bg="#1abc9c")
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lb1 = tk.Label(labelFrame, text="Username:", font='Helvetica 13 bold', bg="#1abc9c", fg='white')
    lb1.place(relx=0.05, rely=0.3, relheight=0.08)

    songInfo1 = tk.Entry(labelFrame)
    songInfo1.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame, text="Password:", font='Helvetica 13 bold', bg="#1abc9c", fg='white')
    lb2.place(relx=0.05, rely=0.5, relheight=0.08)

    songInfo2 = Entry(labelFrame, show="*")
    songInfo2.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    loginBtn = Button(root, text="Login", font='Helvetica 12 bold', bg='#FF5733', fg='white', command=validate_login)
    loginBtn.place(relx=0.30, rely=0.7, relwidth=0.18, relheight=0.08)

    singupBtn = Button(root, text="Sign up", font='Helvetica 12 bold', bg='#FF5733', fg='white', command=login_pa)
    singupBtn.place(relx=0.10, rely=0.7, relwidth=0.18, relheight=0.08)

    forgotBtn = Button(root, text="Forgot Password", font='Helvetica 10 bold', bg='#FF5733', fg='white', command=forgot_password)
    forgotBtn.place(relx=0.50, rely=0.7, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font='Helvetica 12 bold', bg='#FF5733', fg='white', command=root.destroy)
    quitBtn.place(relx=0.70, rely=0.7, relwidth=0.18, relheight=0.08)

    root.mainloop()


login_page()
