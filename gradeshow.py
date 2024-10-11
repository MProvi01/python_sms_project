import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

import mysql.connector

connection = None
def open_grade_table():
    def get_connection():
        global connection
        if connection is None or not connection.is_connected():
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="stud_manage")
        return connection

    def show():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT idgrade, student, course, grade FROM grades")

        records = cursor.fetchall()

        for (idgrade, student, course, grade) in records:
            listBox.insert("", "end", values=(idgrade, student, course, grade))

        cursor.close()

    root = tk.Tk()
    root.geometry("900x500")
    root.title("Grades Table")
    root.resizable(False, False)

    tk.Label(root, text="All the Grades", fg="Grey", font=(None, 20)).place(x=300, y=5)

    cols = ('idgrade','student', 'course', 'grade')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=1)
    listBox.place(x=10, y=50)

    show()
    root.mainloop()