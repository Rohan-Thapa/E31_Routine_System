from tkinter import *
from tkinter import ttk, messagebox
from functools import partial

classes = [
    'ST4059CEM Legal and Ethical Foundations in Cyber Security',
    'ST4061CEM Programming and Algorithm 1 - Batch 30',
    'ST4065CEM Computer System & Networks',
    'Quiz'
]

options = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

routine = {
    "Sunday": [f"Time: 7:00-8:00 AM {classes[0]}", f"Time: 9:00 - 10:30 AM {classes[1]}"],
    "Monday": [f"Time: 7:00-8:00 AM {classes[2]}", f"Time: 9:00 - 10:30 AM {classes[1]}"],
    "Tuesday": [f"Time: 7:00-9:00 AM {classes[0]}"],
    "Wednesday": [f"Time: 8:00-9:00 AM {classes[2]}", f"Time: 9:00 - 10:30 AM {classes[1]}"],
    "Thursday": [f"Time: 7:00-8:00 AM {classes[2]}", f"Time: 9:00 - 10:30 AM {classes[1]}"],
    "Friday": [f"Time: 9:00-10:00 AM {classes[3]}"]
}

def show():
    day = clicked.get()
    if day == 'Saturday':
        messagebox.showerror("Opps!", "You have no classes in Saturday.")
        quit()

    lbl2.destroy()
    etn.destroy()
    drop.destroy()

    lbl3.config(text="Class Routine", font=("Arial", 16))
    for lecture in routine[day]:
        if len(routine[day]) == 1:
            grp1.config(cursor="hand2", text=classes[0])
        elif len(routine[day]) == 2:
            grp1.config(cursor="hand2", text=classes[0])
            grp2.config(cursor="hand2", text=classes[1])
        else:
            messagebox.showerror("Error", "There is the error in internal communication")

def details(event):
    info_text = f"Time: 7:00AM - 8:00AM\nClass: {classes[0]}\nLecturer: Manish Khanal"
    messagebox.showinfo("Detail info", info_text)

def main():
    root = Tk()
    root.title("Routine InfoSys")
    global clicked, grp1, grp2, lbl3, drop, etn, lbl2

    lbl1 = ttk.Label(root, text="Routine of Batch E31", font=('Arial', 18))
    lbl1.grid(row=0, column=0, padx=10, pady=5, columnspan=3)

    lbl2 = ttk.Label(root, text="Choose the day: ")
    lbl2.grid(row=1, column=0, padx=5)

    clicked = StringVar()
    clicked.set("Sunday")

    drop = ttk.OptionMenu(root, clicked, *options)
    drop.grid(row=1, column=1)

    etn = ttk.Button(root, text="Show result", command=show)
    etn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    lbl3 = Label(root, text="")
    lbl3.grid(row=3, column=0, columnspan=1, pady=5)

    grp1 = Label(root, text="", fg='blue')
    grp1.grid(row=4, column=0, columnspan=4, padx=5, pady=5)
    grp1.bind("<Button-1>", details)

    grp2 = Label(root, text="", fg='blue')
    grp2.grid(row=5, column=0, columnspan=4, padx=5, pady=5)
    grp2.bind("<Button-1>", details)

    root.mainloop()

if __name__ == '__main__':
    main()
