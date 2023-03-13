import requests
import os
#search_youtube函式:傳入關鍵字，回傳youtube搜尋到的第一個網址
def search_youtube(keyword):
  params={"search_query":keyword}
  res=requests.get("https://www.youtube.com/results",params)
  i=res.text.find('/watch?v=',0)
  j=res.text.find('"',i)
  vid=res.text[i:j]
  return vid
#連續語音辨識
import pyMicVoiceDetection as mic
import speech_recognition as sr

while True:
  #偵測音量，有聲段存至 1.wav
  mic.record(filename="1.wav",dur=25,TH=0.02,SilenceNum=50)
  r=sr.Recognizer()
  #由1.wav 讀出待辨識 audio
  with sr.WavFile("1.wav") as source:
    audio=r.record(source)

  try:
    #取得google語音有中文辨識結果
    result=r.recognize_google(audio,language='zh-TW')
    vid='https://www.youtube.com/'+search_youtube(result)
    
    os.system(f"start {vid}")    
    
  except Exception as e:
    pass
