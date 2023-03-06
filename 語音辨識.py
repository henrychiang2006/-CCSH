import pyttsx3

engine = pyttsx3.init()

# 設置要說的文字
text = '멈춘 시간 속 잠든 너를 찾아가
아무리 막아도 결국 너의 곁인 걸
길고 긴 여행을 끝내 이젠 돌아가
너라는 집으로 지금 다시 way back home
아무리 힘껏 닫아도 다시 열린 서랍 같아
하늘로 높이 날린 넌 자꾸 내게 되돌아와
힘들게 삼킨 이별도 다 그대로인 걸 oh oh oh (oh oh oh)
수없이 떠난 길 위에서 난 너를 발견하고
비우려 했던 맘은 또 이렇게 너로 차올라
발걸음의 끝에 늘 네가 부딪혀
그만, 그만
멈춘 시간 속 잠든 너를 찾아가
아무리 막아도 결국 너의 곁인 걸
길고 긴 여행을 끝내 이젠 돌아가
너라는 집으로 지금 다시 way back home
조용히 잠든 방을 열어 기억을 꺼내 들어
부서진 시간 위에서 선명히 너는 떠올라
길 잃은 맘 속에 널 가둔 채 살아
그만, 그만
멈춘 시간 속 잠든 너를 찾아가
아무리 막아도 결국 너의 곁인 걸
길고 긴 여행을 끝내 이젠 돌아가
너라는 집으로 지금 다시 way back home
세상을 뒤집어 찾으려 해
오직 너로 완결된 이야기를
모든 걸 잃어도 난 너 하나면 돼
빛이 다 꺼진 여기 나를 안아줘
눈을 감으면 소리 없이 밀려와
이 마음 그 위로 넌 또 한 겹 쌓여가
내겐 그 누구도 아닌 네가 필요해
돌아와 내 곁에 그날까지 I'm not done
'

# 使用引擎將文字轉換為語音
engine.say(text)

# 撥放語音
#engine.runAndWait()

import pyttsx3

engine = pyttsx3.init()

# 設置語音參數
engine.setProperty('rate', 300)  # 設置語速為 150 詞每分鐘
engine.setProperty('volume', 300)  # 設置音量為 0.8
voices = engine.getProperty('voices')  # 獲取可用聲音列表
engine.setProperty('voice', voices[1].id)  # 選擇第二個聲音

# 設置要說的文字


# 使用引擎將文字轉換為語音
engine.say(text)

# 撥放語音
engine.runAndWait()