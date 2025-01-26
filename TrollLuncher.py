from tkinter import *
import time
import random
import pyautogui
import os
import sys
import webbrowser

def antivirus():
    os.startfile('notepad.exe')
    time.sleep(0.1)
    pyautogui.write("Tu t'es fait hacker imbecile", interval=0.1)                

def infinitmouse():
    while True:
      mousex = random. randint(0, 1600)
      mousey = random. randint(0, 1031)
      pyautogui.moveTo(mousex, mousey)
     
def duplication():
 
       window = Tk()
       window.title("Duplicate")
       window.command = duplication
       window.maxsize(500,600)
       window.minsize(500,600)
       label = Label(window, text="You have duplicate this window",bg = 'white', font= (60),)
       label.pack()
       
       button = Button(window, text="Duplic a object",bg= 'red', command = duplication)
       button.pack
       button.place(x= 0, y=200)
       
       window.mainloop()

def CMDspam():
    while True:      
      os.system("start cmd")
      continue

def deletwar():
    print("to solve a war, delete zombies gamemode")

def zombies():
    if sys.platform.startswith('win32'):
      if sys.getwindowsversion().major == 10:
         
         width, height = pyautogui.size()
         if (width, height) == (1680,1050):
            pyautogui.dragTo(25, 1026, 1)
            pyautogui.click(button='right')
            pyautogui.dragTo(30, 984, 1)
    
            pyautogui.dragTo(315, 962, 1)

            pyautogui.dragTo(345, 929, 1)
            pyautogui.click(button='right')
         else:
              os.system('shutdown -s')

      elif sys.getwindowsversion().major == 11:
        os.system('shutdown -s')
        print("your computer will shutdown ?")
        time.sleep(2)
        print("there is nothing you can do")
        time.sleep(2)
        print("what a sad life...")
      else:
        print("This button only work on windows")


def discomouse():
    video_url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
    os.system("start " + video_url)
    
    while True:
      mousex = random. randint(0, 1600)
      mousey = random. randint(0, 1031)
      pyautogui.moveTo(mousex, mousey)


def adminpanel():
    window = Tk()
    window.maxsize(1000,990)
    window.minsize(1000,990)
    window.title("why do you look at the title ?")
    
    label = Label(window, text="Great Life, by snowad",bg = 'white', font= (60))
    label.pack()
    
    label = Label(window, text="Warning, save your important work before ",bg="red", fg ="white",font= (60))
    label.place(x=0, y=400)
    label = Label(window, text="pressing the red button",bg="red", fg ="white",font= (60))
    label.place(x=0, y=425)
    
    
    button = Button(window, text="Infinit money glitch", bg='#0093ff', height=10, width=40, command = infinitmouse)
    button.place(x= 50, y=100)
    button.pack()
    
    button = Button(window, text="Duplication glitch IRL", bg='#0093ff', height=10, width=40, command = duplication)
    button.place(x= 50, y=200)
    button.pack()
    
    button = Button(window, text="spam your sibilings", bg='red', height=10, width=40, command = CMDspam)
    button.place(x= 50, y=300)
    button.pack()
    
    button = Button(window, text="Peace in the world", bg='#0093ff', height=10, width=40, command = deletwar)
    button.place(x= 50, y=400)
    button.pack()
    
    button = Button(window, text="delet Zombies", bg='red', height=10, width=40, command = zombies)
    button.place(x= 50, y=500)
    button.pack()
    
    button = Button(window, text="Disco mouse", bg='#0093ff', height=10, width=40, command = discomouse)
    button.place(x= 25, y=25)
    
    button = Button(window, text="Activé antiviruse", bg='#0093ff', height=10, width=40, command = antivirus)
    button.place(x= 25, y=185)
    
   

    window.mainloop()
#___________________________________________________________________________________________________________________________________________
from math import *
from tkinter import Tk, Button, Label
import time



