import tkinter as tk
from students import open_student_form
from courses import open_course_form
from teachers import open_teacher_form
from grades import open_grade_form

def open_menu():
    # Create window
    window = tk.Tk()
    window.title("System Management")

    tk.Label(window, text="System Management", fg="Grey", font=(None, 20)).place(x=250, y=60)
    # button
    btn_student = tk.Button(window, text="Student form", command=open_student_form, height=3, width= 20, bg='slate gray')
    btn_student.place(x=50, y=150)

    btn_course = tk.Button(window, text="Course Form", command=open_course_form, height=3, width= 20, bg='slate gray')
    btn_course.place(x=210, y=150)

    btn_teachers = tk.Button(window, text="Teacher Form", command=open_teacher_form, height=3, width= 20, bg='slate gray')
    btn_teachers.place(x=370, y=150)

    btn_grades = tk.Button(window, text="Grades Form", command=open_grade_form, height=3, width= 20, bg='slate gray')
    btn_grades.place(x=530, y=150)

    window.geometry("800x500")
    window.resizable(False, False)
    window.mainloop()