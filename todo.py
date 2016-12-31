import Tkinter
from Tkinter import *
import tkFileDialog

mainwindow = Tk()

# -------------------------------------------

mainwindow.geometry("340x400")
mainwindow.resizable(width=False, height=False)
mainwindow.title("Tudor Teodorescu's T-List")
# -------------------------------------------

task1 = StringVar()
task2 = StringVar()
task3 = StringVar()
task4 = StringVar()
task5 = StringVar()
task6 = StringVar()
task7 = StringVar()
task8 = StringVar()
task9 = StringVar()
task10 = StringVar()

# -------------------------------------------

first_element = Label(mainwindow, text="1.")
second_element = Label(mainwindow, text="2.")
third_element = Label(mainwindow, text="3.")
fourth_element = Label(mainwindow, text="4.")
fifth_element = Label(mainwindow, text="5.")
sixth_element = Label(mainwindow, text="6.")
seventh_element = Label(mainwindow, text="7.")
eightth_element = Label(mainwindow, text="8.")
nineth_element = Label(mainwindow, text="9.")
tenth_element = Label(mainwindow, text="10.")

# -------------------------------------------

def done1():
    finished_task1.config(textvariable=task1)
    task_1.delete(0, "end")
    print "Finished!"


def done2():
    finished_task2.config(textvariable=task2)
    task_2.delete(0, "end")
    print "Finished!"


def done3():
    finished_task3.config(textvariable=task3)
    task_3.delete(0, "end")
    print "Finished!"


def done4():
    finished_task4.config(textvariable=task4)
    task_4.delete(0, "end")
    print "Finished!"


def done5():
    finished_task5.config(textvariable=task5)
    task_5.delete(0, "end")
    print "Finished!"


def done6():
    finished_task6.config(textvariable=task6)
    task_6.delete(0, "end")
    print "Finished!"


def done7():
    finished_task7.config(textvariable=task7)
    task_7.delete(0, "end")
    print "Finished!"


def done8():
    finished_task8.config(textvariable=task8)
    task_8.delete(0, "end")
    print "Finished!"


def done9():
    finished_task9.config(textvariable=task9)
    task_9.delete(0, "end")
    print "Finished!"


def done10():
    finished_task10.config(textvariable=task10)
    task_10.delete(0, "end")
    print "Finished!"


def save_notes():
    file = tkFileDialog.asksaveasfile(
        parent=mainwindow,
        mode='w',
        defaultextension=".txt",
        filetypes=(
            ("All Files", "*.*"),
            ("Plain Text File", ".txt"),
            ("Hyper Text Markup Language(HTML) File", ".html"),
            ("Cascade Syle Sheet(CSS) File", ".css"),
            ("Stylus CSS Script", ".styl"),
            ("Extended Markup Language(XML)", ".xml"),
            ("PHP", ".php"),
            ("Python Script", ".py"),
            ("C++ File", ".cpp"),
            ("C++ Header File", ".h"),
            ("CSharp(C#) Source", ".cs"),
            ("Java Source", ".java"),
            ("Perl Script", ".prl"),
            ("JavaScript Object Notation File", ".json"),
            ("JavaScript Class Definition", ".cls"),
            ("Java Serverlet", ".do"),
            ("JavaScript Source", ".js"),
            ("Basic Source", ".bas"),
            ("Batch Script", ".bat"),
            ("Shell Script", ".sh"),
            ("Object File", ".o"),
        )
    )
    if file != "":
        data = notes_field.get('0.0', "end" + '-1c')
        file.write(data)
        file.close()


def load_notes():
    print "opening file dialog..."
    file = tkFileDialog.askopenfile(
        parent=mainwindow,
        mode="rb",
        title="Choose a file",
        filetypes=(
            ("All Files", "*.*"),
            ("Plain Text File", ".txt"),
            ("HTML File", ".html"),
            ("CSS File", ".css"),
            ("Stylus CSS Script", ".styl"),
            ("Extended Markup Language", ".xml"),
            ("PHP", ".php"),
            ("Python Script", ".py"),
            ("C++ File", ".cpp"),
            ("C++ Header File", ".h"),
            ("CSharp Source", ".cs"),
            ("Java Source", ".java"),
            ("Perl Script", ".prl"),
            ("JavaScript Object Notation File", ".json"),
            ("JavaScript Class Definition", ".cls"),
            ("Java Serverlet", ".do"),
            ("JavaScript Source", ".js"),
            ("Basic Source", ".bas"),
            ("Batch Script", ".bat"),
            ("Shell Script", ".sh"),
            ("Object File", ".o"),
        )
    )
    if file != "":
        contents = file.read()
        notes_field.delete("0.0", "end")
        notes_field.insert("1.0", contents)
        print ("file opened!")
        file.close()


