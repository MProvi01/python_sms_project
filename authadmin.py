import tkinter as tk
from tkinter import messagebox
import mysql.connector
from menu import open_menu
# import bcrypt
connection = None

def open_adminauth():

    def get_connection():
        global connection
        if connection is None or not connection.is_connected():
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="stud_manage")
        return connection

    def authentication():
        username = username_entry.get()
        password = password_entry.get()

        conn = get_connection()
        cursor = conn.cursor()

        # Récupération du user en bd
        cursor.execute("SELECT password FROM admins WHERE username=%s", (username,))
        result = cursor.fetchone()

        if result:
            # hashed_password = result[0]
            bd_password = result[0]
            # if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            if (password == bd_password):
                # messagebox.showinfo("Success", "SUCCESSFULLY CONNECTED")
                auth_window.destroy()
                open_menu()
            else:
                messagebox.showerror ("Error", "incorrect password")
        else:
            messagebox.showerror("Error", "User and/or Password is incorrect")

    auth_window = tk.Tk()
    auth_window.title("Admin Authentication")

    tk.Label(auth_window, text="Admin Connection", fg="Grey", font=(None, 18)).place(x=250, y=100)

    username_label = tk.Label(auth_window, text="Username:")
    username_label.place(x=200, y=150)
    username_entry = tk.Entry(auth_window,  width= 30)
    username_entry.place(x=300, y=150)

    password_label = tk.Label(auth_window, text="Password:")
    password_label.place(x=200, y=190)
    password_entry = tk.Entry(auth_window,  width= 30,show="*")
    password_entry.place(x=300, y=190)

    # Btn
    login_button = tk.Button(auth_window, text="Connect", command=authentication, height=2, width= 40, bg='slate gray')
    login_button.place(x=200, y=240)

    auth_window.geometry("800x500")
    auth_window.resizable(False, False)
    auth_window.mainloop()