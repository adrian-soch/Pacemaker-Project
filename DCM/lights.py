from tkinter import *
import usb.core
import time


class TrafficLights:

    def __init__(self):

        window = Tk()
        window.title("Traffic Light")

        frame = Frame(window)
        frame.pack()

        self.color = StringVar()

        radio_red = Radiobutton(frame, text="Red", bg="red", variable=self.color, value="R", command=self.on_RadioChange)
        radio_red.grid(row=10, column=1)

        radio_green = Radiobutton(frame, text="Green", bg="green", variable=self.color, value="G", command=self.on_RadioChange)
        radio_green.grid(row = 10, column = 2)

        self.canvas = Canvas(window, width=450, height=300, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white")
        self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white")

        while(1):
            self.run()

        window.mainloop()

    def on_RadioChange(self):
        color = self.color.get()

        if color == 'R':
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_green, fill="white")

        elif color == 'G':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")


    def test(self):
        dev = usb.core.find(find_all=True)
        var = ''
        for cfg in dev:
            if (cfg.idVendor == 4966):
                var = cfg.idVendor
        return var

    def run(self):
        status = ''
        while(1):
            if (len(self.test()) > 0):
                status = self.test()
            else:
                status = "Not Connected"
            print(status)


TrafficLights()