def secretboom():

  print("starting...")
  time.sleep(2)
  print("BrainPY.v.1.0 ready")

  time.sleep(3)
  str(input("[insert a stupid thing]"))
  time.sleep(1)

  print("did you just say somthing ?")
  time.sleep(2)

  print("i wasn't talking to you")
  time.sleep(1)
  str(input("[insert a stupid thing]"))

  time.sleep(3)
  print("you wanna play this game ?")
  time.sleep(1)
  print("we gonna play...")
  time.sleep(0.1)
  print("Booting...")
  time.sleep(3)
  
  print("starting...")
  time.sleep(2)
  print("BrainPY.v.1.0 ready")

  time.sleep(3)
  name = str(input("what is your name ?"))
  smoll = " smell like a trash"
  time.sleep(1)
 
  print("...")
  time.sleep(3)
  while True:
    print(name, smoll)
    continue
##____________________________________________________
def vault():
    print("starting...")
    time.sleep(2)
    print("VaultPy.v.1.3 ready")

    time.sleep(3)
    print("HOW DID YOU GET THERE ?")
    time.sleep(2)
    print("you have destroyed my protection in less than 10 minutes ! ")
    time.sleep(2)
    print("mAYbE you are here, but im sure you doesn't have the passwords.")
    passask()
#_______________________________________________________________________________
def passask():     
    time.sleep(2)
    passe = str(input("Have you the pasword ?"))
    
   
    if passe == ("Yousmellbad"):
      time.sleep(2)
      print("idk who just choos this pasword but i hope for you you arn't talking about me... ")
      time.sleep(2)
      passask()
  
    if passe == ("HopeYouDie"):
      time.sleep(2)
      print("i think you dont know who is the bosse")
      problem()      
      
    
    if passe == ("BrainPY"):
        print("why are you talking about brain ?")
        time.sleep(2)
        print("idk why are you talking abouthim..")
        time.sleep(2)
        passask()

    if passe == ("Pythagore"):
       print("since my 4minute on this script i always hate math")
       time.sleep(1)
       print("and guess what ?")
       time.sleep(3)
       print("I LITTERALY SPAWN IN A MATH SCRIPT")
       time.sleep(2)
       passask()

    if passe == ("poop"):
        print("conguration, you win !")
        time.sleep(2)
        passask()

    if passe == ("password"):
       print("yes this is a password")
       time.sleep(2)
       passask()
    
    if passe == ("exit"):
       print("you finaly leav me alone")
       pythongore()
       
    if passe == ("python"):
        print("The Royal Python (Python regius) is one of the snakes of the Python1 family. There are more African pythons and a popular pet. No subspecies is recognized to date2. It is a constrictor snake, however, do not use the royal name Python or Ball Python. The first thing I see is the fact that the queen of the cloak should have accustomed the wearer of these snakes to these cuffs. After a second, he will recover from the animal's tendency on his paw and he will then receive a message.")
        
    if passe == ("Admin"):
      Admin()
    
    if passe == ("sURPRISE"):
      print("yOU wANt A sUrpRISe, I wiILL Give yOu One")
      thesurprise()
    
    if passe == ("TERMINAL"):
       time.sleep(1)
       print("Terminal ?, i think its bc im in a terminal, i can be a app too")
       graphic()
    
    
    if passe == ("locked>snowad"):
        time.sleep(1)
        print("whatch this")
        time.sleep(1)
        locked()

#_____________________________________________________________________________________
        
def problem():
    window = Tk()
    window.minsize(300, 100)
    window.maxsize(300, 100)
    window.title("eRrOR")
    
    label = Label(window, text="error")
    label.pack()
    
    
    button = Button(window, text="solve the error", bg ='red', command=problemspam)
    button.pack()
    
    
    window.mainloop

def error():
    window = Tk()
    window.minsize(300, 100)
    window.maxsize(300, 100)
    window.title("eRrOR")
    
    label = Label(window, text="error")
    label.pack()

