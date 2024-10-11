import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
connection = None

def open_teacher_form():

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
        name = e2.get()
        tel = e3.get()
        course = e4.get()

        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "INSERT INTO teachers(idteacher, name, telephone, course) VALUES (%s, %s, %s, %s)"
            val = (id, name, tel, course)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("SUCCESS", "Sudent inserted successfully...")

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
        name = e2.get()
        tel = e3.get()
        course = e4.get()

        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "UPDATE teachers SET name=%s, telephone=%s, course=%s WHERE idteacher=%s"
            val = ( name,tel, course,id)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Teacher Updated successfully...")

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
        id = e1.get()
        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM teachers WHERE idteacher=%s"
            val = (id)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("SUCCESS", "Teacher deleted successfully...")

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

        cursor.execute("SELECT idteacher, name, telephone, course FROM teachers")

        records = cursor.fetchall()

        for (idteacher, name, telephone, course) in records:
            listBox.insert("", "end", values=(idteacher, name, telephone, course))

        cursor.close()
    root = tk.Tk()
    root.geometry("850x500")
    root.title("Teachers")
    root.resizable(False, False)
    global e1
    global e2
    global e3
    global e4

    tk.Label(root, text="teacher", fg="Grey", font=(None, 20)).place(x=600, y=5)

    tk.Label(root, text="id").place(x=200, y=10)
    tk.Label(root, text="Name").place(x=200, y=40)
    tk.Label(root, text="telephone").place(x=200, y=70)
    tk.Label(root, text="Email").place(x=200, y=100)

    e1 = tk.Entry(root, width= 30)
    e1.place(x=330, y=10)

    e2 = tk.Entry(root, width= 30)
    e2.place(x=330, y=40)

    e3 = tk.Entry(root, width= 30)
    e3.place(x=330, y=70)

    e4 = tk.Entry(root, width= 30)
    e4.place(x=330, y=100)

    tk.Button(root, text="Add",command = Add,height=2, width= 13, bg='slate gray').place(x=200, y=130)
    tk.Button(root, text="update",command = update,height=2, width= 13, bg='slate gray').place(x=310, y=130)
    tk.Button(root, text="Delete",command = delete,height=2, width= 13, bg='orange red').place(x=420, y=130)

    cols = ('id', 'name', 'telephone', 'email')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)

    listBox.grid(row=1)
    listBox.place(x=10, y=200)

    show()  # Call to populate the Treeview

    def clear_treeview():
        # Clear all items from the Treeview
        for item in listBox .get_children():
            listBox .delete(item)

    listBox.bind('<Double-Button-1>', GetValue)

    root.mainloop()