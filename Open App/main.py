# importing the module
import subprocess
import speech_recognition as sr 
from AppOpener import run 
import webbrowser # --> To search across web.

def listen():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your command...")    
        query = r.recognize_google(audio)
        print(f"You said: {query}\n")

    except Exception as e:
        print("Please say again...")  
        return "None"

    return query

def appOpen(query):
    query = query.replace('open', '')
    query = query.replace(' ', '')

    if query in a:
        run(a)
    else:
        webbrowser.open(query)

if __name__ == '__main__':
    # traverse the software list
    Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(Data)

    query = listen().lower() # --> Take command and convert it into lower case string.


    if 'open' in query:
        appOpen(query)