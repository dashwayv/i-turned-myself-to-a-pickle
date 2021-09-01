""" STARTUP SETUP : Automating the startup environment for daily tasks """
import pyttsx3
import os
import webbrowser
import subprocess

engine=pyttsx3.init()
voices=engine.getProperty('voices')

engine.setProperty('voices',voices[1].id)
engine.runAndWait()

#Setting up the environment
print(" ==== STARTUP - SETUP =====")
engine.say('Hello, Wayvee') #enter name
pyttsx3.speak(" Setting up your environment ")

#system programs to open - enter your online url links and application path.
url_youtube='https://www.youtube.com/'
url_netflix='https://www.netflix.com/browse'
url_whatsapp='https://web.whatsapp.com/'
#path_vscode= r'C:\Users\shant\AppData\Local\Programs\Microsoft VS Code\Code.exe'
#path_notion=r'C:\Users\shant\AppData\Local\Programs\Notion\Notion.exe'


webbrowser.open_new(url_youtube)
webbrowser.open_new(url_netflix)
webbrowser.open_new(url_whatsapp)

# idk why the code below is not working smh
subprocess.call(r'C:\Users\shant\AppData\Local\Programs\Microsoft VS Code\Code.exe') #call VSCODE
subprocess.call(r'C:\Users\shant\AppData\Local\Programs\Notion\Notion.exe') #call NOTION

""" Since chrome is my default browser, else 
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open_new(url_youtube) 

"""
