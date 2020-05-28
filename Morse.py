from tkinter import *
import tkinter as tk
import tkinter.font
import time
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led = LED(14)
convert = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--",":":"---...","?":"..--..","'":".----.","-":"-....-","/":"-..-.","(":"-.--.-",")":"-.--.-","\"":".-..-.","@":".--.-.","=":"-...-","[":"-.--.-","]":"-.--.-","$":"...-..-","+":".-.-.",";":"-.-.-.","_":"..--.-","!":"---."}

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight ='bold')

def dot():
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.25)

def dash():
    led.on()
    time.sleep(0.75)
    led.off()
    time.sleep(0.25)

def space():
    time.sleep(1.5)
def charEnd():
    time.sleep(0.5)
def encrypt():
    text = textBox.get(1.0, tk.END+"-1c").lower()
    if (len(text) < 12):
        for letter in text:
            if letter == " ":
                space()
            elif letter in convert:
                morseconvert = convert[letter]
                for symbol in morseconvert:
                    if symbol == ".":
                        dot()
                    elif symbol =="-":
                        dash()
                charEnd()
            else:
                print("Character not supported")
    else:
        print("Enter name less than 12 character")


enter = Button(win, text = 'Encrypt', font = myFont, command = encrypt, bg = 'bisque2', height = 1, width = 15)
enter.grid(row =1, column = 2)



textBox = Text(win, height=1, width=40)
textBox.grid(row =1,column = 1)