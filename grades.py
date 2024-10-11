import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

import mysql.connector

connection = None
def open_grade_form():
    def get_connection():
        global connection
        if connection is None or not connection.is_connected():
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="stud_manage")
        return connection

    def GetValue(event):
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e3.delete(0, 'end')
        e4.delete(0, 'end')

        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']

        e1.insert(0, select[0])
        e2.insert(0, select[1])
        e3.insert(0, select[2])
        e4.insert(0, select[3])

    def Add():
        id = e1.get()
        student = e2.get()
        course = e3.get()
        grade = e4.get()

        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "INSERT INTO grades(student, course, grade) VALUES (%s, %s, %s)"
            val = (student, course, grade)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("SUCCESS", "Grade inserted successfully...")

            # Clear entry fields
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
            e1.focus_set()

            clear_treeview()

            show()

        except Exception as e:
            print(e)
            conn.rollback()

        finally:
            cursor.close()

    def update():
        id = e1.get()
        student = e2.get()
        course = e3.get()
        grade = e4.get()

        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "UPDATE grades SET student=%s, course=%s, grade=%s WHERE idgrade=%s"
            val = (student, course, grade, id)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Grade Updated successfully...")

            # Clear entry fields
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
            e1.focus_set()
            clear_treeview()
            show()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()

    def delete():
        id = e1.get()
        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM grades WHERE idgrade=%s"
            val = (id,)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("SUCCESS", "Grade deleted successfully...")

            # Clear entry fields
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
            e1.focus_set()

            clear_treeview()

            show()

        except Exception as e:
            print(e)
            conn.rollback()

        finally:
            cursor.close()

    def show():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT idgrade, student, course, grade FROM grades")

        records = cursor.fetchall()

        for (idgrade, student, course, grade) in records:
            listBox.insert("", "end", values=(idgrade, student, course, grade))

        cursor.close()

    root = tk.Tk()
    root.geometry("800x500")
    root.title("Grades")
    root.resizable(False, False)
    global e1
    global e2
    global e3
    global e4

    tk.Label(root, text="Grades", fg="Grey", font=(None, 20)).place(x=600, y=5)

    tk.Label(root, text="idgrade").place(x=200, y=10)
    tk.Label(root, text="Student").place(x=200, y=40)
    tk.Label(root, text="Course").place(x=200, y=70)
    tk.Label(root, text="Grade").place(x=200, y=100)

    #value for combo box
    def get_data_stud(table):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT numero, name FROM {table}")
        return cursor.fetchall()

    def get_data_course(table):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT coursename, coursecode FROM {table}")
        return cursor.fetchall()

    students = get_data_stud('students')
    courses = get_data_course('courses')

    # Création des listes déroulantes
    stud_var = tk.StringVar()
    course_var = tk.StringVar()

    e1 = tk.Entry(root, width=30)
    e1.place(x=330, y=10)

    e2 = Combobox(root, width=27, textvariable=stud_var)
    e2['values'] = [f"{name} - {numero}" for name, numero in students]
    e2.place(x=330, y=40)

    e3 = Combobox(root, width=27, textvariable=course_var)
    e3['values'] = [f"{coursename} - {coursecode}" for coursename, coursecode in courses]
    e3.place(x=330, y=70)

    e4 = tk.Entry(root, width=30)
    e4.place(x=330, y=100)

    tk.Button(root, text="Add", command=Add, height=2, width=13, bg='slate gray').place(x=200, y=130)
    tk.Button(root, text="update", command=update, height=2, width=13, bg='slate gray').place(x=310, y=130)
    tk.Button(root, text="Delete", command=delete, height=2, width=13, bg='orange red').place(x=420, y=130)

    cols = ('idgrade','student', 'course', 'grade')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=1)
    listBox.place(x=10, y=200)

    show()

    def clear_treeview():
        # Clear all items from the Treeview
        for item in listBox.get_children():
            listBox.delete(item)

    listBox.bind('<Double-Button-1>', GetValue)

    root.mainloop()