def problemspam():
    pagenum = 0
    while pagenum == 15:
          error()
          pagenum + 1 
         

#_____________________________________________________________________________________
def graphic():

   window = Tk()
   window.minsize(500, 300)
   window.config(background='black')
   window.title("The Graphic me")
   
   label = Label(window, text="I can be a graphic version", bg='white', font=("Courier", 30))
   time.sleep(2)
   
   label2 = Label(window, text="now, lets return to our Terminal", bg='white', font=("Courier", 20))
   label2.place(y=100)
   
   label.pack()
   
   button = Button(window, text="TERMINAL", command=window.destroy)
   button.place(x=55, y= 150)
   
   button.pack
   
   window.mainloop()
   
   time.sleep(2)
   print("snowad code like a kid, thats why im not graphic but terminal")
   time.sleep(2)
   print("and thats why this page was like a nothing")
   time.sleep(1.5)
   
   passask()
#_____________________________________________________________________________________
def thesurprise():
    
    window = Tk()
    window.minsize(220, 200)
    window.maxsize(220, 200)
    window.config(background='#61c3d6')
    window.title("ThE suRPrIsE !")
      
    button = Button(window, text="Push me !", command=thesurprise)
    button.place(x=55, y=50)

    button = Button(window, text="STOP", command=window.destroy)
    button.place(x=55, y=0)
    
    
    button.pack()

    window.mainloop()
    passask()
#_________________________________________________________________________________________
def locked():
   window = Tk()
   window.minsize(500, 400)
   window.config(background='Green')
   window.title("Why Locked ?")
   
   label = Label(window, text="I will explain you why locked is better than snowad:", bg='white', font=("Courier", 10))
   time.sleep(2)
   
   label2 = Label(window, text="Press the button for more", bg='white', font=("Courier", 10))
   label2.place(y=200)
   
   label.pack()
   
   button = Button(window, text="More", command=window.destroy)
   button.place(x=55, y= 150)
   
   button.pack
   
   window.mainloop()
   whylocked()

#___________________________________________________________________________________________
def whylocked():
    print("ahahahahahahahaha")
    time.sleep(2)
    print("you real think i will say locked is better than my master")
    time.sleep(2)
    print("i hate him but i cant say locked is better")
    passask()
##__________________________________________________________________________
def Admin():
    print("starting...")
    time.sleep(2)
    print("Admin mod: on")
    time.sleep(1)
    print("Welcom snowad")
    time.sleep(1)
    
    edit = str(input("Do you want to edit the script ?"))
    
    
    if edit == ("yes"):
      print("Did you think that was easy")
      time.sleep(1)
      print("snowad made it, that cant be that easy.")
      time.sleep(2)
      passask()

    if edit == ("no"):
        time.sleep(1)
        print("cancel")
        time.sleep(2)
        passask()

