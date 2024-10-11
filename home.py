import tkinter as tk
from authadmin import open_adminauth
from authstudent import open_studauth

# Create window
window = tk.Tk()
window.title("welcome")

def close():
    window.destroy()

tk.Label(window, text="Welcome to Our App!", fg="Grey", font=(None, 20)).place(x=260, y=60)

btn_student = tk.Button(window, text="Connect as Student", command=open_studauth,font='calibri', height=4, width= 50, bg='peru')
btn_student.place(x=200, y=150)

btn_course = tk.Button(window, text=" Connect as Admin", command=open_adminauth,font='calibri', height=4, width= 50, bg='slate gray')
btn_course.place(x=200, y=250)

window.geometry("800x500")
window.resizable(False, False)
window.mainloop()