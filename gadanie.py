import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
for i in range(2):
    engine.say("Julia dlaczego nie robisz lekcji")
    engine.say("W dzienniku są zapisane zadania z matematyki i polskiego")
    engine.say("Pamiętaj w czwartek klasówka z angielskiego")
    engine.runAndWait()
    engine.stop()