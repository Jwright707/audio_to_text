import os
import speech_recognition as sr

os.remove("About_Rally.mp3")
os.remove("About_Rally.wav")

command2mp3 = "ffmpeg -i About_Rally.mp4 About_Rally.mp3"
command2wav = "ffmpeg -i About_Rally.mp3 About_Rally.wav"
os.system(command2mp3)
os.system(command2wav)
r = sr.Recognizer()
with sr.AudioFile('About_Rally.wav') as source:
    audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        print("Working on...")
        print(text)
    except:
        print("Sorry, try again")
