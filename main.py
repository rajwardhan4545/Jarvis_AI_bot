import speech_recognition as sr
import os
import win32com.client
import webbrowser
from openai import OpenAI
import datetime
from config import apikey
# def chat(query):
chatStr =""
def chat(query):
    global chatStr
    client = OpenAI(api_key=apikey)
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    chatStr += f"jarvis : {response.choices[0].text}"
    say(response.choices[0].text)


def ai(prompt):
    client = OpenAI(api_key=apikey)
    text=f"OpenAI response for Prompt : {prompt} \n ****************************\n\n"
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(response.choices[0].text)
    text+=response.choices[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(prompt.split('write')[1:])}.txt","w") as f:
        f.write(text)
        f.write(response.choices[0].text)
def say(text):
    speaker = win32com.client.Dispatch("SAPI.Spvoice")
    s = text
    speaker.Speak(s)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
          print("Recognizing...")
          query = r.recognize_google(audio, language="en-in")
          print(f"Luci : {query}")
          return query
        except Exception as e:
            return "Some Error Occured Sorry"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello i am jarvis A I")
    while True :
        print("Listening...")
        query = takeCommand()
        sites =[["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])

        if "open music" in query:
            say("opening music sir")
            musicpath=r"C:\Users\Hp\Downloads\Why-this-kolaveri-di.mp3"
            os.startfile(musicpath)
        elif "the time" in query:
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strftime}")
        elif "jarvis write".lower() in query.lower():
            ai(prompt=query)
        else :
            chat(query)
        paths = [["telegram",r"C:\Users\Hp\Desktop\Telegram Desktop\Telegram.exe"],["vs code",r"C:\Microsoft VS Code\Code.exe"],["iris",r"C:\Users\Hp\Desktop\Dashboard   IRIS.lnk"]]
        for path in paths:
            if f"open {path[0]}".lower() in query.lower():
                say(f"Opening {path[0]} sir")
                os.startfile(path[1])

