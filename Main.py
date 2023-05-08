import pyttsx3
import webbrowser
import smtplib
import tkinter as tk
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import time
import sys
import pyaudio


def jarvis_code():
    engine = pyttsx3.init('sapi5')
    client = wolframalpha.Client('4JLV8R-ATXGGK5AW4')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices) - 1].id)

    def speak(audio):
        print('J.A.R.V.I.S: ' + audio)
        engine.say(audio)
        engine.runAndWait()

    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning!')

        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon!')

        if currentH >= 18 and currentH != 0:
            speak('Good Evening!')

    greetMe()

    speak('Hello jero, I am your digital assistant JARVIS version 1.0')
    speak('How can I help you?')

    def myCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-in')
                print('User: ' + query + '\n')

            except sr.UnknownValueError:
                speak('Sorry ! I didn\'t get that! Try typing the command!')
                query = str(input('Command: '))

            return query

    if __name__ == '__main__':

            while True:

                query = myCommand()
                query = query.lower()

                if 'open youtube' in query:
                    speak('okay')
                    webbrowser.open('www.youtube.com')

                elif 'open google' in query:
                    speak('Opening google')
                    os.startfile(r"C:\Users\Public\Desktop\Google Chrome.lnk")
                elif 'open minecraft' in query:
                    speak('Opening minecraft')
                    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Minecraft Launcher\Minecraft Launcher.lnk")
                elif 'open opera' in query:
                    speak('Opening Opera')
                    os.startfile(r"C:\Users\User\Desktop\Opera GX Browser.lnk")

                elif 'open gmail' in query:
                    speak('okay')
                    webbrowser.open('www.gmail.com')

                elif "what\'s up" in query or 'how are you' in query:
                    stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
                    speak(random.choice(stMsgs))

                    if 'Who created you' in query:
                        speak('I was created by Jero Floyd on september sixth at 1:46 P.M, 2020')

                elif 'pause' in query or 'wait' in query:
                    speak('Ok, system paused for 2 minutes')
                    time.sleep(120)
                    speak("I'm back")
                    speak('How can i help you?')
                    recipient = myCommand()

                elif 'log out' in query or 'shutdown' in query or 'go to sleep' in query:
                    speak('are you sure you want to shutdown your computer?')
                    shutdown = input('are you sure you want to shutdown your computer?')
                    if shutdown == 'no':
                        exit()
                    else:
                        os.system("shutdown /s /t 1")


                elif 'nothing' in query or 'abort' in query or 'stop' in query or 'good bye' in query:
                    speak('okay')
                    speak('Bye , have a good day.')
                    sys.exit()

                elif 'who are you' in query:
                    speak('I am JARVIS your digital assistant. I was created by Jero on september sixth at 2:37 P.M')

                    if 'Who created you' in query:
                        speak('I was created by Jero on september sixth at 1:46 P.M')

                        if 'thanks' in query or 'thank you' in query:
                            speak("no problem! I'm always at your service!")

                elif 'bye' in query:
                    speak('Bye , have a good day.')
                    sys.exit()

                if 'who are you' in query:
                        speak('I was created by Jero on september sixth at 1:46 P.M')                     

                elif 'open minecraft' in query:
                    os.startfile(r"C:\Users\User\Desktop\TLauncher")
                    random_music = random.choice

                elif 'jarvis' in query or 'hey jarvis' in query:
                    speak("Yes!")
                    print('Yes!')

                    speak("Okay, here's your game... Enjoy mining!")



                else:
                    query = query
                    speak('Searching...')
                    try:
                        try:
                            res = client.query(query)
                            results = next(res.results).text

                            speak('Got it.')
                            speak(results)

                        except:
                            results = wikipedia.summary(query, sentences=2)
                            speak('Got it.')

                            speak(results)

                    except:
                        webbrowser.open('www.google.com')

                speak('Next Command!')

jarvis_code()

