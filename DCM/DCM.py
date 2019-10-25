#Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle

#Creating empty dictionaries to later load users and values into
login_dict = {}
user0, user1, user2, user3, user4, user5, user6, user7, user8, user9 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

#Initializing all global variables with "0"
#AOO
aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry = "0","0","0","0"
 
#VOO
voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_atrialAmplitudeEntry,voo_atrialPulseWidthEntry = "0","0","0","0"

#AAI
aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_APVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry = "0","0","0","0","0","0","0","0","0"

#VVI
vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_atrialAmplitudeEntry,vvi_atrialPulseWidthEntry,vvi_atrialSensitivityEntry,vvi_ARPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry = "0","0","0","0","0","0","0","0"

#Creating Initial Welcome Frame
class WelcomeFrame:
    def __init__(self, master):
        
        #General paramters
        self.master = master
        self.master.configure(background='grey')
        self.frame = tk.Frame(self.master)
        self.master.title("DCM")
        self.master.resizable(width=False, height=False)

        #Label details
        self.label_welcome = tk.Label(self.master, text="Welcome")
        self.label_welcome.config(font=("Helvetica",34))
        self.label_welcome.configure(background='grey')
        self.label_welcome.grid(row=1,column=2,columnspan =1,padx = 200, pady = 20)

        #Next window button
        self.nxtbtn = tk.Button(self.master, text="Next", width=12, command=self._nxt_btn_clicked)
        self.nxtbtn.grid(row=3,column=2,columnspan =1,padx = 200, pady = 20)
        self.nxtbtn.focus()

        #Return button binding
        self.master.bind('<Return>', self.return_bind)
    
    #Return Button method
    def return_bind(self, event):
        self._nxt_btn_clicked()

    #Method to create new window
    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)

    #Method to transition to loginframe
    def _nxt_btn_clicked(self):
        self.master.withdraw()
        self.new_window(LoginFrame)     
    
    #Method to cleanup closing window
    def on_exit(self):
        exit()

#Login Frame window
class LoginFrame:
    def __init__(self, master):

        #General parameters
        self.master = master
        self.master.configure(background='grey')
        self.frame = tk.Frame(self.master)
        self.master.title("USER LOGIN")
        self.master.resizable(width=False, height=False)

        #Label details
        self.label_username = tk.Label(self.master, text="Username")
        self.label_username.configure(background='grey')
        self.label_password = tk.Label(self.master, text="Password")
        self.label_password.configure(background='grey')

        #Window positioning
        self.master.rowconfigure(0, pad=3)
        self.master.rowconfigure(1, pad=3)
        self.master.rowconfigure(2, pad=3)
        self.master.rowconfigure(3, pad=3)
        self.master.rowconfigure(4, pad=3)
        self.master.rowconfigure(5, pad=3)

        #Enter username/password details
        self.entry_username = tk.Entry(self.master)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_username.focus()
        self.label_username.grid(row=0, sticky='e', pady=5)
        self.label_password.grid(row=1, sticky='e', pady=10)
        self.entry_username.grid(row=0, column=1, columnspan = 1,sticky='w')
        self.entry_password.grid(row=1, column=1, columnspan = 1,sticky='w')

        #Add user and login button details
        self.logbtn = tk.Button(self.master, text="Login", width=12, command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2, padx = 80, pady = 0)
        self.add_userbtn = tk.Button(self.master, text="Add user",width =12, command=self._add_user_btn_clicked)
        self.add_userbtn.grid(columnspan =2,padx = 80, pady = 10)
        self.login_successful = False
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

        #Return button bind
        self.master.bind('<Return>', self.return_bind)

    #Return button method  
    def return_bind(self, event):
        self._login_btn_clicked()

    #Method to cleanup closing application
    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            exit()

    #Method to create new window
    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)

    #Method to add transition to add new user screen
    def _add_user_btn_clicked(self):
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.new_window(AddUserWindow)

    #Method to for login button
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

