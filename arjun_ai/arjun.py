import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyautogui as p
import time
from playsound import playsound
import pyjokes
from translate import Translator
import subprocess
import cv2
import sys




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

name = input("what is your name")
if name == "mayank":
    speak("welcome my creator you will be avenged")

def gme():
    webbrowser.open("ev.io")
    


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am arjun Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



    
def joke():
    joke0 = pyjokes.get_joke(language='en', category= 'all')
    speak(joke0)
    print(joke0)

def haccker_mode():
    speak("haccker_mode accitivated")
    speak('sir what you want to try')
    print("[ nmap scan, nikto ,wig,whatweb,wpscanlater,theharvester, will be added in feuture versions]")
    speak("sir ... enter your prefrence")
    opt_choos = input("enter here   ").lower()
    if opt_choos ==  "nmap scan":
        tar = input("enter the ip of the target   ")
        speak("enter the type of scan")
        print("1 - TCP Connect ")
        print("2 - SYN scan")
        print("3 - UDP scan")
        print("4 - vlun scan")
        
        speak("please enter your prefrence")
        preff = int(input("enter the serial number of your chois  "))
        if preff == 1:
            print(f"wsl nmap -Pn -sT {tar}")
            os.system(f"wsl nmap -Pn -sT {tar}")

        if preff == 2:
            print(f"wsl nmap -Pn -sS {tar}")
            os.system(f"wsl nmap -Pn -sS {tar}")
        if preff == 3:
            print(f"wsl nmap -Pn -sU {tar}")
            os.system(f"wsl nmap -Pn -sU {tar}")
        if preff == 4:
            print(f"wsl nmap -Pn -sV --script nmap-vulners/ {tar}")
            os.system(f"wsl nmap -Pn -sV --script nmap-vulners/ {tar}")
        else :
            speak("done")
            print("done")
    if opt_choos == "nikto":
        target_web = input("enter the domain of the target with https or http")
        speak("enter the domain of the target with https or http")
        speak("enter the domain of the target with https or http")
        print(f"wsl nikto -h {target_web}")
        os.system(f"wsl nikto -h {target_web}")
    if opt_choos == "whatweb":
        tr = input("enter the target site name with https ")
        speak("enter the target site name with https ")
        os.system(f"wsl whatweb {tr}")
    if opt_choos == "wig":
        trgett = input("enter the target site name with https ")
        speak("enter the target site name with https ")
        os.system(f"wsl wig {trgett}")
    if opt_choos == "wpscan":
        tt= input("enter the domain address without https or http")
        speak("enter the domain address without https or http")
        os.system(f"wpscan --url {tt} -e p,vt,u")
    if opt_choos == "theharvester":
        tagg = input("enter the domain address without https or http")
        speak("enter the domain address without https or http")
        os.system(f"wsl theHarvester -d {tagg} -l 200 -b bing")
    else:
        print("enter a valid output")
        speak("enter a valid output")


def trans():
    speak("what you want to translate")
    s_p_i = input("enter the word here")
    speak("enter the language which you want to translate to")
    langop = int(input("enter the language which you want to translate to [1)german ,2)Hindi ]"))
    if langop == 1:
        translator_jerman= Translator(to_lang="German")
        translation = translator_jerman.translate(s_p_i)
        print(translation)
    if langop == 2:
        translator_hindi= Translator(to_lang="Hindi")
        translation2 = translator_hindi.translate(s_p_i)
        print (translation2)

def face_rcon():
    cascPath = sys.argv[1]
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    
        

if __name__ == "__main__":
    wish()
    while True:
        query2 = takeCommand().lower()
        if 'wikipedia' in query2:
            speak('Searching Wikipedia...')
            query2 = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query2:
            webbrowser.open("youtube.com")

        elif 'open google' in query2:
            webbrowser.open("google.com")
    
        elif 'open stackoverflow' in query2:
            webbrowser.open("stackoverflow.com")
        elif 'facebook' in query2:
            webbrowser.open("facebook.com ")
        elif 'twitter' in query2:
            webbrowser.open("twitter.com")
        elif 'instagram' in query2:
            webbrowser.open("instagram.com")
        elif 'wikipedia' in query2:
            webbrowser.open("wikipedia.org ")
        elif 'amazon' in query2:
            webbrowser.open("amazon.com")
        elif 'netflix' in query2:
            webbrowser.open("netflix.com")
        elif 'reddit' in query2:
            webbrowser.open("reddit.com")
        elif 'twitch' in query2:
            webbrowser.open("twitch.tv")
        elif 'github' in query2:
            webbrowser.open("github.com")
        elif 'game' in query2:
            gme()
        elif 'face' in query2:
            face_rcon()


        elif 'play music' in query2:
            music_dir = 'C:\\Users\\kumar\\Desktop\\arjun_ai\\arjun music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query2:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open powershell' in query2:
            codePath = "G:\\Windows\\winsxs\\x86_microsoft-windows-powershell-exe_31bf3856ad364e35_6.1.7600.16385_none_68ec54d7638638f5\\powershell.exe"
            os.startfile(codePath)

        elif 'send email ' in query2:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("plese enter the email account of the person you want to send the email to")
                to = input("enter the email here -   ")    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak(f"Sorry my friend {name}. I am not able to send this email")
        elif 'attack' in query2:
            haccker_mode()
        elif 'joke' in query2:
            joke()
        elif 'translate' in query2:
            trans()
        elif 'creator' in query2:
            speak("acctuly i was not made by a individual creator i was made by a group of creators and they were seventh graders mayank kumar , harsh gupta , aditi and shourya vatsa")
            print(" ")










































