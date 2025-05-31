import os
import time
import pyautogui
import pyttsx3
import pyaudio

import speech_recognition as sr
import csv



engine = pyttsx3.init()
engine.say("welcome to computer exhibition-2024!")
engine.runAndWait()
# Initialize recognizer
recognizer = sr.Recognizer()
B = ""
engine.say("how may i help you")
engine.runAndWait()

f= open("inst.txt","a")
while True :


    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)
        try:
        # Recognize speech using Google Web Speech API
            B=recognizer.recognize_google(audio)
            B= B.upper()
        
        except sr.UnknownValueError:
            engine.say("Sorry, I could not understand the audio.")
            engine.runAndWait()
        except sr.RequestError as e:
            engine.say(f"Could not request results; {e}")
            engine.runAndWait()


    if B== "":
        
        engine.say("Please say something")
        engine.runAndWait()


    elif "GOOGLE" in B:
        engine.say("opening google")
        engine.runAndWait()

        os.startfile("Chrome.exe")
        break

    elif "WEATHER" in B:
        name="weather"
        engine.say("showing weather")
        engine.runAndWait()
        os.startfile("Chrome.exe")
        pyautogui.write("weather")
        pyautogui.press("enter")
        break
    
    elif "OPEN" in B:
        
        h=""
        cnt = 0
        for i in B :
            if i == " ":
                cnt = cnt +1
            if cnt == 1 :
                h= h+i

        engine.say(f"opening {h}")
        engine.runAndWait()
        os.startfile("Chrome.exe")
        time.sleep(3)
        pyautogui.write(f"{h}.com")
        pyautogui.press("enter")
        break

    elif "STOP" in B:
        engine.say("I am thankful for serving you")
        engine.runAndWait()

        break
    
    
    else:
 
        engine.say("searching that on google")
        engine.runAndWait()
        os.startfile("Chrome.exe")
        time.sleep(1)
        pyautogui.write(B)
        pyautogui.press('enter')
        time.sleep(4)
        break

f.write(f"{B}\n")
    
    
f.close()