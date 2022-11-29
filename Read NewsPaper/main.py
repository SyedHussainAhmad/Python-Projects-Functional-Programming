import requests
import time
import json
from win32com.client import Dispatch

def speak(str):
    readData = Dispatch('SAPI.Spvoice')
    readData.Speak(str)

if __name__ == "__main__":

    data = requests.get ("https://newsdata.io/api/1/news?apikey=pub_1071061999ed7304acb0b43bf70dbb0c1c335&q=Technology&language=en ")

    speak('Kaise ho Hussain Bhai')