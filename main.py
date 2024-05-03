from tkinter import *
import tkinter.font as font
import subprocess


class main_window:
    def __init__(self, windowroot):
        self.window = windowroot
        self.window.geometry("750x400")
        self.window.title("Digital Signal Processing")
        self.createWidgets()

    def createWidgets(self):
        buttonFont = font.Font(family='Helvetica', size=8, weight='bold')

        self.FilteringButton = Button(
            self.window, text="Filtering", width="13", height="3", command=self.Filter, font=buttonFont)
        self.ResamplingButton = Button(
            self.window, text="Resampling", width="13", height="3", command=self.Resampling, font=buttonFont)
        self.Task2Button = Button(
            self.window, text="Task 2", width="13", height="3", command=self.ECG, font=buttonFont)
        
        self.FilteringButton.place(x=330, y=10)
        self.ResamplingButton.place(x=330, y=70)
        self.Task2Button.place(x=330, y=130)
        
    

    def Filter(self):
        subprocess.run(["python", "Filtering_Gui.py"], check=True)
        
    def Resampling(self):
        subprocess.run(["python", "Resampling_Gui.py"], check=True)
        
    def ECG(self):
        subprocess.run(["python", "Task2_Gui.py"], check=True)

def main():
    window = Tk()
    main_window(window)
    window.mainloop()

if __name__ == "__main__":
    main()
