from Speak import speak
def remem(rememberMessage):
    remember = open("Remember.txt","a")
    remember.write(rememberMessage)
    speak("Remembered sir.")
    remember.close()


def remembered():
    remember = open("Remember.txt","r")
    speak("You told me to remember that" + remember.read())
