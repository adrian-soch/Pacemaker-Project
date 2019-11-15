#Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#Creating sqlite3 database
db = sqlite3.connect("DCM.sqlite", detect_types= sqlite3.PARSE_DECLTYPES)

#Create seperate table for each state within database
db.execute("CREATE TABLE IF NOT EXISTS users (user TEXT NOT NULL, password TEXT NOT NULL, codename TEXT NOT NULL)")

#Current User
currentuser = ''

#Initializing all global variables with "0"
#AOO
aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry = "0","0","0","0"

#VOO
voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry = "0","0","0","0"

#AAI
aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_APVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry = "0","0","0","0","0","0","0","0","0"

#VVI
vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_ARPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry = "0","0","0","0","0","0","0","0"


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
        global currentuser
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')

        #Query Database to find username and password
        cursor = db.execute("SELECT * FROM users WHERE (user = ?) and (password = ?)", (username,password,))
        row = cursor.fetchall()

        if row:
            #If username is found then they become the current user
            currentuser = str(row[0][2])
            self.master.withdraw()
            self.new_window(MainWindow)
        else:
            #Otherwise the username/password is wrong
            messagebox.showerror("Error", "Username/Password is Incorrect")

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
        username = self.entry_username.get()
        password = self.entry_password.get()
        password2 = self.entry_password2.get()
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.entry_password2.delete(0, 'end')

        #Password verification
        if(password == password2):
            valid = 0
            cursor = db.execute("SELECT user FROM users WHERE (user=?)", (username,))
            row = cursor.fetchone()
            if row:
                valid = 0
                messagebox.showerror("Error", "User exists")
            else:
                checker = db.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name != 'android_metadata' AND name != 'sqlite_sequence';")
                counter = len(checker.fetchall())
                counters = "user"+str(counter+1)
                valid = 1

            if valid == 1:
                try:
                    checker = db.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name != 'android_metadata' AND name != 'sqlite_sequence';")
                    counter2 = len(checker.fetchall())

                    #Verify there are no errors    
                    if (len(username) < 1 or len(password) < 1):
                        messagebox.showerror("Error", "Missing Username and/or Password")
                    elif (counter2 > 10):
                        messagebox.showerror("Error", "Maximum allowed user limit reached")
                    else:
                        userlog = 'No Mode Set'
                        db.execute("CREATE TABLE "+counters+" (userlog TEXT NOT NULL,"
                            " aoo_lowerRateLimitEntry INTEGER NOT NULL, aoo_upperRateLimitEntry INTEGER NOT NULL, aoo_atrialAmplitudeEntry REAL NOT NULL, aoo_atrialPulseWidthEntry INTEGER NOT NULL,"
                            " voo_lowerRateLimitEntry INTEGER NOT NULL, voo_upperRateLimitEntry INTEGER NOT NULL, voo_ventricularAmplitudeEntry REAL NOT NULL, voo_ventricularPulseWidthEntry INTEGER NOT NULL,"
                            " aai_lowerRateLimitEntry INTEGER NOT NULL, aai_upperRateLimitEntry INTEGER NOT NULL, aai_atrialAmplitudeEntry REAL NOT NULL, aai_atrialPulseWidthEntry INTEGER NOT NULL, aai_atrialSensitivityEntry REAL NOT NULL, aai_ARPEntry INTEGER NOT NULL, aai_APVARPEntry INTEGER NOT NULL, aai_hysteresisEntry INTEGER NOT NULL, aai_rateSmoothingEntry INTEGER NOT NULL,"
                            " vvi_lowerRateLimitEntry INTEGER NOT NULL, vvi_upperRateLimitEntry INTEGER NOT NULL, vvi_ventricularAmplitudeEntry REAL NOT NULL, vvi_ventricularPulseWidthEntry INTEGER NOT NULL, vvi_ventricularSensitivityEntry REAL NOT NULL, vvi_ARPEntry INTEGER NOT NULL, vvi_hysteresisEntry INTEGER NOT NULL, vvi_rateSmoothingEntry INTEGER NOT NULL)")
                        db.execute("INSERT INTO users VALUES(?, ?, ?)", (username, password, counters))
                        db.execute("INSERT INTO "+counters+" VALUES(?, "
                            "?,?,?,?, "
                            "?,?,?,?, "
                            "?,?,?,?,?,?,?,?,?, "
                            "?,?,?,?,?,?,?,?)", (userlog, 
                            60, 120, 3.5, 1.5, 
                            60, 120, 3.5, 1.5, 
                            60, 120, 3.5, 1.5, 3.3, 250, 200, 0, 0, 
                            60, 120, 3.5, 1.5, 3.3, 250, 0, 0))
                        messagebox.showinfo("Success", "User Added")
                        self.quitButton.focus()

                except Exception as e:
                    messagebox.showerror("Error", "User exists")
                
                db.commit()

        #Passwords don't match
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
        self.master.geometry('750x570')
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

        #Retrieve all relevant data from tables for currentuser
        global currentuser
        cursor = db.execute("SELECT * FROM "+currentuser);row = cursor.fetchall()

        #Current Mode
        global userlog
        userlog                           = str(row[0][0])

        #Global Variables setup with current user parameters
        #AOO
        global aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry 
        aoo_lowerRateLimitEntry           = str(row[0][1])
        aoo_upperRateLimitEntry           = str(row[0][2])
        aoo_atrialAmplitudeEntry          = str(row[0][3])
        aoo_atrialPulseWidthEntry         = str(row[0][4])
        
        #VOO
        global voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry
        voo_lowerRateLimitEntry           = str(row[0][5])
        voo_upperRateLimitEntry           = str(row[0][6])
        voo_ventricularAmplitudeEntry     = str(row[0][7])
        voo_ventricularPulseWidthEntry    = str(row[0][8])

        #AAI
        global aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_PVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry
        aai_lowerRateLimitEntry           = str(row[0][9])
        aai_upperRateLimitEntry           = str(row[0][10])
        aai_atrialAmplitudeEntry          = str(row[0][11])
        aai_atrialPulseWidthEntry         = str(row[0][12])
        aai_atrialSensitivityEntry        = str(row[0][13])
        aai_ARPEntry                      = str(row[0][14])
        aai_PVARPEntry                    = str(row[0][15])
        aai_hysteresisEntry               = str(row[0][16])
        aai_rateSmoothingEntry            = str(row[0][17])

        #VVI
        global vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_VRPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry
        vvi_lowerRateLimitEntry           = str(row[0][18])
        vvi_upperRateLimitEntry           = str(row[0][19])
        vvi_ventricularAmplitudeEntry     = str(row[0][20])
        vvi_ventricularPulseWidthEntry    = str(row[0][21])
        vvi_ventricularSensitivityEntry   = str(row[0][22])
        vvi_VRPEntry                      = str(row[0][23])
        vvi_hysteresisEntry               = str(row[0][24])
        vvi_rateSmoothingEntry            = str(row[0][25])

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

        #Spinbox for setup
        self.aooLowerRateLimitEntry = tk.Spinbox(self.aoo,from_=30,to=175,increment=5)
        self.aooUpperRateLimitEntry = tk.Spinbox(self.aoo,from_=50,to=175,increment=5)
        self.aooAtrialAmplitudeEntry = tk.Spinbox(self.aoo,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.aooAtrialPulseWidthEntry = tk.Spinbox(self.aoo,from_=0.05,to=1.9,format="%.2f",increment=0.1)

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
        self.vooVentricularAmplitudeButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooVentricularAmplitude"))
        self.vooVentricularPulseWidthButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooVentricularPulseWidth"))
        
        #Setup labels for inputs
        self.vooLowerRateLimitLabel = tk.Label(self.voo, text = "Lower Rate Limit")
        self.vooUpperRateLimitLabel = tk.Label(self.voo, text = "Upper Rate Limit ")
        self.vooVentricularAmplitudeLabel = tk.Label(self.voo, text = "Ventricular Amplitude")
        self.vooVentricularPulseWidthLabel = tk.Label(self.voo, text = "Ventricular Pulse Width")

        #Setup  labels to display values
        self.vooLowerRateLimitValue = tk.Label(self.voo, text = "Current Value: "+ voo_lowerRateLimitEntry)
        self.vooUpperRateLimitValue = tk.Label(self.voo, text = "Current Value: "+ voo_upperRateLimitEntry)
        self.vooVentricularAmplitudeValue = tk.Label(self.voo, text = "Current Value: "+ voo_ventricularAmplitudeEntry)
        self.vooVentricularPulseWidthValue = tk.Label(self.voo, text = "Current Value: "+ voo_ventricularPulseWidthEntry)

        #Spinbox for setup
        self.vooLowerRateLimitEntry = tk.Spinbox(self.voo,from_=30,to=175,increment=5)
        self.vooUpperRateLimitEntry = tk.Spinbox(self.voo,from_=50,to=175,increment=5)
        self.vooVentricularAmplitudeEntry = tk.Spinbox(self.voo,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.vooVentricularPulseWidthEntry = tk.Spinbox(self.voo,from_=0.05,to=1.9,format="%.2f",increment=0.1)

        #Adjust positioning
        self.vooLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.vooLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.vooLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.vooLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        self.vooUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.vooUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.vooUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.vooUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)
        self.vooVentricularAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.vooVentricularAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.vooVentricularAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.vooVentricularAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        self.vooVentricularPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.vooVentricularPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.vooVentricularPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.vooVentricularPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
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

        #Spinbox for setup
        self.aaiLowerRateLimitEntry = tk.Spinbox(self.aai,from_=30,to=175,increment=5)
        self.aaiUpperRateLimitEntry = tk.Spinbox(self.aai,from_=50,to=175,increment=5)
        self.aaiAtrialAmplitudeEntry = tk.Spinbox(self.aai,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.aaiAtrialPulseWidthEntry = tk.Spinbox(self.aai,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.aaiAtrialSensitivityEntry = tk.Spinbox(self.aai,from_=0.25,to=10.0,format="%.2f",increment=0.25)
        self.aaiARPEntry = tk.Spinbox(self.aai,from_=150,to=500,increment=10)
        self.aaiAPVARPEntry = tk.Spinbox(self.aai,from_=150,to=500,increment=10)
        self.aaiHysteresisEntry = tk.Spinbox(self.aai,from_=0,to=25,increment=5)
        self.aaiRateSmoothingEntry = tk.Spinbox(self.aai,from_=0,to=25,increment=3)

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
        self.vviVentricularAmplitudeButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviVentricularAmplitude"))
        self.vviVentricularPulseWidthButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviVentricularPulseWidth"))
        self.vviVentricularSensitivityButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviVentricularSensitivity"))
        self.vviVRPButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviVRP"))
        self.vviHysteresisButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviHysteresis"))
        self.vviRateSmoothingButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviRateSmoothing"))

        #Setup labels for inputs
        self.vviLowerRateLimitLabel = tk.Label(self.vvi, text = "Lower Rate Limit")
        self.vviUpperRateLimitLabel = tk.Label(self.vvi, text = "Upper Rate Limit ")
        self.vviVentricularAmplitudeLabel = tk.Label(self.vvi, text = "Ventricular Amplitude")
        self.vviVentricularPulseWidthLabel = tk.Label(self.vvi, text = "Ventricular Pulse Width")
        self.vviVentricularSensitivityLabel = tk.Label(self.vvi, text = "Ventricular Sensitivity")
        self.vviVRPLabel = tk.Label(self.vvi, text = "VRP")
        self.vviHysteresisLabel = tk.Label(self.vvi, text = "Hysteresis")
        self.vviRateSmoothingLabel = tk.Label(self.vvi, text = "Rate Smoothing")

        #Setup  labels to display values
        self.vviLowerRateLimitValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_lowerRateLimitEntry)
        self.vviUpperRateLimitValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_upperRateLimitEntry)
        self.vviVentricularAmplitudeValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_ventricularAmplitudeEntry)
        self.vviVentricularPulseWidthValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_ventricularPulseWidthEntry)
        self.vviVentricularSensitivityValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_ventricularSensitivityEntry)
        self.vviVRPValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_ARPEntry)
        self.vviHysteresisValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_hysteresisEntry)
        self.vviRateSmoothingValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_rateSmoothingEntry)

        #Spinbox for setup
        self.vviLowerRateLimitEntry = tk.Spinbox(self.vvi,from_=30,to=175,increment=5)
        self.vviUpperRateLimitEntry = tk.Spinbox(self.vvi,from_=50,to=175,increment=5)
        self.vviVentricularAmplitudeEntry = tk.Spinbox(self.vvi,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.vviVentricularPulseWidthEntry = tk.Spinbox(self.vvi,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.vviVentricularSensitivityEntry = tk.Spinbox(self.vvi,from_=0.25,to=10.0,format="%.2f",increment=0.25)
        self.vviVRPEntry = tk.Spinbox(self.vvi,from_=150,to=500,increment=10)
        self.vviHysteresisEntry = tk.Spinbox(self.vvi,from_=0,to=25,increment=5)
        self.vviRateSmoothingEntry = tk.Spinbox(self.vvi,from_=0,to=25,increment=3)

        #Adjust positioning
        self.vviLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.vviLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.vviLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.vviUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.vviUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.vviUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.vviVentricularAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.vviVentricularAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.vviVentricularAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.vviVentricularPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.vviVentricularPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.vviVentricularPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.vviVentricularSensitivityLabel.grid(row=4, column=0, padx=15, pady=15)
        self.vviVentricularSensitivityEntry.grid(row=4, column=1, padx=15, pady=15)
        self.vviVentricularSensitivityButton.grid(row=4, column=2, padx=15, pady=15)
        self.vviVRPLabel.grid(row=5, column=0, padx=15, pady=15)
        self.vviVRPEntry.grid(row=5, column=1, padx=15, pady=15)
        self.vviVRPButton.grid(row=5, column=2, padx=15, pady=15)
        self.vviHysteresisLabel.grid(row=6, column=0, padx=15, pady=15)
        self.vviHysteresisEntry.grid(row=6, column=1, padx=15, pady=15)
        self.vviHysteresisButton.grid(row=6, column=2, padx=15, pady=15)
        self.vviRateSmoothingLabel.grid(row=7, column=0, padx=15, pady=15)
        self.vviRateSmoothingEntry.grid(row=7, column=1, padx=15, pady=15)
        self.vviRateSmoothingButton.grid(row=7, column=2, padx=15, pady=15)
        self.vviLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        self.vviUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)
        self.vviVentricularAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        self.vviVentricularPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        self.vviVentricularSensitivityValue.grid(row=4, column=3, padx=15, pady=15)
        self.vviVRPValue.grid(row=5, column=3, padx=15, pady=15)
        self.vviHysteresisValue.grid(row=6, column=3, padx=15, pady=15)
        self.vviRateSmoothingValue.grid(row=7, column=3, padx=15, pady=15)
        #VVI END-------------------------------------------------------------------------------------------------------------------------------

        #Track the process
        self.logTitle = tk.Label(self.aoo, text = "Current Mode")
        self.logTitle.grid(row=0, column=4, padx=15, pady=15)
        self.aooLog = tk.Label(self.aoo, text = userlog)
        self.aooLog.grid(row=1, column=4, padx=15, pady=15)
        
        self.logTitle = tk.Label(self.voo, text = "Current Mode")
        self.logTitle.grid(row=0, column=4, padx=15, pady=15)
        self.vooLog = tk.Label(self.voo, text = userlog)
        self.vooLog.grid(row=1, column=4, padx=15, pady=15)

        self.logTitle = tk.Label(self.aai, text = "Current Mode")
        self.logTitle.grid(row=0, column=4, padx=15, pady=15)
        self.aaiLog = tk.Label(self.aai, text = userlog)
        self.aaiLog.grid(row=1, column=4, padx=15, pady=15)

        self.logTitle = tk.Label(self.vvi, text = "Current Mode")
        self.logTitle.grid(row=0, column=4, padx=15, pady=15)
        self.vviLog = tk.Label(self.vvi, text = userlog)
        self.vviLog.grid(row=1, column=4, padx=15, pady=15)

        #Position tabs properly
        self.tab_parent.pack(expand = 1, fill='both')

        #Setup confirm buttons
        self.confirmButton = tk.Button(self.aoo, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("aooConfirm"))
        self.confirmButton.grid(row = 4, column = 1)
        self.confirmButton = tk.Button(self.voo, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("vooConfirm"))
        self.confirmButton.grid(row = 4, column = 1)
        self.confirmButton = tk.Button(self.aai, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("aaiConfirm"))
        self.confirmButton.grid(row = 9, column = 1)
        self.confirmButton = tk.Button(self.vvi, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("vviConfirm"))
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
    def confirmChanges(self,value):
        global currentuser
        if (value == "aooConfirm"):
            if messagebox.askyesno("Confirmation", "Upload these changes?"):
                messagebox.showinfo("Done", "Success")
                userlog = "AOO Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "vooConfirm"):
            if messagebox.askyesno("Confirmation", "Upload these changes?"):
                messagebox.showinfo("Done", "Success")
                userlog = "VOO Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "aaiConfirm"):
            if messagebox.askyesno("Confirmation", "Upload these changes?"):
                messagebox.showinfo("Done", "Success")
                userlog = "AAI Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "vviConfirm"):
            if messagebox.askyesno("Confirmation", "Upload these changes?"):
                messagebox.showinfo("Done", "Success")
                userlog = "VVI Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
            
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
        global voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry
        #AAI
        global aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_APVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry
        #VVI
        global vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_ARPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry

        #Currentuser
        global currentuser

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

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("Error","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aoo_lowerRateLimitEntry = temp
                        self.aooLowerRateLimitValue.config(text="Current Value: " + aoo_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aoo_lowerRateLimitEntry = ?", (aoo_lowerRateLimitEntry,))
                        db.commit()

            except Exception as e:
                print(e)
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

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("Error","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aoo_upperRateLimitEntry = temp
                        self.aooUpperRateLimitValue.config(text="Current Value: " + aoo_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aoo_upperRateLimitEntry = ?", (aoo_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aooAtrialAmplitude
        if(value == "aooAtrialAmplitude"):
            temp = self.aooAtrialAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass
                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("Error","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aoo_atrialAmplitudeEntry = temp
                        self.aooAtrialAmplitudeValue.config(text="Current Value: " + aoo_atrialAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET aoo_atrialAmplitudeEntry = ?", (aoo_atrialAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aooAtrialPulseWidth
        if(value == "aooAtrialPulseWidth"):
            temp = self.aooAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("Error","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aoo_atrialPulseWidthEntry = temp
                        self.aooAtrialPulseWidthValue.config(text="Current Value: " + aoo_atrialPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET aoo_atrialPulseWidthEntry = ?", (aoo_atrialPulseWidthEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("Error","The range is between 30 and 175")
                    pass
                
                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        voo_lowerRateLimitEntry = temp
                        self.vooLowerRateLimitValue.config(text="Current Value: " + voo_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET voo_lowerRateLimitEntry = ?", (voo_lowerRateLimitEntry,))
                        db.commit()
                        
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

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("Error","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        voo_upperRateLimitEntry = temp
                        self.vooUpperRateLimitValue.config(text="Current Value: " + voo_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET voo_upperRateLimitEntry = ?", (voo_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vooVentricularAmplitude
        if(value == "vooVentricularAmplitude"):
            temp = self.vooVentricularAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("Error","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        voo_ventricularAmplitudeEntry = temp
                        self.vooVentricularAmplitudeValue.config(text="Current Value: " + voo_ventricularAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET voo_ventricularAmplitudeEntry = ?", (voo_ventricularAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vooVentricularPulseWidth
        if(value == "vooVentricularPulseWidth"):
            temp = self.vooVentricularPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("Error","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        voo_ventricularPulseWidthEntry = temp
                        self.vooVentricularPulseWidthValue.config(text="Current Value: " + voo_ventricularPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET voo_ventricularPulseWidthEntry = ?", (voo_ventricularPulseWidthEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("Error","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_lowerRateLimitEntry = temp
                        self.aaiLowerRateLimitValue.config(text="Current Value: " + aai_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_lowerRateLimitEntry = ?", (aai_lowerRateLimitEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("Error","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_upperRateLimitEntry = temp
                        self.aaiUpperRateLimitValue.config(text="Current Value: " + aai_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_upperRateLimitEntry = ?", (aai_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiAtrialAmplitude
        if(value == "aaiAtrialAmplitude"):
            temp = self.aaiAtrialAmplitudeEntry .get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("Error","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_atrialAmplitudeEntry  = temp
                        self.aaiAtrialAmplitudeValue.config(text="Current Value: " + aai_atrialAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_atrialAmplitudeEntry = ?", (aai_atrialAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiAtrialPulseWidth
        if(value == "aaiAtrialPulseWidth"):
            temp = self.aaiAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("Error","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_atrialPulseWidthEntry = temp
                        self.aaiAtrialPulseWidthValue.config(text="Current Value: " + aai_atrialPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_atrialPulseWidthEntry = ?", (aai_atrialPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #aaiAtrialSensitivity
        if(value == "aaiAtrialSensitivity"):
            temp = self.aaiAtrialSensitivityEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.25 or float(temp) > 10.0):
                    messagebox.showinfo("Error","The range is between 0.25 and 10.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_atrialSensitivityEntry = temp
                        self.aaiAtrialSensitivityValue.config(text="Current Value: " + aai_atrialSensitivityEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_atrialSensitivityEntry = ?", (aai_atrialSensitivityEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("Error","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_ARPEntry = temp
                        self.aaiARPValue.config(text="Current Value: " + aai_ARPEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_ARPEntry = ?", (aai_ARPEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("Error","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_APVARPEntry = temp
                        self.aaiAPVARPValue.config(text="Current Value: " + aai_APVARPEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_APVARPEntry = ?", (aai_APVARPEntry,))
                        db.commit()

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

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_hysteresisEntry = temp
                        self.aaiHysteresisValue.config(text="Current Value: " + aai_hysteresisEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_hysteresisEntry = ?", (aai_hysteresisEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 0 or int(temp) > 25):
                    messagebox.showinfo("Error","The range is between 0(off) and 25")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        aai_rateSmoothingEntry = temp
                        self.aaiRateSmoothingValue.config(text="Current Value: " + aai_rateSmoothingEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_rateSmoothingEntry = ?", (aai_rateSmoothingEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("Error","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_lowerRateLimitEntry = temp
                        self.vviLowerRateLimitValue.config(text="Current Value: " + vvi_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_lowerRateLimitEntry = ?", (vvi_lowerRateLimitEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("Error","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_upperRateLimitEntry = temp
                        self.vviUpperRateLimitValue.config(text="Current Value: " + vvi_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_upperRateLimitEntry = ?", (vvi_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviVentricularAmplitude
        if(value == "vviVentricularAmplitude"):
            temp = self.vviVentricularAmplitudeEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("Error","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_ventricularAmplitudeEntry = temp
                        self.vviVentricularAmplitudeValue.config(text="Current Value: " + vvi_ventricularAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_ventricularAmplitudeEntry = ?", (vvi_ventricularAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviVentricularPulseWidth
        if(value == "vviVentricularPulseWidth"):
            temp = self.vviVentricularPulseWidthEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("Error","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_ventricularPulseWidthEntry = temp
                        self.vviVentricularPulseWidthValue.config(text="Current Value: " + vvi_ventricularPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_ventricularPulseWidthEntry = ?", (vvi_ventricularPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviVentricularSensitivity
        if(value == "vviVentricularSensitivity"):
            temp = self.vviVentricularSensitivityEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.25 or float(temp) > 10.0):
                    messagebox.showinfo("Error","The range is between 0.25 and 10.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_ventricularSensitivityEntry = temp
                        self.vviVentricularSensitivityValue.config(text="Current Value: " + vvi_ventricularSensitivityEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_ventricularSensitivityEntry = ?", (vvi_ventricularSensitivityEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

        #vviVRP
        if(value == "vviVRP"):
            temp = self.vviVRPEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("Error","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("Error","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_ARPEntry = temp
                        self.vviVRPValue.config(text="Current Value: " + vvi_ARPEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_ARPEntry = ?", (vvi_ARPEntry,))
                        db.commit()

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

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_hysteresisEntry = temp
                        self.vviHysteresisValue.config(text="Current Value: " + vvi_hysteresisEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_hysteresisEntry = ?", (vvi_hysteresisEntry,))
                        db.commit()

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

                #Ensure value is in limited range
                elif(int(temp) < 0 or int(temp) > 25):
                    messagebox.showinfo("Error","The range is between 0(off) and 25")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("Confirmation", "Replace current value?"):
                        messagebox.showinfo("Done", "Success")
                        vvi_rateSmoothingEntry = temp
                        self.vviRateSmoothingValue.config(text="Current Value: " + vvi_rateSmoothingEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_rateSmoothingEntry = ?", (vvi_rateSmoothingEntry,))
                        db.commit()

            except:
                messagebox.showinfo("Error","Please enter a valid value")
                pass

    #Method used to log off user
    def logOff(self):
        if messagebox.askyesno("LogOff", "Do you want to log off?"):
            self.master.destroy()
            main()
            #exit()

    #Method to exit application
    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            exit()
    
    #Method for closing windows
    def close_windows(self):
        self.master.destroy()
        exit()


#Main function that runs everything
def main():

    #Run Tkinter
    root = tk.Tk()
    app = WelcomeFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()