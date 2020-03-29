import pyaudio
import wave
from tkinter import *

from threading import Thread
import threading

from tkinter import scrolledtext
from tkinter.font import Font
import time


f = open("text.txt", "r")

article = f.read()
articleArr = article.split(".")


window = Tk()
window.title("welcome")
window.geometry("800x800")
myFont = Font(family="Times New Roman", size=12)

label = Label(window, text="hello", font=myFont)
label.grid(column=0, row=0)

input = scrolledtext.ScrolledText(window, width=100, height=50, font=myFont)
input.grid(column=0, row=1)
text = Text(window)
text.configure(font=myFont)
input.insert(INSERT, article)


def clickHandler():
    label.configure(text=input.get("1.0", 'end-1c'))



CHUNK = 1024
WIDTH = 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

end = False

def record():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)
    # stream.start_stream()
    print("* recording")

    frames = []

    def listen():
        global end
        if not end:
            data = stream.read(CHUNK)
            frames.append(data)
            window.after(1, listen)

    listen()
    return (stream, frames)




def stopRecord(stream):
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('Finished recording')
    end = True


button = Button(window, text="Click me", command=lambda parameter_list: stopRecord(stream))
button.grid(column=1, row=0)


def writeFile(frames, fileName):
    wf = wave.open(fileName, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# for i in range(len(textArr)):
#     print(textArr[i])


# stream, frames = record()


# stopRecord(stream)

# writeFile(frames, "test.wav")

window.mainloop()
