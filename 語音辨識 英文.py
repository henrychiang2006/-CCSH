import speech_recognition as sr

# 創建一個 Recognizer 物件
r = sr.Recognizer()

# 使用麥克風錄音
with sr.Microphone() as source:
    print("請開始說話...")
    audio = r.listen(source)

# 將音訊轉換成文字
try:
    text = r.recognize_google(audio)
    print("你說了：" + text)
except sr.UnknownValueError:
    print("無法辨識你所說的話")
except sr.RequestError as e:
    print("無法連接 Google 語音辨識服務；{0}".format(e))