from Jarvis import JarvisAssistant
import re
import os
import random
import pprint
import datetime
import requests
import sys
import urllib.parse  
import pyjokes
import psutil
import time
import pyautogui
import pywhatkit
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_MainWindow
from Jarvis.features import templeRun
from Jarvis.config import config
from Jarvis.features import openGame
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import concurrent.futures
import subprocess

def run_script(script):
    subprocess.run(["python", script])


obj = JarvisAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

EMAIL_DIC = {
    'ashish': 'ashishpatel3009@gmail.com',
    'me': 'ashish.patel@spsu.ac.in',
    'my personal mail': 'ashishpatel3009@gmail.com',
    'harshita': 'harshita.maratha@spsu.ac.in',
    'dilkhush': 'dilkhushgiri.goswami@spsu.ac.in',
    'anjali': 'anjali.upadhyay@spsu.ac.in'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
# =======================================================================================================================================================


def speak(text):
    obj.tts(text)


app_id = "LPHGG6-R4LV4RTUE7"


def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
    
def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        wish()
    elif hour>12 and hour<18:
        wish()
    else:
        wish()
    c_time = obj.tell_time()
    



def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")
# if __name__ == "__main__":


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        # wish()

        while True:
            command = obj.mic_input()

            if re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                speak(date)

            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"Sir the time is {time_c}")

            elif re.search('launch', command):
                # dict_app = {
                #     'chrome': 'C:/Program Files/Google/Chrome/Application/chrome',
                #     'MYSQL': 'C:/Program Files/MySQL\MySQL Workbench 8.0\MySQLWorkbench.exe'
                # }   

                app = command.split(' ', 1)[1]
                # path = dict_app.get(app)

                # if path is None:
                #     speak('Application path not found')
                #     print('Application path not found')

                # else:
                #     speak('Launching: ' + app + 'for you sir!')
                #     obj.launch_any_app(path_of_app=path)

                pyautogui.keyDown("win")
                pyautogui.keyUp("win")
                time.sleep(0.5)
                pyautogui.write(app)
                print(app)
                time.sleep(0.5)
                pyautogui.press("enter")
                pyautogui.keyUp("enter")

            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)
                speak(f'Alright sir !! Opening {domain}')
                print(open_result)

            

            elif re.search('weather', command):
                city = command.split(' ')[-1]
                weather_res = obj.weather(city=city)
                print(weather_res)
                speak(weather_res)

            elif re.search('tell me about', command):
                topic = command.split(' ')[2:-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak(
                        "Sorry sir. I couldn't load your query from my database. Please try again")

            elif "buzzing" in command or "news" in command or "headlines" in command:
                news_res = obj.news()
                speak('Source: The Times Of India')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res)-2:
                        break
                speak('These were the top headlines, Have a nice day Sir!!..')

            elif 'search google for' in command:
                obj.search_anything_google(command)

            elif 'game' in command:
                speak("Which game would you like to play sir?")
                speak("Number guessing game or Rock paper scissor or temple run or subway surfers")
                gameChoice = obj.mic_input()
                if 'number' in gameChoice:
                    speak("Alright sir, starting the number guessing game")
                    speak("I am thinking of a number between 1 to 100")
                    number = random.randint(1, 100)
                    attempts = 0
                    while True:
                        speak("Take a guess")
                        guess = obj.mic_input()
                        guess = int(guess)
                        attempts += 1
                        if guess < number:
                            speak("Your guess is too low")
                        elif guess > number:
                            speak("Your guess is too high")
                        else:
                            speak(
                                f"Good job sir! You guessed the number in {attempts} attempts")
                            break
                if('rock' in gameChoice or 'paper' in gameChoice or 'scissor' in gameChoice):
                    speak("Alright sir, starting the Rock paper scissor game")
                    speak("Choose one from Rock, Paper or Scissor")
                    user_choice = obj.mic_input()
                    possible_choices = ['rock', 'paper', 'scissor']
                    comp_choice = random.choice(possible_choices)
                    speak(f"I choose {comp_choice}")
                    if user_choice == comp_choice:
                        speak("It's a tie")
                    elif user_choice == 'rock':
                        if comp_choice == 'scissor':
                            speak("You win")
                        else:
                            speak("I win")
                    elif user_choice == 'paper':
                        if comp_choice == 'rock':
                            speak("You win")
                        else:
                            speak("I win")
                    elif user_choice == 'scissor':
                        if comp_choice == 'paper':
                            speak("You win")
                        else:
                            speak("I win")
                if 'temple' in gameChoice or 'temple run' in gameChoice:
                    # speak("Alright sir, starting the temple run game")
                    # subprocess.run(["python", ".\\Jarvis\\features\\templeRun.py"])
                    # obj.temple_run()
                    # pyautogui.FAILSAFE = False
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        executor.submit(run_script, ".\\Jarvis\\features\\templeRun.py")
                        executor.submit(obj.temple_run)
                    speak("Alright sir, starting the temple run game")

                if 'subway surfers' in gameChoice or 'subway' in gameChoice or 'surfers' in gameChoice or 'subway-surfers' in gameChoice:
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        executor.submit(run_script, ".\\Jarvis\\features\\templeRun.py")
                        executor.submit(obj.subway_surfers)
                    speak("Alright sir, starting the subway-surfers game")
                    
            # elif "translator" in command or "translate" in command:
            #     speak("Opening translator")
            #     speak("Loading the speech engine")
                
            #     # Terminate previous Python programs
            #     for proc in psutil.process_iter():
            #         try:
            #             if proc.name() == "python.exe":
            #                 proc.terminate()
            #         except psutil.AccessDenied:
            #             pass  # Ignore processes we don't have permission to terminate

            #     # Specify the path to the translator script
            #     translator_script_path = r'C:\Users\ashis\Desktop\translator\SpeechTranslator.py'
                
            #     # Run the translator script using subprocess
            #     subprocess.call(['python', translator_script_path])


            elif "how do you laugh" in command or 'you laugh' in command:
                speak("Ha Ha Ha Ha Ha Ha Ha Ha Ha Ha")

            elif "how do humans laugh" in command or 'human laugh' in command:
                speak("He He Ha Ha Ha Ha He He He He")


            elif "vision" in command or "overview" in command or "environment" in command:
                speak("Alright sir, starting the road detection system")
                obj.screen_reader()

            elif "road" in command or "road detection" in command:
                speak("Alright sir, starting the road detection system")
                obj.distance_speed_detector()    
            
            elif "play music" in command or "hit some music" in command:
                music_dir = "F://Songs//Imagine_Dragons"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir, song))

            elif 'youtube' in command:
                video = command.split(' ')[1]
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

            elif "email" in command or "send email" in command:
                sender_email = config.email
                sender_password = config.email_password

                try:
                    speak("Whom do you want to email sir ?")
                    recipient = obj.mic_input()
                    receiver_email = EMAIL_DIC.get(recipient)
                    if receiver_email:

                        speak("What is the subject sir ?")
                        subject = obj.mic_input()
                        speak("What should I say?")
                        message = obj.mic_input()
                        msg = 'Subject: {}\n\n{}'.format(subject, message)
                        obj.send_mail(sender_email, sender_password,
                                      receiver_email, msg)
                        speak("Email has been successfully sent")
                        time.sleep(2)

                    else:
                        speak(
                            "I coudn't find the requested person's email in my database. Please try again with a different name")

                except:
                    speak("Sorry sir. Couldn't send your mail. Please try again")

            elif "calculate" in command:
                question = command
                answer = computational_intelligence(question)
                speak(answer)
            
            elif "what is" in command or "who is" in command:
                question = command
                answer = computational_intelligence(question)
                speak(answer)


            # ERROR Hai
            elif "what do i have" in command or "do i have plans" or "am i busy" in command:
                obj.google_calendar_events(command)

            if "make a note" in command or "write this down" in command or "remember this" in command:
                speak("What would you like me to write down?")
                note_text = obj.mic_input()
                obj.take_note(note_text)
                speak("I've made a note of that")

            elif "close the note" in command or "close notepad" in command:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            if "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "system" in command or "system stats" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            elif "battery" in command:
                battery_info = obj.battery_info()
                speak(battery_info)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                time.sleep(1)
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

            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

            elif "switch the window" in command or "switch window" in command:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

            elif "show me the screenshot" in command:
                try:
                    img = Image.open('D://JARVIS//JARVIS_2.0//' + name)
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")

            elif "hide all files" in command or "hide this folder" in command:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

            elif "visible" in command or "make files visible" in command:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

            # if "calculate" in command or "what is" in command:
            #     query = command
            #     answer = computational_intelligence(query)
            #     speak(answer)

            

            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())