from pynput.mouse import Button, Controller
import threading, time
import tkinter as tk

FONT = ("", 10)
TEXT = 0

class Base():
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry("720x720")
        self.app.minsize(720,720)
        self.app.title("Clicker")
        self.select = Select(self.app)
        self.app.mainloop()

class Select():
    def __init__(self,app):
        self.e = threading.Event()
        self.app=app
        self.create_frame()
        self.create_widget()
        
    def create_frame(self):
        self.frame_0=tk.Frame(self.app)
        self.frame_0.pack(side=tk.TOP)
        self.frame_1=tk.Frame(self.app)
        self.frame_1.pack()
        self.frame_2=tk.Frame(self.app)
        self.frame_2.pack()
        self.frame_3=tk.Frame(self.app)
        self.frame_3.pack()

    def create_widget(self):
        self.create_text0(self.frame_0)
        self.create_text1(self.frame_1)
        self.create_text2(self.frame_2)
        self.create_textEntry(self.frame_2)
        self.create_button(self.frame_3)

    def create_text0(self,master):
        self.text0=tk.Label(
            master,
            height=6,
            width=12,
            text="Clicker",
            font=("", 30)
        )
        self.text0.grid(column=0,row=0)

    def create_text1(self,master):
        f=open('./nop/introduction.txt','r')
        data = f.read()
        f.close()
        self.text1=tk.Label(
            master,
            text="========================"
        )
        self.text1.pack(side=tk.TOP)
        self.text2=tk.Label(
            master,
            text=data,
        )
        self.text2.pack(side=tk.TOP)
        self.text3=tk.Label(
            master,
            text="========================"
        )
        self.text3.pack(side=tk.TOP)

    def create_text2(self,master):
        self.text4=tk.Label(
            master,
            text="時間(s)"
        )
        self.text4.grid(column=0,row=0)

    def create_textEntry(self,master):
        global TEXT
        self.txE=tk.Entry(
            master,
            width=20
            )
        self.txE.grid(column=1,row=0)
        TEXT = self.txE.get()

    def create_button(self,master):
        self.button0=tk.Button(
            master,
            height=6,
            width=12,
            text="スタート",
            command=self.hits
        )
        self.button0.pack()

    def hits(self):
        while not self.e.isSet():        # e.set()が実行されるまでFalseを返す
            Controller().click(Button.left)     # 左ボタンをクリックする
            time.sleep(10)   # 1秒待ち
        threading.Thread(target=self.hits, args=(self.e,)).start()
        # input()     # 入力待ち
        # self.e.set() 

if __name__ == "__main__":
    base = Base()
