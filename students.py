import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

connection = None

def open_student_form():
    # Function to initiate a MySQL connection
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
        numero = e1.get()
        name = e2.get()
        age = e3.get()
        courses = e4.get()
        password = e5.get()

        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "INSERT INTO students (numero, name, age, encourse, password) VALUES (%s, %s, %s, %s, %s)"
            val = (numero, name, age, courses, password)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("SUCCESS", "Sudent inserted successfully...")

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
        numero = e1.get()
        name = e2.get()
        age = e3.get()
        course = e4.get()

        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "UPDATE students SET name=%s, age=%s, encourse=%s WHERE numero=%s"
            val = (name, age, course, numero)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Student Updated successfully...")

            # Clear entry fields
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
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
        num = e1.get()
        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM students WHERE numero=%s"
            val = (num,)
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

        cursor.execute("SELECT numero, name, age, encourse FROM students")

        records = cursor.fetchall()

        for (numero, name, age, encourse ) in records:
            listBox.insert("", "end", values=(numero, name, age, encourse ))

        cursor.close()
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Students")
    root.resizable(False, False)
    global e1
    global e2
    global e3
    global e4

    tk.Label(root, text="Students", fg="Grey", font=(None, 20)).place(x=600, y=5)

    tk.Label(root, text="Numero").place(x=200, y=10)
    tk.Label(root, text="Name").place(x=200, y=40)
    tk.Label(root, text="Age").place(x=200, y=70)
    tk.Label(root, text="EnCourse").place(x=200, y=100)
    tk.Label(root, text="Password").place(x=200, y=130)

    e1 = tk.Entry(root, width= 30)
    e1.place(x=330, y=10)

    e2 = tk.Entry(root, width= 30)
    e2.place(x=330, y=40)

    e3 = tk.Entry(root, width= 30)
    e3.place(x=330, y=70)

    e4 = tk.Entry(root, width= 30)
    e4.place(x=330, y=100)

    e5 = tk.Entry(root, width= 30)
    e5.place(x=330, y=130)

    tk.Button(root, text="Add",command = Add,height=2, width= 13, bg='slate gray').place(x=200, y=160)
    tk.Button(root, text="update",command = update,height=2, width= 13, bg='slate gray').place(x=310, y=160)
    tk.Button(root, text="Delete",command = delete,height=2, width= 13, bg='orange red').place(x=420, y=160)

    cols = ('numero', 'name', 'age', 'encourse')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=1)
    listBox.place(x=10, y=230)

    show()

    def clear_treeview():
        # Clear all items from the Treeview
        for item in listBox .get_children():
            listBox .delete(item)

    listBox.bind('<Double-Button-1>', GetValue)

    root.mainloop()