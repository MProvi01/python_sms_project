import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

import mysql.connector

connection = None
def open_course_form():
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
        e5.delete(0, 'end')

        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']

        e1.insert(0, select[0])
        e2.insert(0, select[1])
        e3.insert(0, select[2])
        e4.insert(0, select[3])
        e5.insert(0, select[4])

    def Add():
        # id = e1.get()
        coursename = e2.get()
        coursecode = e3.get()
        vh = e4.get()
        lecturer = e5.get()

        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "INSERT INTO courses (coursename, coursecode, vh, lecturer) VALUES (%s,%s, %s, %s)"
            val = (coursename,coursecode, vh, lecturer)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("SUCCESS", "Course inserted successfully...")

            # Clear entry fields
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
            e5.delete(0, 'end')
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
        coursename = e2.get()
        coursecode = e3.get()
        vh = e4.get()
        lecturer = e5.get()

        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "UPDATE courses SET coursename=%s,coursecode=%s, vh=%s, lecturer=%s WHERE idcourse=%s"
            val = (coursename,coursecode, vh, lecturer, id)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Course Updated successfully...")

            # Clear entry fields
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
            e5.delete(0, 'end')
            e1.focus_set()
            # empty the treeview
            clear_treeview()
            # Refresh Treeview to show updated data
            show()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()

    def delete():
        numero = e1.get()
        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM courses WHERE idcourse=%s"
            val = (numero,)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("SUCCESS", "Student deleted successfully...")

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

        cursor.execute("SELECT idcourse, coursename, coursecode, vh, lecturer FROM courses")

        records = cursor.fetchall()

        for (idcourse, coursename, coursecode, vh, lecturer) in records:
            listBox.insert("", "end", values=(idcourse, coursename, coursecode, vh, lecturer))

        cursor.close()
    root = tk.Tk()
    root.geometry("1000x500")
    root.title("Courses")
    root.resizable(False, False)
    global e1
    global e2
    global e3
    global e4
    global e5

    tk.Label(root, text="courses", fg="Grey", font=(None, 20)).place(x=600, y=5)

    tk.Label(root, text="id").place(x=200, y=10)
    tk.Label(root, text="coursename").place(x=200, y=40)
    tk.Label(root, text="coursecode").place(x=200, y=70)
    tk.Label(root, text="vh").place(x=200, y=100)
    tk.Label(root, text="lecturer").place(x=200, y=130)


    def get_data(table):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM {table}")
        return cursor.fetchall()

    teachers = get_data('teachers')
    teacher_var = tk.StringVar()

    e1 = tk.Entry(root, width= 30)
    e1.place(x=330, y=10)

    e2 = tk.Entry(root, width= 30)
    e2.place(x=330, y=40)

    e3 = tk.Entry(root, width= 30)
    e3.place(x=330, y=70)

    e4 = tk.Entry(root, width= 30)
    e4.place(x=330, y=100)

    e5 = Combobox (root, width=27, textvariable=teacher_var)
    e5['values'] = [f"{name}" for name in teachers]
    e5.place(x=330, y=130)

    tk.Button(root, text="Add",command = Add,height=2, width= 13, bg='slate gray').place(x=200, y=160)
    tk.Button(root, text="update",command = update,height=2, width= 13, bg='slate gray').place(x=310, y=160)
    tk.Button(root, text="Delete",command = delete,height=2, width= 13, bg='orange red').place(x=420, y=160)

    cols = ('id','coursename', 'coursecode', 'vh', 'lecturer')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=1)
    listBox.place(x=10, y=230)

    show()  # Call to populate the Treeview

    def clear_treeview():
        # Clear all items from the Treeview
        for item in listBox .get_children():
            listBox .delete(item)

    listBox.bind('<Double-Button-1>', GetValue)

    root.mainloop()