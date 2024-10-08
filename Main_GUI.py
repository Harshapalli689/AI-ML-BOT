from AIBrain import ReplyBrain #Brain of the Automation Bot using chat_log txt and api to talk.
from Qna import QuestionsAnswer#To answer for the technical questions to that answered by the automation bot.
from date_time import date,time#This is date & time function to know the date & time now.
from wikipedia import tell_me_about#This searchs the content from the webbrowser wikipedia for the user Data to know from the google.
from AppOpener import close,open#This will close and the applications that are running or installed in windows.
from youtube_search import Search#This will search the required videos for the user from the youtube.
from website_open import website_opener#This will opens the Google chrome and searchs what that the user required from the bot from google.
from sendmsgwhatsapp import send_whatsapp_message#This is used by the bot that the user need to send a specified message for the required user.
from google_calendar import get_date,get_events,authenticate_google
from loc import my_location,loc#This  is used to get the location of the user.
import pyjokes#To make jokes by bot
from system_stats import system_stats#System statistics of my windows.
import os#This is used by the bot to handle the os.
from systeminfo import sysinfo#To get the information of the System.
import sys#This is to go offline of bot.
from time import*
from pygame import mixer #This is used to play the notification sound for the tasks speficied in the tasks file. 
from plyer import notification#This is used to notify the Tasks in the Tasks.txt file.
import pyautogui#This is used to Perform the tasks.
from tasks import task,show#This is used to set and show the task.
from Alaram import alarm# This is used to set the alarm.
from remember import remem,remembered #This is used to remember the things that the user told to pc.
from tkinter import*
from PIL import Image, ImageTk
import datetime
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PCbotUI import Ui_MainWindow
import os
import sys
import pywhatkit
import webbrowser as web
import speech_recognition as sr#This is used by the bot to Listen the words of the human or Voice Recognition.
import pyttsx3
from Face_Detector import Facescan,face
from Captureimage import unauthorized
# 1 - Listen : Hindi or English

