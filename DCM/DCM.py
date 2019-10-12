import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle

login_dict = {}
aooLowerRateLimit = "123"
aooUpperRateLimit = "123"
aooAtrialAmplitude = "123"
aooAtrialPulseWidth = "123"

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
        
    def on_exit(self):
        exit()


class LoginFrame:
    def __init__(self, master):
        self.master = master
        self.master.configure(background='grey')
        self.frame = tk.Frame(self.master)
        self.master.title("USER LOGIN")
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

        self.login_successful = False

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
                self.login_successful = True
                self.master.withdraw()
                self.new_window(MainWindow)
                break

        if self.login_successful != True:
            messagebox.showerror("Login error", "Incorrect username/password")


class AddUserWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry('300x200')
        self.quitButton = tk.Button(self.master, text = 'Quit', width = 12, command = self.close_windows)
        self.label_username = tk.Label(self.master, text="Enter New Username")
        self.label_password = tk.Label(self.master, text="Enter New Password")
        self.label_password2 = tk.Label(self.master, text="Confirm Password")

        self.entry_username = tk.Entry(self.master)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password2 = tk.Entry(self.master, show="*")
        self.entry_username.focus()

        self.label_username.grid(row=0, sticky='e', pady=5)
        self.label_password.grid(row=1, sticky='e', pady=10)
        self.label_password2.grid(row=2, sticky='w', pady=10)
        self.entry_username.grid(row=0, column=1, columnspan = 1,sticky='w')
        self.entry_password.grid(row=1, column=1, columnspan = 1,sticky='w')
        self.entry_password2.grid(row=2, column=1, columnspan = 1,sticky='w')

        self.add_userbtn = tk.Button(self.master, text="Add user",width =12, command=self._add_user_btn_clicked)
        self.add_userbtn.grid(row=3,column=1,pady=10)

        self.quitButton = tk.Button(self.master, text = 'Back', width = 12, command = self.close_windows)
        self.quitButton.grid(row=4,column=1,pady=5)

        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

    def on_exit(self):
        self.master.destroy()
        #changed here: press quit wont close the program but close the window

    def _add_user_btn_clicked(self):
        global login_dict
        username = self.entry_username.get()
        password = self.entry_password.get()
        password2 = self.entry_password2.get()
        userExists = False
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.entry_password2.delete(0, 'end')
        
        if(password == password2):
            for key in login_dict:
                if(key == username):
                    userExists = True
             # 10 Users
            if(not(userExists) and len(username) and len(password) and len(login_dict)<11):
                login_dict[username] = password
                writeUsers()
                messagebox.showinfo("Success", "User Added")
                self.quitButton.focus()
            else:
                if(not(len(username) and len(password))):
                    messagebox.showerror("Error", "Missing Username and/or Password")
                elif(userExists):
                    messagebox.showerror("Error", "User exists")
                else:
                    messagebox.showerror("Error", "Maximum allowed user limit reached")
        
        else:
            messagebox.showerror("Error", "Passwords do not match")

    def close_windows(self):
        self.master.destroy()