#Add new user class window
class AddUserWindow:
    def __init__(self, master):
        #Setting default window parameters
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

        #Adjusting window and button spacing
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

    #Method for clean exit 
    def on_exit(self):
        self.master.destroy()

    #Method for clicking add user
    def _add_user_btn_clicked(self):
        global login_dict
        username = self.entry_username.get()
        password = self.entry_password.get()
        password2 = self.entry_password2.get()
        userExists = False
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.entry_password2.delete(0, 'end')
        
        #Password verification
        if(password == password2):
            for key in login_dict:
                if(key == username):
                    userExists = True
            
            #Ensures only 10 users can be added
            if(not(userExists) and len(username) and len(password) and len(login_dict)<11):
                login_dict[username] = password
                writeUsers()
                messagebox.showinfo("Success", "User Added")
                self.quitButton.focus()
            else:
                #Ensures user parameters are valid
                if(not(len(username) and len(password))):
                    messagebox.showerror("Error", "Missing Username and/or Password")
                elif(userExists):
                    messagebox.showerror("Error", "User exists")
                else:
                    messagebox.showerror("Error", "Maximum allowed user limit reached")
        
        else:
            messagebox.showerror("Error", "Passwords do not match")

    #Method for closing window
    def close_windows(self):
        self.master.destroy()

