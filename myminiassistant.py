import pyttsx3
import datetime
import webbrowser
import os
import json
import requests
import calendar
import speech_recognition as sr
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#you can change voice of female to male here
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
        print("recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        speak("sorry , i  couldn't hear you can you please say again")
        return "None"
    return query
def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("  Good Morning!")
    elif hour>=12 and hour<18:
        speak("  Good Afternoon!")
    else:
        speak("   Good Evening!")
def news():
    # url = "enter your api key"
    #enter api for news
    data = requests.get(url).text
    news = json.loads(data)
    p = news["articles"]
    for i in p:
        print(i["title"])
        speak(i["title"])
def today():
    p = datetime.datetime.now()
    r = p.strftime("%d-%m-%y")
    d, m, y = p.strftime("%d-%m-%y").split("-")
    p = calendar.day_name[calendar.weekday(int(y), int(m), int(d))]
    q = p.upper()
    print(f"DATE:-{r} , DAY:-{q}")
    speak(f"today is {q}")
def weather():
    print("Enter city name")
    inp = input().lower()
    city = inp.capitalize()
    # key = "enter your key"
    #enter api key for weather
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    data = requests.get(url).text
    weather = json.loads(data)
    w = weather['main']
    print("TEMPRATURE:-", "{:.2f}".format((w['temp'] - 273.15)), "Celcius")
    print("HUMIDITY:-", w['humidity'], "%")
    print("PRESSURE:-", w['pressure'], "hPa")
    s = weather['wind']
    print("SPEED OF WIND:-", s['speed'], "Km/h")
    print(20*"_")
def game():
    speak("please enter your name")
    print("please enter your name\n")
    name = input()
    speak(f"WELCOME {name} TO THE SNAKE,WATER,GUN GAME")
    i=1
    c=0
    u=0
    t=0
    speak("RULE is you have to press w for water, g for gun and s for snake")

    while(i<11):
        import random
        list = ["s", "g", "w"]
        v = random.choice(list)
        speak(f"Attempt number {i}")
        print(f"Attempt number {i}")
        j=takecommand().lower()
        if(j=="snake" and v=="w"):
            print("I choose",v)
            print("You won in this attempt")
            speak("You won this attempt")
            u=u+1
        if (j =="snake" and v =="s"):
            print("I choose", v)
            print("Tie in this attempt")
            speak("game Tied in this attempt")
            t=t+1
        if (j =="snake" and v =="g"):
            print("I choose", v)
            print("I won in this attempt")
            speak("I won this attempt")
            c = c + 1
        if (j=="water" and v =="g"):
            print("I choose", v)
            print("You won in this attempt")
            speak("You won this attempt")
            u = u + 1
        if (j=="water" and v=="w"):
            print("I choose", v)
            print("game Tied in this attempt")
            speak("Tied")
            t = t + 1
        if (j=="water" and v =="s"):
            print("I choose", v)
            print("I won in this attempt")
            speak("I won this attempt")
            c = c + 1
        if (j=="gun" and v=="s"):
            print("I choose", v)
            print("You won in this attempt")
            speak("You won this attempt")
            u = u + 1
        if (j=="gun" and v=="g"):
            print("I choose", v)
            print("Tie in this attempt")
            speak("game Tied in this attempt")
            t = t + 1
        if (j=="gun" and v=="w"):
            print("I choose", v)
            print("I won in this attempt")
            speak("I won this attempt")
            c = c + 1
        i=i+1
        print(75*"-")
    print("I won ",c,"attempt,you won ",u,"attempt and game tied",t, "times")
    speak(f"I won {c} attempt,you won {u} attempt and game tied {t} times")
    print(70*"*",end="\n")
    if(u<c):
        print("FINALLY I WON")
        speak(" computer won")
    elif(u>c):
        print("FINALLY YOU WON")
        speak(f"congratulation {name} you won this game")
    elif(u==c):
        print("EQUALLY WINNER :)")
        speak("both of us won ")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('username', 'password')
    server.sendmail('username', to, content)
    server.close()


if __name__ == "__main__":

    speak("  hello sir")
    greetings()
    speak("  i am your mini assistant")
    speak("   Please tell me how may I help you")
    while True:
        command = takecommand().lower()

        if 'youtube' in command:
            webbrowser.open("youtube.com")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'google' in command:
            webbrowser.open("google.com")
        elif 'music' in command:
            music_dir = 'D:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in command:
            nowtimeis = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {nowtimeis}")
            print(f"the time is {nowtimeis}")
        elif 'day' in command:
            today()
        elif 'weather' in command:
            weather()
        elif 'news' in command:
            speak("headlines are!")
            news()
        elif 'game' in command:
            game()
        elif 'send email' in command:
            try:
                print("whom are you sending mail")
                to =input()
                speak("What should I say?")
                content = takecommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry , I am not able to send this email")
