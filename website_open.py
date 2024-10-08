import pywhatkit
from Speak import speak
def website_opener(domain):
    pywhatkit.search(domain)
    speak("Its on Your Screen Sir..")
    
    