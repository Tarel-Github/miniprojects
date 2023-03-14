# pip install pyttsx3
import pyttsx3

tts = pyttsx3.init()
tts.say('안녕하세요~!!') # 저장같은거 필요없고 바로 실행
voice = tts.getProperty('voice')
tts.runAndWait()

