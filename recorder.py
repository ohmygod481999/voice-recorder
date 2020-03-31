import pyaudio
import wave
import time


class Recorder():
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = "output.wav"
        self.recording = False
        self.frames = []

    def startRecord(self):
        def stream_callback(in_data, frame_count, time_info, status):
            if self.recording:
                self.frames.append(in_data)
                callback_flag = pyaudio.paContinue
            else:
                callback_flag = pyaudio.paComplete

            return in_data, callback_flag

        self.frames = []
        self.recording = True
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK,
                                  stream_callback=stream_callback)

        print("* recording")

    def stopRecord(self):
        print("* done recording")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.stream = None
        return self.frames

    def resetFrame(self):
        self.frames = []

    def writeFile(self, frame,  fileName):
        wf = wave.open(fileName, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frame))
        wf.close()


# recorder = Recorder()

# recorder.record()

# time.sleep(2)

# recorder.stopRecord()
