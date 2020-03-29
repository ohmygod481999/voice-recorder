from tkinter import *
from tkinter import scrolledtext
from recorder import Recorder


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Wellcome To Long's App")
        self.window.geometry('350x200')
        self.recorder = Recorder()
        file = open("text.txt", "r")
        self.article = file.read()

    def initUI(self):
        label = Label(self.window, text="Hi")
        label.grid(column=0, row=0)

        self.startButton = Button(self.window, text="Start",)
        self.startButton.grid(column=0, row=1)

        self.stopButton = Button(self.window, text="Stop")
        self.stopButton.grid(column=0, row=2)

        self.scrolledText = scrolledtext.ScrolledText(
            self.window, width=100, height=50)
        self.scrolledText.grid(column=0, row=3)

    def initLogic(self):
        def startClickHandler():
            self.recorder.startRecord()

        def stopClickHandler():
            self.recorder.stopRecord()

        self.startButton.configure(command=startClickHandler)
        self.stopButton.configure(command=stopClickHandler)

        self.scrolledText.insert(INSERT, self.article)

    def mainLoop(self):
        self.window.mainloop()


app = App()
app.initUI()
app.initLogic()

app.mainLoop()