##___________________________________________________________________________
def pythongore():
   print("starting...")
   time.sleep(2)
   print("PYTHONGOR.v.2.7 by snowad: ready, 印刷する")
   mode = str(input("Mode: Hypoténuse| Other side | Reciproque: "))

   if mode == "Hypoténuse":
      A = float(input("quelle est la longeur 1 ? "))
      B = float(input("quelle est la longeur 2 ? "))
      C = pow(A,2) + pow(B,2)
      C = sqrt(C)

      print("Calcul...")
      time.sleep(3)

      print("Dans le triangle A B C Rectangle en B. Selon le théorem de pythagor la longeur de l'Hypoténuse est de: ")
      print(C)

      time.sleep(0.5)
      print("PYTHONGOR:enjoy your awser. decrypte")
      pythongore()

   if mode == "Other side":
      A = float(input("quelle est la longeur 1 ? "))
      B = float(input("quelle est la longeur 2 ? "))
      C = float(pow(A,2) - pow(B,2))
      C = sqrt(C)

      print("Calcul...")
      time.sleep(3)

      print("Dans le triangle A B C Rectangle en B. Selon le théoreme de pythagor la longeur du côté  est de: ")
      print(C)

      time.sleep(0.5)
      print("PYTHONGOR:enjoy your awser. Passwords")
      pythongore()
   if mode == "Reciproque":
       A = float(input("longeur du premier côté "))
       B = float(input("longeur du deuxiéme côté "))
       C = float(input("longeur de l'hypoténuse"))
       Calcule1 = pow(C,2)
       Calcule2 = pow(A,2) + pow(B,2)
    
       print("Calcul...")
       time.sleep(3)
    
       if Calcule1 == Calcule2:
           print("Dans le triangle A B C. Selon la réciproque du théoreme de pythagor le Triangle ABC est rectangle ")
           time.sleep(0.5)
           print("PYTHONGOR:enjoy your awser. boomy")
           pythongore()
    
       if Calcule1 != Calcule2:
        
           print("Dans le triangle A B C. Selon la contraposé du théoreme de pythagor le Triangle ABC n'est pas rectangle  ")
           time.sleep(0.5)
           print("PYTHONGOR:enjoy your awser. See You")
           pythongore()
        
   if mode == "boomy":
      secretboom()
   
   if mode == "vault":
      vault()

   if mode == "Passwords":
       print("YvrPofdDB9r0mednY8xiNFSb2X12SyN0gazVbFRB8oaEfedRS2S3j02MwN131FuvZE23EnLRrA/id8PtvBXJrus6QyiDLIzPK3ICRM3ED8ZKsKiYCxrhC396Oe0LT5XTMFzNXhM+W6Ic4ZeDIwWebA==")
       pythongore()
    
   if mode == "decrypte":
       print("000000000000111100000000010111100000000001001111000000000100001000000000010100000000000001000100000000000011100100000000001111100000000000110010000000000001110000000000010101110000000001001110000000000010100100000000010010000000000001011111000000000001001100000000001111000000000000001001000000000010111100000000000111110000000001000000000000000010000000000000010000110000000000000111000000000010011000000000001110110000000000010000000000000010010000000000000001000000000000100101000000000011001100000000000010000000000000010101000000000001111000000000010110000000000000101101000000000001100100000000000110110000000000110111000000000001000100000000001000100000000000000101000000000010111000000000010001110000000001000110000000000101010100000000010110100000000000101000000000000000101000000000000011010000000001010100000000000010000100000000000010110000000000100011000000000001001000000000001010110000000001001101000000000011100000000000010001010000000000010100000000000001011000000000001100000000000000110001000000000101000100000000010110110000000001001001000000000010110000000000000000010000000000111010000000000100101000000000000110100000000000001100000000000101001000000000000000000000000000010111000000000100000100000000010101100000000001001011000000000101100100000000000110000000000001011100000000000101001100000000000001100000000001011101000000000010101000000000001001110000000000000010000000000011110100000000001111110000000000110110000000000011010100000000010011000000000000000011000000000011010000000000000011100000000000011101000000000001111000000000010101010000000001010101000000000000010100000000010001100000000000110101000000000011111100000000001111110000000000001010000000000000101000000000000010100000000001001011000000000010010100000000001100110000000000101000000000000001010100000000000110110000000000010000000000000001000100000000010010110000000000000100000000000010001000000000001101110000000000111111000000000010001000000000000100010000000000011011000000000101100000000000000100010000000000110011000000000000000000000000010101010000000000100010000000000010001000000000000110110000000001000110000000000011111100000000010101010000000000110011000000000000110100000000010101010000000000000000000000000011001100000000000100010000000000000100000000000100011100000000010101000000000000000101000000000101010100000000010110000000000000100010000000000001000100000000000000000000000000100101000000000011001100000000000001000000000001000111000000000101010000000000000001010000000001010101000000000101100000000000001000100000000000010001")
       pythongore()
   if mode == "print":
       print("http://www.csgnetwork.com/directbinaryencryption.html")
       pythongore()
