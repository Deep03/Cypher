import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume',1.0)
count = 0
dir1 = "E:\Music"

for path in os.listdir(dir1):
    if os.path.isfile(os.path.join(dir1, path)):
        count += 1
rr= random.randint(0,count)
contact = {"Dad":'maheshlek@yahoo.com' ,
           "sister":'samikshyalekhak2@gmail.com' ,
           "brother":'deepaklekhak10@gmail.com'}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        if query =='hi fred' or query=='hey friend' \
                or query=="hi friend" or\
                query=="friend" or query=="April":
            speak("Hi sir , How may I help you")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def search_wikipedia():
        query1 = query.split('is'or'was'or'were'or'are')[0]
        speak('Searching Wikipedia...')
        query2 = query1.replace("wikipedia", "")
        results = wikipedia.summary(query2, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('lekhakdeepak10@gmail.com', 'Justwantpeace2003')
    server.sendmail('lekhakdeepak10@gmail.com', to, content)
    server.close()


def music():
    dir1 = 'E:\Music'
    songs = os.listdir(dir1)
    os.startfile(os.path.join(dir1, songs[rr]))

def remainder():
    pass

def accessingsites():
    b = query.split('open')[1]
    if '.com' in b:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(b)
    else:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(b + '.com')

def poweroptions(query):
    if 'shutdown' in query:
        os.system("shutdown /s /t 1")

    if 'restart' in query:
       os.system("shutdown /r /t 1")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'play music' in query:
            music()

        elif 'who' or 'what' in query:
            search_wikipedia()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send email' in query:
            try:
                global email
                speak("To whom sir")
                reciever = takeCommand().split()[1]
                for i, j in contact.items():
                    if reciever == i :
                        email = j
                speak("What should I send sir ?")
                content = takeCommand()
                sendEmail(email, content)
                speak("Email has been sent") , print("Email has been sent")
            except Exception as e:
                print(e)

        elif 'remind me to' or 'set a remainder':
            remainder()

        elif 'shutdown' or 'restart' in query:
            poweroptions(query)
