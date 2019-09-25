import tkinter as tk
from tkinter import messagebox

class LoginFrame:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("DCM")

        self.master.geometry('320x200')
        self.label_username = tk.Label(self.master, text="Username")
        self.label_password = tk.Label(self.master, text="Password")

        self.entry_username = tk.Entry(self.master)
        self.entry_password = tk.Entry(self.master, show="*")

        self.label_username.grid(row=0)
        self.label_password.grid(row=1)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = tk.Checkbutton(self.master, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = tk.Button(self.master, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "john" and password == "password":
            self.new_window()
        else:
            messagebox.showerror("Login error", "Incorrect username/password")

class Demo1:
    def __init__(self, master):
        self.master = master
        self.master.title("3K04 DCM")
        #self.master.geometry('500x280')
        self.frame = tk.Frame(self.master)


    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x280')

        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.master.config(menu=self.menubar)

        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = LoginFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
