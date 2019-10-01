import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle


login_dict = {}
class WelcomeFrame:
    def __init__(self, master):
        self.master = master
        self.master.configure(background='grey')
        self.frame = tk.Frame(self.master)
        self.master.title("DCM")
        self.master.resizable(width=False, height=False)
        self.label_welcome = tk.Label(self.master, text="Welcome")
        self.label_welcome.config(font=("Helvetica",34))
        self.label_welcome.configure(background='grey')
        self.label_welcome.grid(row=1,column=2,columnspan =1,padx = 200, pady = 20)

        self.nxtbtn = tk.Button(self.master, text="Next", width=12, command=self._nxt_btn_clicked)
        self.nxtbtn.grid(row=3,column=2,columnspan =1,padx = 200, pady = 20)
        self.nxtbtn.focus()

    #return button bind
        self.master.bind('<Return>', self.return_bind)
        
    def return_bind(self, event):
        self._nxt_btn_clicked()
    #return button bind end

    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)

    def _nxt_btn_clicked(self):
        self.master.withdraw()
        self.new_window(LoginFrame)
        


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

        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

    #return button bind
        self.master.bind('<Return>', self.return_bind)
        
    def return_bind(self, event):
        self._login_btn_clicked()
    #return button bind end



    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            exit()

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
                self.master.withdraw()
                self.new_window(MainWindow)
                break

        if self.login_successful != 111:
            messagebox.showerror("Login error", "Incorrect username/password")


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x280')
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.master.config(menu=self.menubar)
        self.frame = tk.Frame(self.master)

        # AOO, VOO, AAI, and VVI
        self.tab_parent = ttk.Notebook(self.master)
        self.aoo = ttk.Frame(self.tab_parent)
        self.voo = ttk.Frame(self.tab_parent)
        self.aai = ttk.Frame(self.tab_parent)
        self.vvi = ttk.Frame(self.tab_parent)

        self.tab_parent.add(self.aoo, text = "AOO")
        self.tab_parent.add(self.voo, text = "VOO")
        self.tab_parent.add(self.aai, text = "AAI")
        self.tab_parent.add(self.vvi, text = "VVI")

        #Put in attributes here
        #AOO
        self.aooLowerRateLimitButton = tk.Button(self.aoo, text = "Set")
        self.aooUpperRateLimitButton = tk.Button(self.aoo, text = "Set")
        self.aooAtrialAmplitudeButton = tk.Button(self.aoo, text = "Set")
        self.aooAtrialPulseWidthButton = tk.Button(self.aoo, text = "Set")
        self.aooLowerRateLimitLabel = tk.Label(self.aoo, text = "Lower Rate Limit")
        self.aooUpperRateLimitLabel = tk.Label(self.aoo, text = "Upper Rate Limit ")
        self.aooAtrialAmplitudeLabel = tk.Label(self.aoo, text = "Atrial Amplitude")
        self.aooAtrialPulseWidthLabel = tk.Label(self.aoo, text = "Atrial Pulse Width")
        self.aooLowerRateLimitEntry = tk.Entry(self.aoo)
        self.aooUpperRateLimitEntry = tk.Entry(self.aoo)
        self.aooAtrialAmplitudeEntry = tk.Entry(self.aoo)
        self.aooAtrialPulseWidthEntry = tk.Entry(self.aoo)
        self.aooLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.aooLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.aooLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.aooUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.aooUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.aooUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.aooAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.aooAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.aooAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.aooAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.aooAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.aooAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)

        #VOO
        self.vooLowerRateLimitButton = tk.Button(self.voo, text = "Set")
        self.vooUpperRateLimitButton = tk.Button(self.voo, text = "Set")
        self.vooAtrialAmplitudeButton = tk.Button(self.voo, text = "Set")
        self.vooAtrialPulseWidthButton = tk.Button(self.voo, text = "Set")
        self.vooLowerRateLimitLabel = tk.Label(self.voo, text = "Lower Rate Limit")
        self.vooUpperRateLimitLabel = tk.Label(self.voo, text = "Upper Rate Limit ")
        self.vooAtrialAmplitudeLabel = tk.Label(self.voo, text = "Atrial Amplitude")
        self.vooAtrialPulseWidthLabel = tk.Label(self.voo, text = "Atrial Pulse Width")
        self.vooLowerRateLimitEntry = tk.Entry(self.voo)
        self.vooUpperRateLimitEntry = tk.Entry(self.voo)
        self.vooAtrialAmplitudeEntry = tk.Entry(self.voo)
        self.vooAtrialPulseWidthEntry = tk.Entry(self.voo)
        self.vooLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.vooLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.vooLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.vooUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.vooUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.vooUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.vooAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.vooAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.vooAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.vooAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.vooAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.vooAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)

        #AAI
        self.aaiLowerRateLimitButton = tk.Button(self.aai, text = "Set")
        self.aaiUpperRateLimitButton = tk.Button(self.aai, text = "Set")
        self.aaiAtrialAmplitudeButton = tk.Button(self.aai, text = "Set")
        self.aaiAtrialPulseWidthButton = tk.Button(self.aai, text = "Set")
        self.aaiLowerRateLimitLabel = tk.Label(self.aai, text = "Lower Rate Limit")
        self.aaiUpperRateLimitLabel = tk.Label(self.aai, text = "Upper Rate Limit ")
        self.aaiAtrialAmplitudeLabel = tk.Label(self.aai, text = "Atrial Amplitude")
        self.aaiAtrialPulseWidthLabel = tk.Label(self.aai, text = "Atrial Pulse Width")
        self.aaiLowerRateLimitEntry = tk.Entry(self.aai)
        self.aaiUpperRateLimitEntry = tk.Entry(self.aai)
        self.aaiAtrialAmplitudeEntry = tk.Entry(self.aai)
        self.aaiAtrialPulseWidthEntry = tk.Entry(self.aai)
        self.aaiLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.aaiLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.aaiLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.aaiUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.aaiUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.aaiUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.aaiAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.aaiAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.aaiAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.aaiAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.aaiAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.aaiAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)

        #VVI
        self.vviLowerRateLimitButton = tk.Button(self.vvi, text = "Set")
        self.vviUpperRateLimitButton = tk.Button(self.vvi, text = "Set")
        self.vviAtrialAmplitudeButton = tk.Button(self.vvi, text = "Set")
        self.vviAtrialPulseWidthButton = tk.Button(self.vvi, text = "Set")
        self.vviLowerRateLimitLabel = tk.Label(self.vvi, text = "Lower Rate Limit")
        self.vviUpperRateLimitLabel = tk.Label(self.vvi, text = "Upper Rate Limit ")
        self.vviAtrialAmplitudeLabel = tk.Label(self.vvi, text = "Atrial Amplitude")
        self.vviAtrialPulseWidthLabel = tk.Label(self.vvi, text = "Atrial Pulse Width")
        self.vviLowerRateLimitEntry = tk.Entry(self.vvi)
        self.vviUpperRateLimitEntry = tk.Entry(self.vvi)
        self.vviAtrialAmplitudeEntry = tk.Entry(self.vvi)
        self.vviAtrialPulseWidthEntry = tk.Entry(self.vvi)
        self.vviLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.vviLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.vviLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.vviUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.vviUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.vviUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.vviAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.vviAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.vviAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.vviAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.vviAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.vviAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)

        self.tab_parent.pack(expand = 1, fill='both')

        #self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        #self.quitButton.pack()
        #self.frame.pack()

    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            exit()
    def close_windows(self):
        self.master.destroy()
        exit()

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

        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            exit()

    def _add_user_btn_clicked(self):
        global login_dict
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        
        # 10 Users
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
    try:
        with open('HACKERS_DONT_LOOK_HERE.pickle', 'rb') as file:
            login_dict =  pickle.load(file)
            print(login_dict)
    except(FileNotFoundError):
        with open('DCM/HACKERS_DONT_LOOK_HERE.pickle', 'rb') as file:
            login_dict =  pickle.load(file)
            print(login_dict)

def writeUsers():
    global login_dict
    print(login_dict)
    try:
        with open('HACKERS_DONT_LOOK_HERE.pickle', 'wb') as file:
            pickle.dump(login_dict,file)
    except(FileNotFoundError):
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
