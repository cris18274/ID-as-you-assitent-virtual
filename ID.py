#Asistente virtual

import pyttsx3  # recoder --> terminal: pip install pyttsx3
import datetime
import speech_recognition as sr  #recorder---> terminal: pip install speechRecognition
import wikipedia  #recorder----> terminal: pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #recorder-----> terminal: pip install psutil
import pyjokes #recorder----->terminal: pip install pyjokes
import os
import pyautogui #recorder----->terminal: pip install pyautogui
import random
import wolframalpha #recorder------>terminal: pip install wolframalpha
import json
import requests
from urllib.request import urlopen
import time


engine = pyttsx3.init()
wolframalpha_app_id = 'wolfram alpha id will go here'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 12 hour clock
    speak("The current time is")
    speak(Time)

#time_()

def date_()
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

#date_() 

def wishme():
    speak("Welcome back User!")
    time_() 
    date_()

    #Greetings
 
    hour = datetime.datime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning User!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon User!")
    elif hour>=18 and hour<24:
        speak("Good Evening User!")
    else:
        speak("Good Night User!")

    speak("ID at your service. Please tell me how can I help you today?")

#wishme()

def TakeCommand():  
    r=sr.Recognizer()
    with sr.Micrphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
         print(e)
         print("Say that again please.....")
         return "None"
    return query 

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    #for this function, you must enable low security in you gmail which you are going to use as sender
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to.content)
    server.close()

def screenshot():
    img= pyautogui.screenshot
    img.save('C:/Users/screenshot.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)  

def joke():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
   
    wishme()

    while True:
        query = TakeCommand().lower()

        #All commands will be stored in lower case in query 
        #for easy recognition
     
        if 'time' in query: # tell us time whe asked
            time_()

        elif  'date' in query: # tell us date when asked 
            date_()

        elif 'wikipedia' in query:
            speak("Searching.....")
            query=query.replece('wikipedia','')
            result=wikipedia.summary(query,sentence=3)
            speak('Acording to Wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=TakeCommand()
                #provide reciever email address

                speak("Who is the Reciever?")
                reciever=input("Enter Reciever's Email:")
                reciever='reciever_is_me@gmail.com'
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')

             except Exception as e:
                 print(e)
                 speak("Unable to send Email.")
          elif 'search in chrome' in query:
               speak('What should I search?')
               chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#Chromepath is location of chrome's installation on Computer

               search = TakeCommand().lower()
               wb.get(chromepath).open_new_tab(search+'.com')  #only open websites with '.com' at end.
               
          elif 'search youtube' in query:
              speak('What should I search?')
              search_Term = TakeCommand().lower()
              speak("Here We go to YOUTUBE!")
              wb.open('https://www.youtube.com/results?search_query='+search_Term)
          
          elif 'search google' in query:
              speak('What should I search?')
              search_Term = TakeCommand().lower()
              speak('Searching.....')
              wb.open('https://www.google.com/search?q='+search_Term)


           elif 'cpu' in query:
               cpu()
           
           elif 'joke' in query:
               joke()

           elif 'go offline' in query:
               speak('Going Offline User!')
               quit()
       
           elif 'world' in query:
               speak('Opening MS Word.....')
               ms_word = r'E:/Office/Office16/WINWORD.EXE'
               os.startfile(ms_word)
  
           elif 'write a note' in  query:
               speak("What should I while, User?")
               notes = TakeCommand()
               file = open('notes.txt','w')
               speak("User should I include Date and Time?")
               ans = TakeCommand() 
               if 'yes' in ans or 'sure' in ans:
                  strTime = datetime.datetime.now().strftime("%H:%M:%S")
                  file.write(strfTime)
                  file.write(':-')
                  file.write(notes)          
                  speak('Done Taking Notes, User!')
               else:
                   file.write(notes)
           elif 'show note' in query:
               speak('showing notes')
               file = open('notes.txt','r')
               print(file.read())
               speak(file.read())
           elif 'screenshot' in query:
               screenshot()
           
          elif 'play music' in query:
              song_dir = 'D:/SONGS'
              music = is.listdir(song_dir)
              speak('What should I play?')
              speak('select a number.....')
              ans = TakeCommand().lower()
              while('number' not in ans and ans != 'random' and ans != 'your choose'):
                  speak('I could not undestand you. Please Try Again.') 
                  ans = TakeCommand().lower()
              if 'number' in ans:
                  no = int(ans.replace('number',''))
              elif 'random' or 'you choose' in ans:
                  no = random.randint(1,100)
                  
              os.startfile(os.path.join(songs_dir,music[no]))

          elif 'calculate' in query:
              client = wolframalpha.Client(wolframalpha_app_id)
              indx = query.lower().split().index('calculate')
              query = query.split()[indx + 1:]
              res = client.query(''.join(query))
              answer = next(res.results).text
              print('The Answer is : '+answer)
              speak('The Answer is'+answer)

          elif 'what is' in query or 'who is' in query:
              #use the same API key that we generated earlier i.e. wolframalpha
              client = wolframalpha.Client(wolframalpha_app_id)
              res = client.query(query)

              try:
                  print(next(res.results).text)
                  speak(next(res.results).text)
              except StopIteration:
                  print("No Results")
                  
    
          elif 'remember that' in query:
              speak("What shoul I remember?")
              memory = TakeCommand()
              speak("You asked me to remember that"+memory)
              remember = open('memory.txt','w')
              remember.write(memory)
              remember.close()

          elif 'do you remember anything' in query:
              remember = open('memory.txt','r')
              speak('You asked me to remember that'+remember.read())

          elif 'where is' in query:
              query = query.replace("where is","")
              location = query
              speak("User asked to locate"+location)
              wb.open_new_tab("https://www.google.com/maps/place/"+location)

         
          elif 'news' in query:
              try:
                  jsonObj = urlopen("http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-21&sortBy=publishedAt&apiKey=API_KEY")
                  data = json.load(jsonObj)
                  i = 1
 
                  speak('Here are some top headlines from the Entertainment Industry')
                  print('==========TOP HEADLINES=========='+'\n')
                  for item in data['articles']:
                      print(str(i)+'. '+item['title']+'\n')
                      print(item['description']+'\n')
                      speak(item['title'])
                      i += 1
              except Exception as e:
                      print(str(e))
          
          elif 'stop listening' in query:
              speak('For How many second you want me to stop listening to your commands?')
              ans = int(TakeCommand())
              time.sleep(ans)
              print(ans)

          elif 'log out' in query:
              os.system("shutdowm -l")
          elif 'restart' in query:
              os.system("shutdowm /r /t 1")
          elif 'shutdowm' in query:
              os.system("shutdowm /s /t 1")
 
   #make ID app   #transform .py to .exe    
  #recorder terminal: pip install pyinstaller
  # use command cd.. for navegate to desktop
  # introduce in terminal: pyinstaller --onefile 'ID.py'


           
          
              

       

 

 




