import tkinter as tk
import alarm

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("alarm")
        master.geometry("300x500+300+500")
        self.pack()
        self.create_widgets()

        #
        self.Alarms = [alarm.alarm() for i in range(2)]

    #todo: 1, 2を配列にできないか？
    def create_widgets(self):
        frame1 = tk.Frame(self.master, background="#ece")
        self.en1 = tk.Entry(frame1, text="entry1")
        self.en1.grid(row=0, column=0)
        self.boolvar1 = tk.BooleanVar()
        self.cb1 = tk.Checkbutton(frame1, text="ON", variable=self.boolvar1, command=lambda:self.change_state(0, self.boolvar1))
        self.cb1.grid(row=0, column=1)
        frame1.pack()

        frame2 = tk.Frame(self.master, background="#cec")
        self.en2 = tk.Entry(frame2, text="entry2")
        self.en2.grid(row=0, column=0)
        self.boolvar2 = tk.BooleanVar()
        self.cb2 = tk.Checkbutton(frame2, text="ON", variable=self.boolvar2, command=lambda:self.change_state(1, self.boolvar2))
        self.cb2.grid(row=0, column=1)
        frame2.pack()

    #check_button
    def change_state(self, id,  boolvar):
        if boolvar.get():
            print("ON")
            if id == 0:
                mozi = self.en1.get()
                print(mozi)
                #todo:マルチスレッドにする。
                self.Alarms[id].set_alarm(id, mozi)
            elif id == 1:
                mozi = self.en2.get()
                self.Alarms[id].set_alarm(id, mozi)
        else:
            pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()