#Class for main window
class MainWindow:
    def __init__(self, master):
        #General window setup
        self.content = tk.Entry()
        self.master = master
        self.master.geometry('500x570')
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.master.config(menu=self.menubar)
        self.frame = tk.Frame(self.master)

        # Tabs created for AOO, VOO, AAI, and VVI 
        self.tab_parent = ttk.Notebook(self.master)
        self.aoo = ttk.Frame(self.tab_parent)
        self.voo = ttk.Frame(self.tab_parent)
        self.aai = ttk.Frame(self.tab_parent)
        self.vvi = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.aoo, text = "AOO")
        self.tab_parent.add(self.voo, text = "VOO")
        self.tab_parent.add(self.aai, text = "AAI")
        self.tab_parent.add(self.vvi, text = "VVI")

        #AOO BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #Setup buttons
        self.aooLowerRateLimitButton = tk.Button(self.aoo, text = "Set", command= lambda: self.setValue("aooLowerRateLimit"))
        self.aooUpperRateLimitButton = tk.Button(self.aoo, text = "Set", command= lambda: self.setValue("aooUpperRateLimit"))
        self.aooAtrialAmplitudeButton = tk.Button(self.aoo, text = "Set", command= lambda: self.setValue("aooAtrialAmplitude"))
        self.aooAtrialPulseWidthButton = tk.Button(self.aoo, text = "Set", command= lambda: self.setValue("aooAtrialPulseWidth"))

        #Setup labels for inputs
        self.aooLowerRateLimitLabel = tk.Label(self.aoo, text = "Lower Rate Limit")
        self.aooUpperRateLimitLabel = tk.Label(self.aoo, text = "Upper Rate Limit")
        self.aooAtrialAmplitudeLabel = tk.Label(self.aoo, text = "Atrial Amplitude")
        self.aooAtrialPulseWidthLabel = tk.Label(self.aoo, text = "Atrial Pulse Width")

        #Setup  labels to display values
        self.aooLowerRateLimitValue = tk.Label(self.aoo, text = "Current Value: " + aoo_lowerRateLimitEntry)
        self.aooUpperRateLimitValue = tk.Label(self.aoo, text = "Current Value: " + aoo_upperRateLimitEntry)
        self.aooAtrialAmplitudeValue = tk.Label(self.aoo, text = "Current Value: " + aoo_atrialAmplitudeEntry)
        self.aooAtrialPulseWidthValue = tk.Label(self.aoo, text = "Current Value: " + aoo_atrialPulseWidthEntry)
    
        #Setup entry field
        self.aooLowerRateLimitEntry = tk.Entry(self.aoo)
        self.aooUpperRateLimitEntry = tk.Entry(self.aoo)
        self.aooAtrialAmplitudeEntry = tk.Entry(self.aoo)
        self.aooAtrialPulseWidthEntry = tk.Entry(self.aoo)

        #Adjust positioning
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
        #AOO END-------------------------------------------------------------------------------------------------------------------------------

        #VOO BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #Setup buttons
        self.vooLowerRateLimitButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooLowerRateLimit"))
        self.vooUpperRateLimitButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooUpperRateLimit"))
        self.vooAtrialAmplitudeButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooAtrialAmplitude"))
        self.vooAtrialPulseWidthButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooAtrialPulseWidth"))
        
        #Setup labels for inputs
        self.vooLowerRateLimitLabel = tk.Label(self.voo, text = "Lower Rate Limit")
        self.vooUpperRateLimitLabel = tk.Label(self.voo, text = "Upper Rate Limit ")
        self.vooAtrialAmplitudeLabel = tk.Label(self.voo, text = "Ventricular Amplitude")
        self.vooAtrialPulseWidthLabel = tk.Label(self.voo, text = "Ventricular Pulse Width")

        #Setup  labels to display values
        self.vooLowerRateLimitValue = tk.Label(self.voo, text = "Current Value: "+ voo_lowerRateLimitEntry)
        self.vooUpperRateLimitValue = tk.Label(self.voo, text = "Current Value: "+ voo_upperRateLimitEntry)
        self.vooAtrialAmplitudeValue = tk.Label(self.voo, text = "Current Value: "+ voo_atrialAmplitudeEntry)
        self.vooAtrialPulseWidthValue = tk.Label(self.voo, text = "Current Value: "+ voo_atrialPulseWidthEntry)

        #Setup entry field
        self.vooLowerRateLimitEntry = tk.Entry(self.voo)
        self.vooUpperRateLimitEntry = tk.Entry(self.voo)
        self.vooAtrialAmplitudeEntry = tk.Entry(self.voo)
        self.vooAtrialPulseWidthEntry = tk.Entry(self.voo)

        #Adjust positioning
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
        #VOO END-------------------------------------------------------------------------------------------------------------------------------

        #AAI BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #Setup buttons
        self.aaiLowerRateLimitButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiLowerRateLimit"))
        self.aaiUpperRateLimitButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiUpperRateLimit"))
        self.aaiAtrialAmplitudeButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiAtrialAmplitude"))
        self.aaiAtrialPulseWidthButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiAtrialPulseWidth"))
        self.aaiAtrialSensitivityButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiAtrialSensitivity"))
        self.aaiARPButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiARP"))
        self.aaiAPVARPButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiAPVARP"))
        self.aaiHysteresisButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiHysteresis"))
        self.aaiRateSmoothingButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiRateSmoothing"))

        #Setup labels for inputs
        self.aaiLowerRateLimitLabel = tk.Label(self.aai, text = "Lower Rate Limit")
        self.aaiUpperRateLimitLabel = tk.Label(self.aai, text = "Upper Rate Limit ")
        self.aaiAtrialAmplitudeLabel = tk.Label(self.aai, text = "Atrial Amplitude")
        self.aaiAtrialPulseWidthLabel = tk.Label(self.aai, text = "Atrial Pulse Width")
        self.aaiAtrialSensitivityLabel = tk.Label(self.aai, text = "Atrial Sensitivity")
        self.aaiARPLabel = tk.Label(self.aai, text = "ARP")
        self.aaiAPVARPLabel = tk.Label(self.aai, text = "APVARP")
        self.aaiHysteresisLabel = tk.Label(self.aai, text = "Hysteresis")
        self.aaiRateSmoothingLabel = tk.Label(self.aai, text = "Rate Smoothing")

        #Setup  labels to display values
        self.aaiLowerRateLimitValue = tk.Label(self.aai, text = "Current Value: "+ aai_lowerRateLimitEntry)
        self.aaiUpperRateLimitValue = tk.Label(self.aai, text = "Current Value: "+ aai_upperRateLimitEntry)
        self.aaiAtrialAmplitudeValue = tk.Label(self.aai, text = "Current Value: "+ aai_atrialAmplitudeEntry)
        self.aaiAtrialPulseWidthValue = tk.Label(self.aai, text = "Current Value: "+ aai_atrialPulseWidthEntry)
        self.aaiAtrialSensitivityValue = tk.Label(self.aai, text = "Current Value: "+ aai_atrialSensitivityEntry)
        self.aaiARPValue = tk.Label(self.aai, text = "Current Value: "+ aai_ARPEntry)
        self.aaiAPVARPValue = tk.Label(self.aai, text = "Current Value: "+ aai_APVARPEntry)
        self.aaiHysteresisValue = tk.Label(self.aai, text = "Current Value: "+ aai_hysteresisEntry)
        self.aaiRateSmoothingValue = tk.Label(self.aai, text = "Current Value: "+ aai_rateSmoothingEntry)

        #Setup entry field
        self.aaiLowerRateLimitEntry = tk.Entry(self.aai)
        self.aaiUpperRateLimitEntry = tk.Entry(self.aai)
        self.aaiAtrialAmplitudeEntry = tk.Entry(self.aai)
        self.aaiAtrialPulseWidthEntry = tk.Entry(self.aai)
        self.aaiAtrialSensitivityEntry = tk.Entry(self.aai)
        self.aaiARPEntry = tk.Entry(self.aai)
        self.aaiAPVARPEntry = tk.Entry(self.aai)
        self.aaiHysteresisEntry = tk.Entry(self.aai)
        self.aaiRateSmoothingEntry = tk.Entry(self.aai)

        #Adjust positioning
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
        #AAI END-------------------------------------------------------------------------------------------------------------------------------


        #VVI BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #Setup buttons
        self.vviLowerRateLimitButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviLowerRateLimit"))
        self.vviUpperRateLimitButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviUpperRateLimit"))
        self.vviAtrialAmplitudeButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviAtrialAmplitude"))
        self.vviAtrialPulseWidthButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviAtrialPulseWidth"))
        self.vviAtrialSensitivityButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviAtrialSensitivity"))
        self.vviARPButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviARP"))
        self.vviHysteresisButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviHysteresis"))
        self.vviRateSmoothingButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviRateSmoothing"))

        #Setup labels for inputs
        self.vviLowerRateLimitLabel = tk.Label(self.vvi, text = "Lower Rate Limit")
        self.vviUpperRateLimitLabel = tk.Label(self.vvi, text = "Upper Rate Limit ")
        self.vviAtrialAmplitudeLabel = tk.Label(self.vvi, text = "Ventricular Amplitude")
        self.vviAtrialPulseWidthLabel = tk.Label(self.vvi, text = "Ventricular Pulse Width")
        self.vviAtrialSensitivityLabel = tk.Label(self.vvi, text = "Ventricular Sensitivity")
        self.vviARPLabel = tk.Label(self.vvi, text = "VRP")
        self.vviHysteresisLabel = tk.Label(self.vvi, text = "Hysteresis")
        self.vviRateSmoothingLabel = tk.Label(self.vvi, text = "Rate Smoothing")

        #Setup  labels to display values
        self.vviLowerRateLimitValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_lowerRateLimitEntry)
        self.vviUpperRateLimitValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_upperRateLimitEntry)
        self.vviAtrialAmplitudeValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_atrialAmplitudeEntry)
        self.vviAtrialPulseWidthValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_atrialPulseWidthEntry)
        self.vviAtrialSensitivityValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_atrialSensitivityEntry)
        self.vviARPValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_ARPEntry)
        self.vviHysteresisValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_hysteresisEntry)
        self.vviRateSmoothingValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_rateSmoothingEntry)

        #Setup entry field
        self.vviLowerRateLimitEntry = tk.Entry(self.vvi)
        self.vviUpperRateLimitEntry = tk.Entry(self.vvi)
        self.vviAtrialAmplitudeEntry = tk.Entry(self.vvi)
        self.vviAtrialPulseWidthEntry = tk.Entry(self.vvi)
        self.vviAtrialSensitivityEntry = tk.Entry(self.vvi)
        self.vviARPEntry = tk.Entry(self.vvi)
        self.vviHysteresisEntry = tk.Entry(self.vvi)
        self.vviRateSmoothingEntry = tk.Entry(self.vvi)

        #Adjust positioning
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
        #VVI END-------------------------------------------------------------------------------------------------------------------------------

        #Position tabs properly
        self.tab_parent.pack(expand = 1, fill='both')

        #Setup confirm buttons
        self.confirmButton = tk.Button(self.aoo, text = 'Confirm', width = 20, command = self.confirmChanges)
        self.confirmButton.grid(row = 4, column = 1)
        self.confirmButton = tk.Button(self.voo, text = 'Confirm', width = 20, command = self.confirmChanges)
        self.confirmButton.grid(row = 4, column = 1)
        self.confirmButton = tk.Button(self.aai, text = 'Confirm', width = 20, command = self.confirmChanges)
        self.confirmButton.grid(row = 9, column = 1)
        self.confirmButton = tk.Button(self.vvi, text = 'Confirm', width = 20, command = self.confirmChanges)
        self.confirmButton.grid(row = 8, column = 1)

        #Setup logoff button
        self.quitButton = tk.Button(self.aoo, text = 'LogOff', width = 12, command = self.logOff)
        self.quitButton.grid(row=5,column=1,pady=5)
        self.quitButton = tk.Button(self.voo, text = 'LogOff', width = 12, command = self.logOff)
        self.quitButton.grid(row=5,column=1,pady=5)
        self.quitButton = tk.Button(self.aai, text = 'LogOff', width = 12, command = self.logOff)
        self.quitButton.grid(row=10,column=1,pady=5)
        self.quitButton = tk.Button(self.vvi, text = 'LogOff', width = 12, command = self.logOff)
        self.quitButton.grid(row=10,column=1,pady=5)

    #Confirm changes method
    def confirmChanges(self):
        if messagebox.askyesno("Confirmation", "Upload these changes?"):
            messagebox.showinfo("Done", "Success")

    #New window method
    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)

    #Method to set value
    def setValue(self,value):

        #Global Variables
        #AOO
        global aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry 
        #VOO
        global voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_atrialAmplitudeEntry,voo_atrialPulseWidthEntry
        #AAI
        global aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_APVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry
        #VVI
        global vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_atrialAmplitudeEntry,vvi_atrialPulseWidthEntry,vvi_atrialSensitivityEntry,vvi_ARPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry

        #AOO
        #aooLowerRateLimit
        if(value == "aooLowerRateLimit"):
            temp = self.aooLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(self.aooLowerRateLimitEntry.get()) >= int(aoo_upperRateLimitEntry) and int(aoo_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("Error","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aoo_lowerRateLimitEntry = temp
                        self.aooLowerRateLimitValue.config(text="Current Value: " + aoo_lowerRateLimitEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aooUpperRateLimit
        if(value == "aooUpperRateLimit"):
            temp = self.aooUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(aoo_lowerRateLimitEntry) >= int(self.aooUpperRateLimitEntry.get()) and int(aoo_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("Error","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aoo_upperRateLimitEntry = temp
                        self.aooUpperRateLimitValue.config(text="Current Value: " + aoo_upperRateLimitEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aooAtrialAmplitude
        if(value == "aooAtrialAmplitude"):
            temp = self.aooAtrialAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aoo_atrialAmplitudeEntry = temp
                        self.aooAtrialAmplitudeValue.config(text="Current Value: " + aoo_atrialAmplitudeEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aooAtrialPulseWidth
        if(value == "aooAtrialPulseWidth"):
            temp = self.aooAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aoo_atrialPulseWidthEntry = temp
                        self.aooAtrialPulseWidthValue.config(text="Current Value: " + aoo_atrialPulseWidthEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #VOO
        #vooLowerRateLimit
        if(value == "vooLowerRateLimit"):
            temp = self.vooLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(self.vooLowerRateLimitEntry.get()) >= int(voo_upperRateLimitEntry) and int(voo_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("Error","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        voo_lowerRateLimitEntry = temp
                        self.vooLowerRateLimitValue.config(text="Current Value: " + voo_lowerRateLimitEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass
        
        #vooUpperRateLimit
        if(value == "vooUpperRateLimit"):
            temp = self.vooUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(voo_lowerRateLimitEntry) >= int(self.vooUpperRateLimitEntry.get()) and int(voo_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("Error","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        voo_upperRateLimitEntry = temp
                        self.vooUpperRateLimitValue.config(text="Current Value: " + voo_upperRateLimitEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vooAtrialAmplitude
        if(value == "vooAtrialAmplitude"):
            temp = self.vooAtrialAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        voo_atrialAmplitudeEntry = temp
                        self.vooAtrialAmplitudeValue.config(text="Current Value: " + voo_atrialAmplitudeEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vooAtrialPulseWidth
        if(value == "vooAtrialPulseWidth"):
            temp = self.vooAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        voo_atrialPulseWidthEntry = temp
                        self.vooAtrialPulseWidthValue.config(text="Current Value: " + voo_atrialPulseWidthEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #AAI
        #aaiLowerRateLimit
        if(value == "aaiLowerRateLimit"):
            temp = self.aaiLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(self.aaiLowerRateLimitEntry.get()) >= int(aai_upperRateLimitEntry) and int(aai_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("Error","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_lowerRateLimitEntry = temp
                        self.aaiLowerRateLimitValue.config(text="Current Value: " + aai_lowerRateLimitEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiUpperRateLimit
        if(value == "aaiUpperRateLimit"):
            temp = self.aaiUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(aai_lowerRateLimitEntry) >= int(self.aaiUpperRateLimitEntry.get()) and int(aai_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("Error","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_upperRateLimitEntry = temp
                        self.aaiUpperRateLimitValue.config(text="Current Value: " + aai_upperRateLimitEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiAtrialAmplitude
        if(value == "aaiAtrialAmplitude"):
            temp = self.aaiAtrialAmplitudeEntry .get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_atrialAmplitudeEntry  = temp
                        self.aaiAtrialAmplitudeValue.config(text="Current Value: " + aai_atrialAmplitudeEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiAtrialPulseWidth
        if(value == "aaiAtrialPulseWidth"):
            temp = self.aaiAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_atrialPulseWidthEntry = temp
                        self.aaiAtrialPulseWidthValue.config(text="Current Value: " + aai_atrialPulseWidthEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiAtrialSensitivity
        if(value == "aaiAtrialSensitivity"):
            temp = self.aaiAtrialSensitivityEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_atrialSensitivityEntry = temp
                        self.aaiAtrialSensitivityValue.config(text="Current Value: " + aai_atrialSensitivityEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiARP
        if(value == "aaiARP"):
            temp = self.aaiARPEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_ARPEntry = temp
                        self.aaiARPValue.config(text="Current Value: " + aai_ARPEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiAPVARP
        if(value == "aaiAPVARP"):
            temp = self.aaiAPVARPEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_APVARPEntry = temp
                        self.aaiAPVARPValue.config(text="Current Value: " + aai_APVARPEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiHysteresis
        if(value == "aaiHysteresis"):
            temp = self.aaiHysteresisEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_hysteresisEntry = temp
                        self.aaiHysteresisValue.config(text="Current Value: " + aai_hysteresisEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiRateSmoothing
        if(value == "aaiRateSmoothing"):
            temp = self.aaiRateSmoothingEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_rateSmoothingEntry = temp
                        self.aaiRateSmoothingValue.config(text="Current Value: " + aai_rateSmoothingEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #VVI
        #vviLowerRateLimit
        if(value == "vviLowerRateLimit"):
            temp = self.vviLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(self.vviLowerRateLimitEntry.get()) >= int(vvi_upperRateLimitEntry) and int(vvi_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("Error","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_lowerRateLimitEntry = temp
                        self.vviLowerRateLimitValue.config(text="Current Value: " + vvi_lowerRateLimitEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviUpperRateLimit
        if(value == "vviUpperRateLimit"):
            temp = self.vviUpperRateLimitEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(vvi_lowerRateLimitEntry) >= int(self.vviUpperRateLimitEntry.get()) and int(vvi_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("Error","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_upperRateLimitEntry = temp
                        self.vviUpperRateLimitValue.config(text="Current Value: " + vvi_upperRateLimitEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviAtrialAmplitude
        if(value == "vviAtrialAmplitude"):
            temp = self.vviAtrialAmplitudeEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_atrialAmplitudeEntry = temp
                        self.vviAtrialAmplitudeValue.config(text="Current Value: " + vvi_atrialAmplitudeEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviAtrialPulseWidth
        if(value == "vviAtrialPulseWidth"):
            temp = self.vviAtrialPulseWidthEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_atrialPulseWidthEntry = temp
                        self.vviAtrialPulseWidthValue.config(text="Current Value: " + vvi_atrialPulseWidthEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviAtrialSensitivity
        if(value == "vviAtrialSensitivity"):
            temp = self.vviAtrialSensitivityEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_atrialSensitivityEntry = temp
                        self.vviAtrialSensitivityValue.config(text="Current Value: " + vvi_atrialSensitivityEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviARP
        if(value == "vviARP"):
            temp = self.vviARPEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_ARPEntry = temp
                        self.vviARPValue.config(text="Current Value: " + vvi_ARPEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviHysteresis
        if(value == "vviHysteresis"):
            temp = self.vviHysteresisEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_hysteresisEntry = temp
                        self.vviHysteresisValue.config(text="Current Value: " + vvi_hysteresisEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviRateSmoothing
        if(value == "vviRateSmoothing"):
            temp = self.vviRateSmoothingEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_rateSmoothingEntry = temp
                        self.vviRateSmoothingValue.config(text="Current Value: " + vvi_rateSmoothingEntry)
            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

    #Method used to log off user
    def logOff(self):
        if messagebox.askyesno("LogOff", "Do you want to log off?"):
            self.master.destroy()
            main()  

    #Method to exit application
    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            exit()
    
    #Method for closing windows
    def close_windows(self):
        self.master.destroy()
        exit()

#Access pickle file to read current users
def readUsers():
    global login_dict
    #Try/except is used to check for two different paths
    try:
        with open('HACKERS_DONT_LOOK_HERE.pickle', 'rb') as file:
            login_dict =  pickle.load(file)
            print(login_dict)
    except(FileNotFoundError):
        with open('DCM/HACKERS_DONT_LOOK_HERE.pickle', 'rb') as file:
            login_dict =  pickle.load(file)
            print(login_dict)

#Write new users to the pickle file
def writeUsers():
    global login_dict
    #Try/except is used to check for two different paths
    try:
        with open('HACKERS_DONT_LOOK_HERE.pickle', 'wb') as file:
            pickle.dump(login_dict,file)
    except(FileNotFoundError):
        with open('DCM/HACKERS_DONT_LOOK_HERE.pickle', 'wb') as file:
            pickle.dump(login_dict,file)

#Access pickle file to read values from each user
def readValues():
    global user0, user1, user2, user3, user4, user5, user6, user7, user8, user9
    userList = [user0, user1, user2, user3, user4, user5, user6, user7, user8, user9]
    try:
        for i in range(10):
            with open('user' + i + '.pickle', 'rb') as file:
                userList[i] = pickle.load(file)
                print(userList[i])
    except(FileNotFoundError):
        for i in range(10):
            with open('DCM/user' + i + '.pickle', 'rb') as file:
                userList[i] = pickle.load(file)
                print(userList[i])


#Write new user values to pickle file
def writeValues():
    global user0, user1, user2, user3, user4, user5, user6, user7, user8, user9
    userList = [user0, user1, user2, user3, user4, user5, user6, user7, user8, user9]
    try:
        for i in range(10):
            with open('user' + str(i) + '.pickle', 'wb') as file:
                pickle.dump(userList[i], file)
    except(FileNotFoundError):
        for i in range(10):
            with open('DCM/user' + str(i) + '.pickle', 'wb') as file:
                pickle.dump(userList[i], file)
        

#Main function that runs everything
def main():
    try:
        readUsers()
    except (EOFError):
        pass
    #Run Tkinter
    root = tk.Tk()
    app = WelcomeFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()