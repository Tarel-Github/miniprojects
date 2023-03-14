# TTS (Text To Speech)
# pip install gTTS
# pip install playsound
from gtts import gTTS
from playsound import playsound

text = '안녕하세요, 손민성입니다.'

tts = gTTS(text = text, lang = 'ko', slow = False) # 텍스트 입력
tts.save('./studyPython/output/hi.mp3')# 음성파일 저장
print('생성 완료!')
playsound('./studyPython/output/hi.mp3') # 저장된 음성파일을 재생
print('음성출력 완료!')
