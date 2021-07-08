import pyttsx3 as pt
import subprocess as sp
import speech_recognition as sr

print("********************Hey there.....! Welcome to my Application********************")
pt.speak("********************Hey there.....! Welcome to my Application********************")
print("\n")
i=1
while i < 10:
 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("start saying...!")
  pt.speak("start saying...!")
  audio = r.record(source,duration=5)
  print("We got it, Speech done ..... plz wait")
  pt.speak("We got it, Speech done ..... plz wait")
 out=r.recognize_google(audio)
 print(out)
 if (("yourself" in out) or ("Yourself" in out)) and (("about" in out) or ("About" in out)):
  print("Hello sir, this is your assistant, JARVIS")
  pt.speak("Hello sir, this is your assistant, JARVIS")
 elif ("run" in out) and ("chrome" in out):
  sp.getoutput("chrome")
 elif (("execute" in out) or ("Execute" in out)) and (("window" in out) or ("Window" in out)) and (("Player" in out) or ("player" in out)):
  sp.getoutput("wmplayer")
 elif (("run" in out) or ("Run" in out)) and (("notepad" in out) or ("Notepad" in out) or ("editor" in out) or ("Editor" in out)):
  sp.getoutput("notepad")
 elif (("open" in out) or ("Open" in out)) and (("team" in out) or ("Team" in out)) or (("viewer" in out) or ("Viewer" in out)):
  sp.getoutput("TeamViewer")
 elif (("run" in out) or ("Run" in out)) and (("kmplayer" in out) or ("KMplayer" in out) or ("KMPlayer" in out) or ("KM Player" in out)):
  sp.getoutput("kmplayer")
 elif (("start" in out) or ("Start" in out)) and (("calculator" in out) or ("Calculator" in out) or ("calc" in out)):
  sp.getoutput("start calc")
 elif (("open" in out) or ("Open" in out)) and (("this pc" in out) or ("This pc" in out) or ("This Pc" in out) or ("My computer" in out) or ("my computer" in out) or ("My pc" in out)):
  sp.getoutput("start explorer")
 elif (("start" in out) or ("open" in out)) and (("Virtual Box" in out) or ("Virtual box" in out) or ("virtual box" in out) or ("virtualbox" in out) or ("VirtualBox" in out)):
  sp.getoutput("start virtualbox")
 elif (("Open" in out) or ("open" in out)) and (("paint" in out) or ("Paint" in out) or ("mspaint" in out) or ("ms paint" in out) or ("MS Paint" in out) or ("Ms Paint" in out)):
  sp.getoutput("start mspaint")
 elif (("start" in out) or ("open" in out)) and (("Task Manager" in out) or ("Task manager" in out) or ("task manager" in out) or ("task Manager" in out)):
  sp.getoutput("start taskmgr")
 elif (("exit" in out) or ("Exit" in out) or ("quit" in out) or ("Quit" in out)):
  print("Thank you, it was wonderful to help you.")
  pt.speak("Thank you, it was wonderful to help you.")
  exit()
 else:
  print("could not recognize your voice")
  pt.speak("could not recognize your voice")
i=i+1