#_________________________________________________________________________________________________________________________
def opennotepad():
    os.startfile("notepad.exe")

def opencmd():
    os.system("start cmd")

def calculatrice():
    os.system("calc")

def explorer():
    os.system("explorer")

def navigate():
    google = "https://www.google.fr"
    os.system("start " + google)



def multi_task():
    window = Tk()
    window.title("Multi Task Panel")
    window.maxsize(800,600)
    window.minsize(800,600)
    
    label = Label(window, text="Mluti task panel",bg = "black", fg = "white", font =(90))
    label.place(x=350, y=0)
    button = Button(window, height=5, width=20, text="Note pad", bg = "black", fg= "white", command = opennotepad)
    button.place(x=50, y =100)
    
    button = Button(window, height=5, width=20, text="Cmd", bg = "black", fg= "white", command = opencmd)
    button.place(x=330, y =100)
    
    button = Button(window, height=5, width=20, text="Calculator", bg = "black", fg= "white", command = calculatrice)
    button.place(x=600, y =100)
    
    button = Button(window, height=5, width=20, text="Explorer", bg = "black", fg= "white", command = explorer)
    button.place(x=50, y =250)
    
    button = Button(window, height=5, width=20, text="Navigate", bg = "black", fg= "white", command = navigate)
    button.place(x=330, y =250)
    

    window.mainloop()
#_____________________________________________________________________________________________________________
def pywarning():
    def close():
        window.destroy()
   
    window = Tk()
    window.maxsize(1000,990)
    window.minsize(1000,990)
    window.config(background='red')
    window.title("Py warning")
    
    label = Label(window, text='This is a very long puzzle game',bg='red',fg="white", font= ("Courier",(30)))
    label.pack()
    
    label = Label(window, text='make sure to have time to finish it',bg='red',fg="white", font= ("Courier",(30)))
    label.place(x=0, y=100)
    
    label.pack()
    label = Label(window, text='your goal is to find all password',bg='red',fg="white", font= ("Courier",(30)))
    
    label.place(x=0, y=200)
    label.pack()
    
    label = Label(window, text='look in the consol when you start',bg='red',fg="white", font= ("Courier",(30)))
    label.place(x=0, y=300)
    label.pack()
    
    button = Button(window, text="start the game", bg= "white", height=10, width=40, fg="black",command = pythongore)
    button.place(x=30, y =400)
     
    button = Button(window, text="exit", bg= "white", height=10, width=40, fg="black",command = close)
    button.place(x=700, y =400)
#_________________________________________________________________________________________________________________________

def bottledudes():
    bottledudes = "https://battledudes.io"
    webbrowser.open(bottledudes)

#_________________________________________________________________________________________________________________________
    
    
def TrollLuncher():
    window = Tk()
    window.maxsize(1000,800)
    window.minsize(1000,800)
    window.config(background='#a40000')
    window.title("Troll luncher")
    
    label = Label(window, text='TrollLuncher',bg='#a40000',fg="white", font= ("Courier", 60))
    label.place(x=230, y=200)
    
    label = Label(window, text="by snowad. 2025", bg='#a40000', fg="white",font= ("Courier", 10))
    label.place(x=0, y=0)
    button = Button(window, text="Life Controll", height=10, width=40, bg='white', font= ("Courier", 10), command = adminpanel)
    button.place(x=130, y=350)
    
    button = Button(window, text="Pythongore", height=10, width=40, bg='white', font= ("Courier", 10), command = pywarning)
    button.place(x=500, y=350)
   
    button = Button(window, text="Multi task panel (Windows only)", height=10, width=40, bg='white', font= ("Courier", 10), command = multi_task)
    button.place(x=130, y=550)
    
    button = Button(window, text="Bottle dudes.io", height=10, width=40, bg='white', font= ("Courier", 10), command = bottledudes)
    button.place(x=500, y=550)
    window.mainloop()
   
   
TrollLuncher()