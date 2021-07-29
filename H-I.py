import pyttsx3
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')                      #initialising pyttsx3 with sapi
voicess = engine.getProperty('voices')                #calling voices property from sapi
engine.setProperty('voic',voicess[0].id)              #setting voic as voice[1].id(Female voice)


def wish():                                     #Greetings
    a = time.strftime("%H:%M:%S")
    if '04:00:00' <= a <= '11:59:59':
        speak("Good Morning Sir!")
    elif '12:00:00' <= a <= '17:59:59':
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Hello! I am Friday, Please tell me how may I help you?")


def takeCommand():                              #returns our voice in string format
    r = sr.Recognizer()                         #helps in recognising audio
    with sr.Microphone() as source:             #used as source microphone
        print("Listening")
        r.pause_threshold = 1                   #it will consider the end of the task after 1 sec
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said {query}")
    
    except Exception as e:
        print("Say that again please")
        speak("Say that again please")
        return "None"
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__=="__main__":
    wish()
    while True:
        requirement = takeCommand().lower()
        if 'wikipedia' in requirement:
            speak("Searching Wiki")
            requirement = requirement.replace("wikipedia", "")
            result = wikipedia.summary(requirement, sentences=2)
            print(result)
            speak(f"According to Wiki{result}")

        elif 'open youtube' in requirement:
            webbrowser.open("youtube.com")

        elif 'open google' in requirement:
            webbrowser.open("google.com")

        elif 'play music' in requirement:
            music = "D:\\p songs"
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[0]))
        
        elif 'time' in requirement:
            t = time.strftime("%H:%M:%S")
            speak(f"Sir the time is {t}")

        elif "vs code" in requirement:
            target = "C:\\Users\\sneha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(target)

        elif "exit" in requirement:
            break