import speech_recognition as sr
import webbrowser

recognitor1 = sr.Recognizer()
def search():
    while True:
        with sr.Microphone() as source:
            print("Skajite chto nibud")
            audio = recognitor1.listen(source)
            try:
                print("Recognition..")
                searching = recognitor1.recognize_google(audio, language='ru-RU')
                print(f"vi skazali: {searching}")
                search_url =  f"https://www.yandex.kz/search?text={searching}"
                webbrowser.open (search_url)
            except sr.UnknownValueError:
                print("Error")
            
search()