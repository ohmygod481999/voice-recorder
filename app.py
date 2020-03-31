from tkinter import *
from tkinter import scrolledtext
from recorder import Recorder
import os


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Wellcome To Long's App")
        self.window.geometry('350x200')
        self.recorder = Recorder()
        file = open("text.txt", mode="r", encoding="utf8")
        self.article = file.read()
        self.count = 1
        file.close()

    def initUI(self):
        self.scrolledText = scrolledtext.ScrolledText(
            self.window, width=50, height=30)
        self.scrolledText.grid(column=0, row=0)

        panelRight = PanedWindow(self.window)
        panelRight.grid(column=1, row=0)

        labelFolder = Label(panelRight, text="Folder Name: ")
        labelFolder.grid(column=0, row=0)

        self.folderNameInput = Entry(panelRight)
        self.folderNameInput.grid(column=0, row=1)

        labelFileName = Label(panelRight, text="File Name: ")
        labelFileName.grid(column=0, row=2)

        self.fileNameInput = Entry(panelRight)
        self.fileNameInput.grid(column=0, row=3)

        labelSentence = Label(panelRight, text="Sentence: ")
        labelSentence.grid(column=0, row=4)

        self.sentenceInput = Entry(panelRight)
        self.sentenceInput.grid(column=0, row=5)

        self.startButton = Button(panelRight, text="Start",)
        self.startButton.grid(column=0, row=6)

        self.stopButton = Button(panelRight, text="Stop")
        self.stopButton.grid(column=0, row=7)

        self.resetCountButton = Button(panelRight, text="Reset")
        self.resetCountButton.grid(column=0, row=8)

    def initLogic(self):
        def startClickHandler():
            self.recorder.startRecord()

        def stopClickHandler():
            frames = self.recorder.stopRecord()
            textFile = open("data/" + self.folderNameInput.get() + "/index.txt",
                            mode="a", encoding="utf8")

            textFile.write(self.fileNameInput.get() + ".wav" + '\n')
            textFile.write(self.sentenceInput.get() + '\n')

            self.recorder.writeFile(
                frames, "data/" + self.folderNameInput.get() + "/" + self.fileNameInput.get() + ".wav")

            self.count = self.count + 1
            self.fileNameInput.delete(0, END)
            self.fileNameInput.insert(0,
                                      self.folderNameInput.get() + "-" + str(self.count))

        def resetHandler():
            self.count = 1

        self.startButton.configure(command=startClickHandler)
        self.stopButton.configure(command=stopClickHandler)
        self.resetCountButton.configure(command=resetHandler)

        self.scrolledText.insert(INSERT, self.article)

    def mainLoop(self):
        self.window.mainloop()


def main():
    app = App()
    app.initUI()
    app.initLogic()

    app.mainLoop()


if __name__ == "__main__":
    main()