def Listen():
    bot.updateMoveDynamically("listening")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        bot.terminalPrint("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        bot.updateMoveDynamically("loading")
        bot.terminalPrint("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    return query

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
def speak(text):
        """
        Convert any text to speech
        :param text: text(String)
        :return: True/False (Play sound if True otherwise write exception to log and return  False)
        """
        bot.updateMoveDynamically("speaking")
        try:
            engine.say(text)
            bot.terminalPrint(f"AI : {text}.")
            print(f"\nAI : {text}.")
            engine.runAndWait()
            engine.setProperty('rate', 175)
        except:
            t = "Sorry I couldn't understand and handle this input"
            bot.terminalPrint(t)
      
def wishme():
    bot.updateMoveDynamically("speaking")  
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        text = "\n Good Morning sir. I am Your PC Bot. How can I Assist you?"
    elif 12 <= hour < 18:
        text = "\n Good Afternoon sir. I am Your PC Bot. How can I Assist you?"
    else:
        text = "\n Good Evening sir. I am Your PC Bot. How can I Assist you?"
    speak(text)
class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.MainExecution()
    def MainExecution(self):
        speak("Starting with Face Recognition Sir")
        speak("Please Stay on Front of Camera Sir..")
        speak("Show Your Face Camera and make gentle smile sir..")
        if  face()!=True:
            speak("YOUR ARE NOT A AUTHORIZED PERSON TO ACCESS THE SYSTEM SIR..")
            speak("Go from in Front of PC")
            unauthorized()
            exit(0)
        else:
            import time
            speak("CAM ACCESSED")
            time.sleep(0.2)
            speak("YOU ARE AUTHORIZED TO ACCESS ME SIR..")
        bot.terminalPrint(">> Starting The PC bot : Wait For Some Seconds.")
        bot.terminalPrint("\n >> Starting The PC bot : Wait For Few Seconds More")
        speak("Hello Sir")
        wishme()
        while True:
            Data = Listen()
            Data = str(Data)
            bot.terminalPrint(f"You Said : {Data}")
            from date_time import time,date
            if "time now" in Data:
                speak("Now the time is")
                speak(time())
            elif "date" in Data:
                speak("Todays date is")
                speak(date())

            elif "go to sleep" in Data:
                speak("Ok sir , You can call me anytime")
                break

            elif "system info" in Data:
                speak("Your pc info is")
                sysinfo()

            elif "windows statistics" in Data:
                speak("your pc statistics are")
                speak(system_stats())

            elif "joke" in Data or "jokes" in Data or "pc joke" in Data:
                joke = pyjokes.get_joke()
                bot.terminalPrint(joke)
                speak(joke)
            elif "turn on the tv" in Data:# Specific COmmand
                speak("Ok..Turning On The Android TV")

            elif "what is" in Data or "question" in Data or "answer" in Data:
                Reply = QuestionsAnswer(Data)
                speak(Reply)

            elif ("search in chrome" in Data) or ("open chrome" in Data) or ("google" in Data):
                speak("opening")
                speak("What I have to Search sir..")
                domain=Listen()
                website_opener()

            elif "hide all files" in Data or "hide this folder" in Data:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

            elif "visible" in Data or "make files visible" in Data:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

            elif "tell me about" in Data:
                speak(tell_me_about(Data))

            elif "goodbye" in Data or "offline" in Data or "bye" in Data:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()

            elif "where is my location" in Data:
                import time
                speak("Hold on sir it is opening on your screening")
                web.open("https://www.google.com/maps")
                time.sleep(0.2)
                speak("see on your screen sir")
                
            elif "where is" in Data:
                place = Data.split('where is ', 1)[1]
                current_loc, target_loc, distance =loc(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                except:
                    res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    speak(res)

            elif ("calendar" in Data) or ("events" in Data) or ("days" in Data):
                speak("Tell me the date sir..")
                text=Listen()
                text=text.lower()
                service =authenticate_google()##I have to make execute ##
                date =get_date(text)
                if date:
                    get_events(date, service)

            elif ("open WhatsApp" in Data) or ("WhatsApp" in Data) or ("message using whatsapp" in Data) or ("message" in Data):
                speak("Opening Whatsapp Sir!!")
                speak("What message i have to send Sir!!")
                quer=Listen()
                speak(f"Searching sir.")
                text=quer.lower()
                send_whatsapp_message(text)

            elif "search youtube" in Data or "youtube" in Data:
                speak("Opening Youtube Sir!!")
                speak("What i have to search Sir!!")
                quer=Listen()
                speak(f"Searching sir.")
                text=quer.lower()
                Search(text)

            elif "schedule my day" in Data:
               speak("Task is scheduling")
               task()

            elif "show my schedule" in Data:
                show()
                
            elif "internet speed" in Data:
                import speedtest
                wifi  = speedtest.Speedtest()
                upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                download_net = wifi.download()/1048576
                speak(f"Wifi download speed is {download_net}")
                speak(f"Wifi Upload speed is {upload_net}")

            elif "ipl score" in Data:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
                    a = bot.terminalPrint(f"{team1} : {team1_score}")
                    print(f"{team1} : {team1_score}")

                    b = bot.terminalPrint(f"{team2} : {team2_score}")
                    print(f"{team2} : {team2_score}")
                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )
                    
            elif "play a game" in Data:
                    from game import game_play
                    game_play()
        
            elif "screenshot" in Data:
                import pyautogui #pip install pyautogui
                im = pyautogui.screenshot()
                im.save("scrsht.jpg")
        
            elif "click my photo" in Data:
               import pyautogui
               pyautogui.press("super")
               pyautogui.typewrite("camera")
               pyautogui.press("enter")
               pyautogui.sleep(2)
               speak("SMILE")
               pyautogui.press("enter")

            elif "one tab" in Data or "1 tab" in Data:
              speak("Closing,sir")
              import pyautogui
              pyautogui.hotkey("ctrl","w")
              speak("All tabs closed")

            elif "2 tab" in Data:
              import pyautogui
              pyautogui.hotkey("ctrl","w")
              sleep(0.5)
              pyautogui.hotkey("ctrl","w")
              speak("All tabs closed")
              
            elif "3 tab" in Data:
                import pyautogui
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All tabs closed")
                
            elif "4 tab" in Data:
                import pyautogui
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All tabs closed")
                
            elif "5 tab" in Data:
                import pyautogui
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All tabs closed")

            elif "hello" in Data:
                speak("Hello sir, how are you ?")

            elif "i am fine" in Data:
                speak("that's great, sir")

            elif "how are you" in Data:
                speak("Perfect, sir")

            elif "thank you" in Data:
                speak("you are welcome, sir")

            elif "pause" in Data:
                import pyautogui
                pyautogui.press("k")
                speak("video paused")
            elif "play" in Data:
                import pyautogui
                pyautogui.press("k")
                speak("video played")
            elif "mute" in Data:
                import pyautogui
                pyautogui.press("m")
                speak("video muted")

            elif "news" in Data:
                from NewsRead import get_news##Have to add apis
                speak(get_news)

            elif "temperature" in Data:
                import requests 
                from bs4 import BeautifulSoup
                search = "temperature in my place"
                url = f"https://www.google.com/search?q={search}"
                r  = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_ = "BNeawe").text
                speak(f"current temperature in your place is {temp}")

            elif "weather" in Data:
               import requests 
               search = "temperature in my place"
               from bs4 import BeautifulSoup
               url = f"https://www.google.com/search?q={search}"
               r  = requests.get(url)
               data = BeautifulSoup(r.text,"html.parser")
               temp = data.find("div", class_ = "BNeawe").text
               speak(f"current weather in your place is {temp}")

            elif "set an alarm" in Data:
               bot.terminalPrint("input time example:- 10 and 10 and 10")
               speak("input time example:- 10 and 10 and 10")
               speak("Set the time")
               speak("Please tell the time :- ")
               a=input("set the time by manual like 10and10and10")
               alarm(a)
               speak("Done,sir")
        
            elif "remember that" in Data:
               rememberMessage = Data.replace("remember that"," ")
               rememberMessage = Data.replace("pc" or "bot","")
               speak("You told me "+rememberMessage)
               remem(rememberMessage)
           

            elif "what do you remember" in Data:
               remembered()

            elif "volume up" in Data:
               from keyboard import volumeup
               speak("Turning volume up,sir")
               volumeup()

            elif "volume down" in Data:
               from keyboard import volumedown
               speak("Turning volume down, sir")
               volumedown()

            elif "shutdown system" in Data:
               speak("Are You sure you want to shutdown")
               shutdown = Listen()
               if shutdown == "yes":
                  os.system("shutdown /s /t 1")
               elif shutdown == "no":
                   break
        

            elif "open" in Data:#for opening windows apps
               app_name = Data.replace("open ","")
               speak("opening")
               speak(app_name)
               open(app_name, match_closest=True)

            elif "close" in Data:#closing the windows apps
               app_name = Data.replace("close ","").strip()
               speak("closing")
               speak(app_name)
               close(app_name, match_closest=True, output=False) # App will be close be it matches little bit too (Without bot.terminalPrinting context (like CLOSING <app_name>))
        
            else:
              if Data!=""  and Data!=[]:
                  Reply = ReplyBrain(Data)
                  speak(Reply)
startExe = MainThread()
class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_exit.clicked.connect(self.close)
        self.gui.pushButton_chrome.clicked.connect(self.chrome_app)
        self.gui.pushButton_what.clicked.connect(self.what_app)
        self.gui.pushButton_you.clicked.connect(self.yt_app)

    def __del__(self):
        sys.stdout = sys.__stdout__
     
    def terminalPrint(self,text):
        self.gui.plainTextEdit.setReadOnly(True)
        self.gui.plainTextEdit.appendPlainText(text)
        self.gui.plainTextEdit.setFont(QFont('Times', 12))
        self.gui.plainTextEdit.verticalScrollBar().setValue(self.gui.plainTextEdit.verticalScrollBar().maximum())
    
    def updateMoveDynamically(self,state):
        if state=="speaking":
            self.gui.speaking.raise_()
            self.gui.speaking.show()
            self.gui.Listening.hide()
            self.gui.loading.hide()
            
        elif state=="listening":
            self.gui.Listening.raise_()
            self.gui.Listening.show()
            self.gui.speaking.hide()
            self.gui.loading.hide()
            
        elif state=="loading":
            self.gui.loading.raise_()
            self.gui.loading.show()
            self.gui.speaking.hide()
            self.gui.Listening.hide()        
        
    def chrome_app(self):
        os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")
    
    def yt_app(self):
        pywhatkit.playonyt("beliver song")
    
    def what_app(self):
        web.open("http://web.whatsapp.com/")
    
    def startTask(self):

        self.gui.label= QtGui.QMovie("..//..//..//Downloads//chatbot-unscreen.gif")
        self.gui.GIF_1.setMovie(self.gui.label)
        self.gui.label.start()
        
        self.gui.loadingMovie= QtGui.QMovie("../../../Downloads/load.gif")
        self.gui.loading.setMovie(self.gui.loadingMovie)
        self.gui.loadingMovie.start()
        
        self.gui.speakingMovie= QtGui.QMovie("../../../Downloads/speak.gif")
        self.gui.speaking.setMovie(self.gui.speakingMovie)
        self.gui.speakingMovie.start()
        
        self.gui.ListeningMovie= QtGui.QMovie("../../../Downloads/listening.gif")
        self.gui.Listening.setMovie(self.gui.ListeningMovie)
        self.gui.ListeningMovie.start()
        
        timer=QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

        self.tempershow()
        self.Dayshower()
    
        startExe.start()
        
    def tempershow(self):
        import requests 
        from bs4 import BeautifulSoup
        search = "temperature in my place"
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        self.gui.Temp_show.setText("  Temperature : "+temp)
        self.gui.Temp_show.setFont(QFont('Times', 12))
    
    def Dayshower(self):
        from datetime import datetime
        # get current datetime
        dt = datetime.now()
        self.gui.Day_show.setText('  Day-Name:'+dt.strftime('%A'))
        self.gui.Day_show.setFont(QFont('Times', 12))
        
    def showTimeLive(self):
        t_ime=QTime.currentTime()
        time=t_ime.toString()
        d_ate=QDate.currentDate()
        date=d_ate.toString()
        label_Time="Time :"+time
        label_date="Date :"+date
        
        self.gui.Time_show.setText("  "+label_Time)
        self.gui.Time_show.setFont(QFont('Times', 12))
        self.gui.Date_show.setText("  "+label_date)
        self.gui.Date_show.setFont(QFont('Times', 12))
app = QApplication(sys.argv)
bot = Gui_Start()
bot.show()
exit(app.exec_())

