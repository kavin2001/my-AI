# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import pyttsx3
# import openai
# import speech_recognition as sr


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# openai.api_key= "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"

# def transcribe_audio():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = recognizer.listen(source)
#     return recognizer.recognize_google(audio)
# model_engine = "text-davinci-002"
# prompt = transcribe_audio()
# prompt = "what is my name"

# completion = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# message = completion.choices[0].txt
# print(message)
# if __name__=="__main__":
    # speak('i am your friend and i can help you any time you want')

# import webbrowser

# url = 'F:\kd\my-friend\project\index.html'
# webbrowser.open_new_tab(url)

import webbrowser
import time
webbrowser.open("F:\kd\my-friend\project\index.html")
time.sleep(2)