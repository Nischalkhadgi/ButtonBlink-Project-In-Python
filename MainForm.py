import Tkinter
import GPIOLibs

class MainForm:
    root = None
    def __init__(self):
        #making switch state to 0
        self.switchState = 0

        self.gpio = GPIOLibs.GPIOLibs()
        
        root = Tkinter.Tk()
        root.title("First programming in raspberry pi")
        root.geometry("400x400")
        
        #Adding Widgets
        self.switchBtn = Tkinter.Button(root, text ="Turn On Light", command = self.toggleSwitch)
        self.switchBtn.pack()
        
        #Making Tkinter loop
        root.mainloop()
    def toggleSwitch(self):
        if (self.switchState == 0):
            self.switchState = 1
            self.gpio.LedState(self.switchState)
            self.switchBtn["text"] = "Turn off Light"
        else:
            self.switchState = 0
            self.gpio.LedState(self.switchState)
            self.switchBtn["text"] = "Turn on Light"
