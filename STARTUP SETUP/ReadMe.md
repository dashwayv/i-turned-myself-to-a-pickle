# STARTUP - SETUP
<h2 align="center"> Automated Personalized Environment Setup.
<br> <h4 align="center"> <i>to save your precious 2 minutes, everytime everyday.</i> </h3> </h4>
<br>

* coded in python
<br>
>    So after a couple of months watching videos on Automation, drooling over projects of Michael Reeves and finally trying out Python before the semester exams begin, i finally had a bright idea of trying something out with the loads of documentations and Video knowlege, big brain w3schools texts i've been hanging with for a while <i> ( that'll maybe be like a week)</i>.
<br>
<br>
What i had in mind was a simple time-saving solution <i>(literally 2 mins not even kidding) </i> for my daily routine that'll help me keep myself productive every morning everday :)
<br>
<br>
- There is a set of things i follow each day when i startup my computer, like a freaking robot that i am - 
<br>

* Loading up Youtube 
* Loading up Netflix
* Loading up Whatsapp (For Zoom classes)
* Loading up VS CODE 
---
  ### Run
  Use any IDE, just copy the code and run in the terminal. 
  ```bash
                      python startupsetup.py                 
  ``` 
  
---
 ## (to do)
<i>
<h3>1. Opening Applications using Python</h3>
For opening applications using python, i've made use of the following models - 
<br>
<b> webbrowser: <i></b> module provides a high-level interface to allow displaying Web-based documents to users.</i>
<br>SYNTAX: webbrowser.open_new(url) 
<br>DOCUMENTATION: <a href='https://docs.python.org/3/library/webbrowser.html'> here </a> <br>
<b>os module: </b> <i> The OS module in python provides functions for interacting with the operating system. </i>
<br> note: Since
<br>
<b>pyttsx3 : </b> <i>is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3. </i>
<br>
---
> I've added custom links to open in new tabs of my default browser, while the os.startfile() was not fetching the files from the PC, i've let it be for now.
<br> Also i have added a introductory voices to make it sound more cool than this actually is.  I mean, why not xD

<br>
<br>
<h3>2. Autorun the program during Windows Startup</h3>
The next task in hand is to autorun the program as soon as Windows have been set up. 
<br><b> option 1 : Appending or adding script to windows Registry </b> 
<br>
The process involves editing the windows registry key from the script, which i was hesitant to do, so i wanted to look for a simpler approach.
<br>
<b> option 2 :  Appending or Adding script to windows Startup folder </b>
<br>
I just had to copy the script .py file into the startup folder in the windows, simpler and hopefully doesn't kill my pc.
<br>
<br>

  
  

```bash
                                       
NOTE: I've also been thinking about building up an automated Zoom bot that joins my classes and leaves on the time, or when the teacher says " I am ending the Class". I think itll cure my sleep schedule - maybe more if i could get my computer start up before a scheduled time and follow the entire class routine, smh.
  ``` 
