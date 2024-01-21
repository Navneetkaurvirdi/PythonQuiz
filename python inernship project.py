from tkinter import *
from PIL import Image, ImageTk

count = 0

root = Tk()

root.title("PYQUIZ")
root.geometry("1920x1080")
root.config(background="wheat4")

mylabel = Label(root, text="PYTHON QUIZ", foreground="black", font=("Helvetica", 50, "underline"), background="wheat4")
mylabel.place(x=550, y=30)

image = Image.open("C:\\Users\\nkvir\\OneDrive\\Desktop\\python.jpeg")
image = ImageTk.PhotoImage(image)

photo = Label(root, image=image, relief="solid", borderwidth=4)
photo.place(x=620, y=200)


def func():
    global count
    count = 0
    top = Toplevel()
    top.config(background="lavender")
    top.geometry("1920x1080")
    new = Label(top, text="Quiz Start", font=("Helvetica", 20, "underline"))
    new.place(x=650, y=30)

    # menu-driven question start

    # first is:
    l1 = Label(top, text="Ques1. Who is the Developer of Python?", font=("Helvetica", 15), background="lavender")
    l1.place(x=40, y=100)
    c1 = StringVar()
    c1.set(None)

    b1 = Radiobutton(top, text="Guido van Rossum", value="Guido van Rossum", variable=c1,
                     font=("Helvetica", 10), background="lavender")
    b1.place(x=110, y=150)

    b2 = Radiobutton(top, text="Dennis MacAlistair Ritchie", value="Dennis MacAlistair Ritchie", variable=c1,
                     font=("Helvetica", 10), background="lavender")
    b2.place(x=110, y=180)

    b3 = Radiobutton(top, text="Bjarne Stroustrup", value="Bjarne Stroustrup", variable=c1, font=("Helvetica", 10),
                      background="lavender")
    b3.place(x=110, y=210)

    def submit():
        global count
        selected_option = c1.get()
        if selected_option == 'Guido van Rossum':
            feedbackk = "Correct!"
            feedback_label1.config(text=feedbackk, foreground="blue")
            count += 1
        else:
            feedbackk = f"Wrong! The correct answer is: Guido van Rossum"
            feedback_label1.config(text=feedbackk, foreground="red")

    feedback_label1 = Label(top, text="", font=("Helvetica", 12), background="lavender")
    feedback_label1.place(x=40, y=250)

    s1 = Button(top, text="Submit", background="skyblue", foreground="black", command=submit)
    s1.place(x=350, y=310)

    # second question
    c2 = StringVar()
    c2.set(None)
    l2 = Label(top, text="Ques2. How List is Represented in Python?", font=("Helvetica", 15), background="lavender")
    l2.place(x=40, y=350)

    b4 = Radiobutton(top, text="[1,2,3,4,5]", value="[1,2,3,4,5]", variable=c2, font=("Helvetica", 10),
                      background="lavender")
    b4.place(x=110, y=400)

    b5 = Radiobutton(top, text="(1,2,3,4,5)", value="(1,2,3,4,5)", variable=c2, font=("Helvetica", 10),
                      background="lavender")
    b5.place(x=110, y=435)

    b6 = Radiobutton(top, text="{1,2,3,4,5}", value="{1,2,3,4,5}", variable=c2, font=("Helvetica", 10),
                      background="lavender")
    b6.place(x=110, y=470)

    def submit1():
        global count
        selected_option = c2.get()
        if selected_option == '[1,2,3,4,5]':
            feedback1 = "Correct!"
            feedback_label2.config(text=feedback1, foreground="blue")
            count += 1
        else:
            feedback1 = f"Wrong! The correct answer is: [1,2,3,4,5]"
            feedback_label2.config(text=feedback1, foreground="red")

    feedback_label2 = Label(top, text="", font=("Helvetica", 12), background="lavender")
    feedback_label2.place(x=40, y=550)

    s2 = Button(top, text="Submit", background="skyblue", foreground="black", command=submit1)
    s2.place(x=350, y=500)

    # third question
    c3 = StringVar()
    c3.set(None)
    l3 = Label(top, text="Ques3. How tuple is Represented in Python?", font=("Helvetica", 15), background="lavender")
    l3.place(x=40, y=600)

    b7 = Radiobutton(top, text="[1,2,3,4,5]", value="{1,2,3,4,5}", variable=c3, font=("Helvetica", 10),
                      background="lavender")
    b7.place(x=110, y=650)

    b8 = Radiobutton(top, text="(1,2,3,4,5)", value="[1,2,3,4,5]", variable=c3, font=("Helvetica", 10),
                      background="lavender")
    b8.place(x=110, y=680)

    b9 = Radiobutton(top, text="{1,2,3,4,5}", value="(1,2,3,4,5)", variable=c3, font=("Helvetica", 10),
                      background="lavender")
    b9.place(x=110, y=710)

    feedback_label3 = Label(top, text="", font=("Helvetica", 12), background="lavender")
    feedback_label3.place(x=40, y=750)

    def submit3():
        global count
        selected_option = c3.get()
        if selected_option == '(1,2,3,4,5)':
            ffeedback = "Correct"
            feedback_label3.config(text=ffeedback, foreground="blue")
            count += 1
        else:
            ffeedback = f"Wrong! The correct answer is: (1,2,3,4,5)"
            feedback_label3.config(text=ffeedback, foreground="red")

        a = Label(top, text=f"**RESULT IS**\nYou got {count} points out of 3.", font=("Helvetica", 15),
                  background="lavender")
        a.place(x=600, y=400)
        a.config(foreground="orchid4")

    s3 = Button(top, text="Submit", background="skyblue", foreground="black", command=submit3)
    s3.place(x=350, y=740)


b1 = Button(root, text="Click here to start", padx=50, pady=50, font=("Helvetica", 10), background="wheat3",
            activebackground="PeachPuff3", command=func)
b1.place(x=450, y=500)

b2 = Button(root, text="Click here to Quit ", padx=50, pady=50, font=("Helvetica", 10), background="wheat3",
            activebackground="PeachPuff3", command=quit)
b2.place(x=950, y=500)

root.mainloop()