class MainWindow:
    def __init__(self, master):
        self.content = tk.Entry()
        self.master = master
        self.master.geometry('500x570')
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
        self.aooLowerRateLimitButton = tk.Button(self.aoo, text = "Set", command=self.setValue)
        self.aooUpperRateLimitButton = tk.Button(self.aoo, text = "Set", command=self.setValue)
        self.aooAtrialAmplitudeButton = tk.Button(self.aoo, text = "Set", command=self.setValue)
        self.aooAtrialPulseWidthButton = tk.Button(self.aoo, text = "Set", command=self.setValue)

        self.aooLowerRateLimitLabel = tk.Label(self.aoo, text = "Lower Rate Limit")
        self.aooUpperRateLimitLabel = tk.Label(self.aoo, text = "Upper Rate Limit")
        self.aooAtrialAmplitudeLabel = tk.Label(self.aoo, text = "Atrial Amplitude")
        self.aooAtrialPulseWidthLabel = tk.Label(self.aoo, text = "Atrial Pulse Width")

        self.aooLowerRateLimitValue = tk.Label(self.aoo, text = "Current Value: " + aooLowerRateLimit)
        self.aooUpperRateLimitValue = tk.Label(self.aoo, text = "Current Value: " + aooUpperRateLimit)
        self.aooAtrialAmplitudeValue = tk.Label(self.aoo, text = "Current Value: " + aooAtrialAmplitude)
        self.aooAtrialPulseWidthValue = tk.Label(self.aoo, text = "Current Value: " + aooAtrialPulseWidth)
    
        self.aooLowerRateLimitEntry = tk.Entry(self.aoo)
        self.aooUpperRateLimitEntry = tk.Entry(self.aoo)
        self.aooAtrialAmplitudeEntry = tk.Entry(self.aoo)
        self.aooAtrialPulseWidthEntry = tk.Entry(self.aoo)

        self.aooLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.aooLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.aooLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.aooLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        self.aooUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.aooUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.aooUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.aooUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)
        self.aooAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.aooAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.aooAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.aooAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        self.aooAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.aooAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.aooAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.aooAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)


        #VOO
        self.vooLowerRateLimitButton = tk.Button(self.voo, text = "Set", command=self.setValue)
        self.vooUpperRateLimitButton = tk.Button(self.voo, text = "Set", command=self.setValue)
        self.vooAtrialAmplitudeButton = tk.Button(self.voo, text = "Set", command=self.setValue)
        self.vooAtrialPulseWidthButton = tk.Button(self.voo, text = "Set", command=self.setValue)

        self.vooLowerRateLimitLabel = tk.Label(self.voo, text = "Lower Rate Limit")
        self.vooUpperRateLimitLabel = tk.Label(self.voo, text = "Upper Rate Limit ")
        self.vooAtrialAmplitudeLabel = tk.Label(self.voo, text = "Ventricular Amplitude")
        self.vooAtrialPulseWidthLabel = tk.Label(self.voo, text = "Ventricular Pulse Width")

        self.vooLowerRateLimitValue = tk.Label(self.voo, text = "Current Value: "+"123")
        self.vooUpperRateLimitValue = tk.Label(self.voo, text = "Current Value: "+"123")
        self.vooAtrialAmplitudeValue = tk.Label(self.voo, text = "Current Value: "+"123")
        self.vooAtrialPulseWidthValue = tk.Label(self.voo, text = "Current Value: "+"123")

        self.vooLowerRateLimitEntry = tk.Entry(self.voo)
        self.vooUpperRateLimitEntry = tk.Entry(self.voo)
        self.vooAtrialAmplitudeEntry = tk.Entry(self.voo)
        self.vooAtrialPulseWidthEntry = tk.Entry(self.voo)

        self.vooLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.vooLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.vooLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.vooLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        self.vooUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.vooUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.vooUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.vooUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)
        self.vooAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.vooAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.vooAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.vooAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        self.vooAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.vooAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.vooAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.vooAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)


        #AAI
        self.aaiLowerRateLimitButton = tk.Button(self.aai, text = "Set", command=self.setValue)
        self.aaiUpperRateLimitButton = tk.Button(self.aai, text = "Set", command=self.setValue)
        self.aaiAtrialAmplitudeButton = tk.Button(self.aai, text = "Set", command=self.setValue)
        self.aaiAtrialPulseWidthButton = tk.Button(self.aai, text = "Set", command=self.setValue)
        self.aaiAtrialSensitivityButton = tk.Button(self.aai, text = "Set", command=self.setValue)
        self.aaiARPButton = tk.Button(self.aai, text = "Set", command=self.setValue)
        self.aaiAPVARPButton = tk.Button(self.aai, text = "Set", command=self.setValue)
        self.aaiHysteresisButton = tk.Button(self.aai, text = "Set", command=self.setValue)
        self.aaiRateSmoothingButton = tk.Button(self.aai, text = "Set", command=self.setValue)

        self.aaiLowerRateLimitLabel = tk.Label(self.aai, text = "Lower Rate Limit")
        self.aaiUpperRateLimitLabel = tk.Label(self.aai, text = "Upper Rate Limit ")
        self.aaiAtrialAmplitudeLabel = tk.Label(self.aai, text = "Atrial Amplitude")
        self.aaiAtrialPulseWidthLabel = tk.Label(self.aai, text = "Atrial Pulse Width")
        self.aaiAtrialSensitivityLabel = tk.Label(self.aai, text = "Atrial Sensitivity")
        self.aaiARPLabel = tk.Label(self.aai, text = "ARP")
        self.aaiAPVARPLabel = tk.Label(self.aai, text = "APVARP")
        self.aaiHysteresisLabel = tk.Label(self.aai, text = "Hysteresis")
        self.aaiRateSmoothingLabel = tk.Label(self.aai, text = "Rate Smoothing")

        self.aaiLowerRateLimitValue = tk.Label(self.aai, text = "Current Value: "+"123")
        self.aaiUpperRateLimitValue = tk.Label(self.aai, text = "Current Value: "+"123")
        self.aaiAtrialAmplitudeValue = tk.Label(self.aai, text = "Current Value: "+"123")
        self.aaiAtrialPulseWidthValue = tk.Label(self.aai, text = "Current Value: "+"123")
        self.aaiAtrialSensitivityValue = tk.Label(self.aai, text = "Current Value: "+"123")
        self.aaiARPValue = tk.Label(self.aai, text = "Current Value: "+"123")
        self.aaiAPVARPValue = tk.Label(self.aai, text = "Current Value: "+"123")
        self.aaiHysteresisValue = tk.Label(self.aai, text = "Current Value: "+"123")
        self.aaiRateSmoothingValue = tk.Label(self.aai, text = "Current Value: "+"123")

        self.aaiLowerRateLimitEntry = tk.Entry(self.aai)
        self.aaiUpperRateLimitEntry = tk.Entry(self.aai)
        self.aaiAtrialAmplitudeEntry = tk.Entry(self.aai)
        self.aaiAtrialPulseWidthEntry = tk.Entry(self.aai)
        self.aaiAtrialSensitivityEntry = tk.Entry(self.aai)
        self.aaiARPEntry = tk.Entry(self.aai)
        self.aaiAPVARPEntry = tk.Entry(self.aai)
        self.aaiHysteresisEntry = tk.Entry(self.aai)
        self.aaiRateSmoothingEntry = tk.Entry(self.aai)
        
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
        self.aaiAtrialSensitivityLabel.grid(row=4, column=0, padx=15, pady=15)
        self.aaiAtrialSensitivityEntry.grid(row=4, column=1, padx=15, pady=15)
        self.aaiAtrialSensitivityButton.grid(row=4, column=2, padx=15, pady=15)
        self.aaiARPLabel.grid(row=5, column=0, padx=15, pady=15)
        self.aaiARPEntry.grid(row=5, column=1, padx=15, pady=15)
        self.aaiARPButton.grid(row=5, column=2, padx=15, pady=15)
        self.aaiAPVARPLabel.grid(row=6, column=0, padx=15, pady=15)
        self.aaiAPVARPEntry.grid(row=6, column=1, padx=15, pady=15)
        self.aaiAPVARPButton.grid(row=6, column=2, padx=15, pady=15)
        self.aaiHysteresisLabel.grid(row=7, column=0, padx=15, pady=15)
        self.aaiHysteresisEntry.grid(row=7, column=1, padx=15, pady=15)
        self.aaiHysteresisButton.grid(row=7, column=2, padx=15, pady=15)
        self.aaiRateSmoothingLabel.grid(row=8, column=0, padx=15, pady=15)
        self.aaiRateSmoothingEntry.grid(row=8, column=1, padx=15, pady=15)
        self.aaiRateSmoothingButton.grid(row=8, column=2, padx=15, pady=15)

        self.aaiLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        self.aaiUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)
        self.aaiAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        self.aaiAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        self.aaiAtrialSensitivityValue.grid(row=4, column=3, padx=15, pady=15)
        self.aaiARPValue.grid(row=5, column=3, padx=15, pady=15)
        self.aaiAPVARPValue.grid(row=6, column=3, padx=15, pady=15)
        self.aaiHysteresisValue.grid(row=7, column=3, padx=15, pady=15)
        self.aaiRateSmoothingValue.grid(row=8, column=3, padx=15, pady=15)
        

        #VVI
        self.vviLowerRateLimitButton = tk.Button(self.vvi, text = "Set", command=self.setValue)
        self.vviUpperRateLimitButton = tk.Button(self.vvi, text = "Set", command=self.setValue)
        self.vviAtrialAmplitudeButton = tk.Button(self.vvi, text = "Set", command=self.setValue)
        self.vviAtrialPulseWidthButton = tk.Button(self.vvi, text = "Set", command=self.setValue)
        self.vviAtrialSensitivityButton = tk.Button(self.vvi, text = "Set", command=self.setValue)
        self.vviARPButton = tk.Button(self.vvi, text = "Set", command=self.setValue)
        self.vviAPVARPButton = tk.Button(self.vvi, text = "Set", command=self.setValue)
        self.vviHysteresisButton = tk.Button(self.vvi, text = "Set", command=self.setValue)
        self.vviRateSmoothingButton = tk.Button(self.vvi, text = "Set", command=self.setValue)

        self.vviLowerRateLimitLabel = tk.Label(self.vvi, text = "Lower Rate Limit")
        self.vviUpperRateLimitLabel = tk.Label(self.vvi, text = "Upper Rate Limit ")
        self.vviAtrialAmplitudeLabel = tk.Label(self.vvi, text = "Ventricular Amplitude")
        self.vviAtrialPulseWidthLabel = tk.Label(self.vvi, text = "Ventricular Pulse Width")
        self.vviAtrialSensitivityLabel = tk.Label(self.vvi, text = "Ventricular Sensitivity")
        self.vviARPLabel = tk.Label(self.vvi, text = "VRP")
        self.vviHysteresisLabel = tk.Label(self.vvi, text = "Hysteresis")
        self.vviRateSmoothingLabel = tk.Label(self.vvi, text = "Rate Smoothing")

        self.vviLowerRateLimitValue = tk.Label(self.vvi, text = "Current Value: "+"123")
        self.vviUpperRateLimitValue = tk.Label(self.vvi, text = "Current Value: "+"123")
        self.vviAtrialAmplitudeValue = tk.Label(self.vvi, text = "Current Value: "+"123")
        self.vviAtrialPulseWidthValue = tk.Label(self.vvi, text = "Current Value: "+"123")
        self.vviAtrialSensitivityValue = tk.Label(self.vvi, text = "Current Value: "+"123")
        self.vviARPValue = tk.Label(self.vvi, text = "Current Value: "+"123")
        self.vviHysteresisValue = tk.Label(self.vvi, text = "Current Value: "+"123")
        self.vviRateSmoothingValue = tk.Label(self.vvi, text = "Current Value: "+"123")

        self.vviLowerRateLimitEntry = tk.Entry(self.vvi)
        self.vviUpperRateLimitEntry = tk.Entry(self.vvi)
        self.vviAtrialAmplitudeEntry = tk.Entry(self.vvi)
        self.vviAtrialPulseWidthEntry = tk.Entry(self.vvi)
        self.vviAtrialSensitivityEntry = tk.Entry(self.vvi)
        self.vviARPEntry = tk.Entry(self.vvi)
        self.vviHysteresisEntry = tk.Entry(self.vvi)
        self.vviRateSmoothingEntry = tk.Entry(self.vvi)

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
        self.vviAtrialSensitivityLabel.grid(row=4, column=0, padx=15, pady=15)
        self.vviAtrialSensitivityEntry.grid(row=4, column=1, padx=15, pady=15)
        self.vviAtrialSensitivityButton.grid(row=4, column=2, padx=15, pady=15)
        self.vviARPLabel.grid(row=5, column=0, padx=15, pady=15)
        self.vviARPEntry.grid(row=5, column=1, padx=15, pady=15)
        self.vviARPButton.grid(row=5, column=2, padx=15, pady=15)
        self.vviHysteresisLabel.grid(row=6, column=0, padx=15, pady=15)
        self.vviHysteresisEntry.grid(row=6, column=1, padx=15, pady=15)
        self.vviHysteresisButton.grid(row=6, column=2, padx=15, pady=15)
        self.vviRateSmoothingLabel.grid(row=7, column=0, padx=15, pady=15)
        self.vviRateSmoothingEntry.grid(row=7, column=1, padx=15, pady=15)
        self.vviRateSmoothingButton.grid(row=7, column=2, padx=15, pady=15)

        self.vviLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        self.vviUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)
        self.vviAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        self.vviAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        self.vviAtrialSensitivityValue.grid(row=4, column=3, padx=15, pady=15)
        self.vviARPValue.grid(row=5, column=3, padx=15, pady=15)
        self.vviHysteresisValue.grid(row=6, column=3, padx=15, pady=15)
        self.vviRateSmoothingValue.grid(row=7, column=3, padx=15, pady=15)


        self.tab_parent.pack(expand = 1, fill='both')

        self.confirmButton = tk.Button(self.aoo, text = 'Confirm', width = 20, command = self.confirmChanges)
        self.confirmButton.grid(row = 4, column = 1)

        self.confirmButton = tk.Button(self.voo, text = 'Confirm', width = 20, command = self.confirmChanges)
        self.confirmButton.grid(row = 4, column = 1)
        
        self.confirmButton = tk.Button(self.aai, text = 'Confirm', width = 20, command = self.confirmChanges)
        self.confirmButton.grid(row = 9, column = 1)

        self.confirmButton = tk.Button(self.vvi, text = 'Confirm', width = 20, command = self.confirmChanges)
        self.confirmButton.grid(row = 8, column = 1)

        self.quitButton = tk.Button(self.aoo, text = 'LogOff', width = 12, command = self.logOff)
        self.quitButton.grid(row=5,column=1,pady=5)
        self.quitButton = tk.Button(self.voo, text = 'LogOff', width = 12, command = self.logOff)
        self.quitButton.grid(row=5,column=1,pady=5)
        self.quitButton = tk.Button(self.aai, text = 'LogOff', width = 12, command = self.logOff)
        self.quitButton.grid(row=10,column=1,pady=5)
        self.quitButton = tk.Button(self.vvi, text = 'LogOff', width = 12, command = self.logOff)
        self.quitButton.grid(row=10,column=1,pady=5)

    def confirmChanges(self):
        '''global aooLowerRateLimit, aooUpperRateLimit, aooAtrialAmplitude, aooAtrialPulseWidth
        aooLowerRateLimit = str(self.aooLowerRateLimitEntry.get())
        aooUpperRateLimit = str(self.aooUpperRateLimitEntry.get())
        aooAtrialAmplitude = str(self.aooAtrialAmplitudeEntry.get())
        aooAtrialPulseWidth = str(self.aooAtrialPulseWidth.get())'''
        if messagebox.askyesno("Confirmation", "Upload these changes?"):
            messagebox.showinfo("Done", "Success")

    
    def setValue(self):
        '''a = self.aooLowerRateLimitEntry.get()
        print(a)
        currentValue.set(a)'''
        if messagebox.askyesno("Confirmation", "Upload these changes?"):
            messagebox.showinfo("Done", "Success")

    def logOff(self):
        if messagebox.askyesno("LogOff", "Do you want to log off?"):
            self.master.destroy()
            main()  

    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            exit()
    def close_windows(self):
        self.master.destroy()
        exit()


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
