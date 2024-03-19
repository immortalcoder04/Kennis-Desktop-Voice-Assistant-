import pyttsx3
import datetime
import speech_recognition as sp
import wikipedia
import webbrowser
import os
import smtplib

#==============================================================

engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#==============================================================

def speak(audio):
    engine.say(audio)
    engine.runAndWait()#Without this command, speech will not be audible to us.

#===============================================================

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak('Good Morning')
    elif hour>=12 and hour <17:
        speak('Good afternoon')
    else:
        speak('Good Evening ,sir')
    speak('Hello Sir I am Kennis ,How can i help u?')

#===============================================================

def takecommand():
    '''It takes microphone input from user 
    and response to it as requirement.
    '''
    r=sp.Recognizer()
    
    with sp.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        r.energy_threshold=200                                                      
        audio=r.listen(source)         
    
    try:
        print('Recognising...')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    
    except  :
        print("Can't Listen bro...")
        speak("Can't Listen bro")
        return 'None'
    return query

#===============================================================

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tarunroyal0409@gmail.com', 'wchaxzvmohhedxxx')
    server.sendmail('tarunroyal198@gmail.com', to, content)
    server.close()

        
#===============================================================        

# MAIN FUNCTION         
if __name__=="__main__":
    
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia',"")
            result=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'the time' in query:
            starttime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {starttime}")
        elif 'open code' in query:
            codepath="C:\\Users\\Tarun Mishra\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codepath)
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Tarun Mishra\\OneDrive\\Documents\\music'
            songs = os.listdir(music_dir)
              
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'email to tarun' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "tarunroyal198@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry bro. I am not able to send this email")
        elif 'quit' in query:
            speak('thank for using me')
            break