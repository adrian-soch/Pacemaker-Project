import tkinter as tk
from tkinter import messagebox
import pickle


login_dict = {}
class WelcomeFrame:
    def __init__(self, master):
        self.master = master
        self.master.configure(background='grey')
        self.frame = tk.Frame(self.master)
        self.master.title("DCM")
        self.master.geometry('400x200')
        self.master.resizable(width=False, height=False)
        self.label_welcome = tk.Label(self.master, text="Welcome")
        self.label_welcome.configure(background='grey')
        self.label_welcome.grid(row=1,column=2,columnspan =1,padx = 80, pady = 10)

        self.nxtbtn = tk.Button(self.master, text="Next", width=12, command=self._nxt_btn_clicked)
        self.nxtbtn.grid(row=3,column=2,columnspan =1,padx = 80, pady = 10)
        self.nxtbtn.focus()

    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)

    def _nxt_btn_clicked(self):
        self.new_window(LoginFrame)
        self.master.withdraw()

class LoginFrame:
    def __init__(self, master):
        self.master = master
        self.master.configure(background='grey')
        self.frame = tk.Frame(self.master)
        self.master.title("DCM")
        self.master.resizable(width=False, height=False)

        #self.master.geometry('300x200')
        self.label_username = tk.Label(self.master, text="Username")
        self.label_username.configure(background='grey')
        self.label_password = tk.Label(self.master, text="Password")
        self.label_password.configure(background='grey')

        self.master.columnconfigure(0, pad=20)
        self.master.columnconfigure(1, pad=20)
        self.master.columnconfigure(2, pad=20)
        self.master.columnconfigure(3, pad=20)

        self.master.rowconfigure(0, pad=3)
        self.master.rowconfigure(1, pad=3)
        self.master.rowconfigure(2, pad=3)
        self.master.rowconfigure(3, pad=3)
        self.master.rowconfigure(4, pad=3)
        self.master.rowconfigure(5, pad=3)

        self.entry_username = tk.Entry(self.master)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_username.focus()

        self.label_username.grid(row=0, sticky='e', pady=5)
        self.label_password.grid(row=1, sticky='e', pady=10)
        self.entry_username.grid(row=0, column=1, columnspan = 1,sticky='w')
        self.entry_password.grid(row=1, column=1, columnspan = 1,sticky='w')

        self.logbtn = tk.Button(self.master, text="Login", width=12, command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2, padx = 80, pady = 0)

        self.add_userbtn = tk.Button(self.master, text="Add user",width =12, command=self._add_user_btn_clicked)
        self.add_userbtn.grid(columnspan =2,padx = 80, pady = 10)

        self.login_successful = 000

    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)

    def _add_user_btn_clicked(self):
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')

        self.new_window(AddUserWindow)

    def _login_btn_clicked(self):
        global login_dict
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')

        for key in login_dict:
            if key == username and password == login_dict[key]:
                self.login_successful = 111
                self.new_window(MainWindow)
                self.master.withdraw()
                #self.close_windows()
                break

        if self.login_successful != 111:
            messagebox.showerror("Login error", "Incorrect username/password")

    def close_windows(self):
        self.master.destroy()


class MainWindow:
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
        sys.exit

class AddUserWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry('300x200')
        self.quitButton = tk.Button(self.master, text = 'Quit', width = 12, command = self.close_windows)
        self.label_username = tk.Label(self.master, text="Enter New Username")
        self.label_password = tk.Label(self.master, text="Enter New Password")

        self.entry_username = tk.Entry(self.master)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_username.focus()

        self.label_username.grid(row=0, sticky='e', pady=5)
        self.label_password.grid(row=1, sticky='e', pady=10)
        self.entry_username.grid(row=0, column=1, columnspan = 1,sticky='w')
        self.entry_password.grid(row=1, column=1, columnspan = 1,sticky='w')

        self.add_userbtn = tk.Button(self.master, text="Add user",width =12, command=self._add_user_btn_clicked)
        self.add_userbtn.grid(row=2,column=1,pady=10)

        self.quitButton = tk.Button(self.master, text = 'Quit', width = 12, command = self.close_windows)
        self.quitButton.grid(row=3,column=1,pady=5)

    def _add_user_btn_clicked(self):
        global login_dict
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        
        # 10 Users + admin
        if(len(username) and len(password) and len(login_dict)<11):
            login_dict[username] = password
            writeUsers()
            messagebox.showinfo("Success", "User Added")
            self.quitButton.focus()
        else:
            messagebox.showerror("Error", "Maximum allowed user limit reached")
    def close_windows(self):
        self.master.destroy()

def readUsers():
    global login_dict
    with open('DCM/HACKERS_DONT_LOOK_HERE.pickle', 'rb') as file:
        login_dict =  pickle.load(file)
        print(login_dict)

def writeUsers():
    global login_dict
    print(login_dict)
    with open('DCM/HACKERS_DONT_LOOK_HERE.pickle', 'wb') as file:
        pickle.dump(login_dict,file)

def main():
    try:
        readUsers()
    except (EOFError):
        pass
    root = tk.Tk()
    app = WelcomeFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
