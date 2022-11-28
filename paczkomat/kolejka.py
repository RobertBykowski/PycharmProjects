import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 180)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

line = random.randint(1, 10)
print(line)
list = [0,"first","second","third","fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh"]
word = list[line]
print(word)
engine.say("All of our agents are currently busy You are"+word+" in line")
engine.runAndWait()
engine.stop()