def clear_notes():
    notes_field.delete("0.0", "end")
    
# -------------------------------------------

task_1 = Entry(mainwindow, textvariable=task1,)
task_2 = Entry(mainwindow, textvariable=task2,)
task_3 = Entry(mainwindow, textvariable=task3,)
task_4 = Entry(mainwindow, textvariable=task4,)
task_5 = Entry(mainwindow, textvariable=task5,)
task_6 = Entry(mainwindow, textvariable=task6,)
task_7 = Entry(mainwindow, textvariable=task7,)
task_8 = Entry(mainwindow, textvariable=task8,)
task_9 = Entry(mainwindow, textvariable=task9,)
task_10 = Entry(mainwindow,textvariable=task10,)

# -------------------------------------------

done_1 = Button(mainwindow, text="Done", command=done1)
done_2 = Button(mainwindow, text="Done", command=done2)
done_3 = Button(mainwindow, text="Done", command=done3)
done_4 = Button(mainwindow, text="Done", command=done4)
done_5 = Button(mainwindow, text="Done", command=done5)
done_6 = Button(mainwindow, text="Done", command=done6)
done_7 = Button(mainwindow, text="Done", command=done7)
done_8 = Button(mainwindow, text="Done", command=done8)
done_9 = Button(mainwindow, text="Done", command=done9)
done_10 = Button(mainwindow,text="Done", command=done10)

# -------------------------------------------

finished_task1 = Label(mainwindow, textvariable=task1)
finished_task2 = Label(mainwindow, textvariable=task2)
finished_task3 = Label(mainwindow, textvariable=task3)
finished_task4 = Label(mainwindow, textvariable=task4)
finished_task5 = Label(mainwindow, textvariable=task5)
finished_task6 = Label(mainwindow, textvariable=task6)
finished_task7 = Label(mainwindow, textvariable=task7)
finished_task8 = Label(mainwindow, textvariable=task8)
finished_task9 = Label(mainwindow, textvariable=task9)
finished_task10 = Label(mainwindow, textvariable=task10)

# -------------------------------------------

notes_lbl = Label(mainwindow, text="Notes")
notes_field = Text(mainwindow, height="8", width="48")
notes_scroll = Scrollbar(mainwindow)
notes_scroll.config(command=notes_field.yview)
notes_field.config(yscrollcommand=notes_scroll.set)

# save_list_btn = Button(mainwindow, command=save_list)
save_notes_btn = Button(mainwindow, command=save_notes, text="Save Note")
# load_list_btn = Button()
load_notes_btn = Button(mainwindow, command=load_notes, text="Load Note")
clear_notes_btn = Button(mainwindow, command=clear_notes, text="Clear Note Area")

# -------------------------------------------

first_element.grid(column="0", row="0")
second_element.grid(column="0", row="1")
third_element.grid(column="0", row="2")
fourth_element.grid(column="0", row="3")
fifth_element.grid(column="0", row="4")
sixth_element.grid(column="0", row="5")
seventh_element.grid(column="0", row="6")
eightth_element.grid(column="0", row="7")
nineth_element.grid(column="0", row="8")
tenth_element.grid(column="0", row="9")

task_1.grid(column="1", row="0")
task_2.grid(column="1", row="1")
task_3.grid(column="1", row="2")
task_4.grid(column="1", row="3")
task_5.grid(column="1", row="4")
task_6.grid(column="1", row="5")
task_7.grid(column="1", row="6")
task_8.grid(column="1", row="7")
task_9.grid(column="1", row="8")
task_10.grid(column="1", row="9")

done_1.grid(column="2", row="0")
done_2.grid(column="2", row="1")
done_3.grid(column="2", row="2")
done_4.grid(column="2", row="3")
done_5.grid(column="2", row="4")
done_6.grid(column="2", row="5")
done_7.grid(column="2", row="6")
done_8.grid(column="2", row="7")
done_9.grid(column="2", row="8")
done_10.grid(column="2", row="9")

finished_task1.grid(column="3", row="0")
finished_task2.grid(column="3", row="1")
finished_task3.grid(column="3", row="2")
finished_task4.grid(column="3", row="3")
finished_task5.grid(column="3", row="4")
finished_task6.grid(column="3", row="5")
finished_task7.grid(column="3", row="6")
finished_task8.grid(column="3", row="7")
finished_task9.grid(column="3", row="8")
finished_task10.grid(column="3", row="9")

notes_lbl.grid(column="0", row="10")
notes_field.place(x="0", y="274")

save_notes_btn.grid(column="0", row="11")
load_notes_btn.grid(column="1", row="11")
clear_notes_btn.grid(column="2", row="11")

# -------------------------------------------

mainwindow.mainloop()
