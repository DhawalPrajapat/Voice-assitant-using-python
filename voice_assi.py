import pyttsx3            #convert text to speech
import speech_recognition as sr
import webbrowser         #search on browser
import datetime
import pyjokes
import os
import time
import wikipedia
import smtplib

#Function of speech to text
def sptext():
    # create variable as object
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # to reduce ambient noise in the background
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            data = r.recognize_google(audio,language='en-in')
            print(f"User said: {data}\n")
            return data

        except Exception as e:
            print("Say that again please.....")
            return "None"
        return data
# sptext()


#function of text to speech
def speak(x):
    engine = pyttsx3.init()
    #get voice
    voices = engine.getProperty('voices')
    #set voice male,female or others
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    # set speed of voice
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

# speak("Hello Welcome to Dhawal erra")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am friday sir. please tell me how may i help you")


# def sendEmail(to,content):



#this conditional statement is use for split program (you can say this main part our program from here)
if __name__ == '__main__':

    # if "friday" in sptext().lower():
        wishMe()

        while True:

                data1 = sptext().lower()
                if "your name" in data1:
                    name = "my name is friday"
                    speak(name)
                elif "old are you" in data1:
                    age = "i am 2 years old"
                    speak(age)

                elif "are you" in data1:
                    age = "i am good and you"
                    speak(age)

                elif "good" in data1:
                    age = "ohhh"
                    speak(age)

                elif "wikipedia" in data1:
                    speak("Searching Wikipedia...")
                    wiki = data1.replace("wikipedia","")
                    results = wikipedia.summary(wiki,sentences = 2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)

                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p") #first datetime() is module and another is function and strftime(%I = hours %M = minute %p = am/pm)
                    speak(f"The current time is {time}")

                elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")

                elif "google" in data1:
                    webbrowser.open("https://www.google.com/")

                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en",category="chuck")
                    print(joke_1)
                    speak(joke_1)

                elif "song" in data1:
                    ad = "E:\music"
                    listsong = os.listdir(ad)
                    print(listsong)
                    os.startfile(os.path.join(ad,listsong[1]))

                elif "open code" in data1:
                    codepath = "X:\\Python_VS\\Project\\Voice_assistant\\voice_assi.py"
                    os.startfile(codepath)

                elif "by" in data1:
                    th = "okay boss!Thank you"
                    speak(th)
                    break



#else:
#   print("Thanks")


