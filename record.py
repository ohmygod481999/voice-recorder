import pyaudio
import wave
from tkinter import *

from tkinter import scrolledtext
from tkinter.font import Font
import time


# f = open("text.txt", "r")

# article = f.read()
# articleArr = article.split(".")


# window = Tk()
# window.title("welcome")
# window.geometry("800x800")
# myFont = Font(family="Times New Roman", size=12)

# label = Label(window, text="hello", font=myFont)
# label.grid(column=0, row=0)

# input = scrolledtext.ScrolledText(window, width=100, height=50, font=myFont)
# input.grid(column=0, row=1)
# text = Text(window)
# text.configure(font=myFont)
# input.insert(INSERT, article)


# def clickHandler():
#     label.configure(text=input.get("1.0", 'end-1c'))


# button = Button(window, text="Click me", command=clickHandler)
# button.grid(column=1, row=0)


# window.mainloop()

CHUNK = 1024
WIDTH = 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()


def record(callback):
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    stream_callback=callback)
    stream.start_stream()
    print("* recording")
    return stream

def stopRecord(stream):
    stream.stop_stream()
    stream.close()
    p.terminate()

def writeFile(data, fileName):
    wf = wave.open(fileName, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    # wf.writeframes(b''.join(frames))
    wf.writeframes(data)
    wf.close()


# for i in range(len(textArr)):
#     print(textArr[i])


# frames = record()

# writeFile(frames, "long.wav")

def callback(in_data, frame_count, time_info, status):
    print(type(in_data))
    writeFile(in_data,"test.wav")
    return (in_data, pyaudio.paContinue)

stream = record(callback)

time.sleep(2)

stopRecord(stream)