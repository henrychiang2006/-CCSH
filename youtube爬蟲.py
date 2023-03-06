import webbrowser 
import requests
r = requests.get('https://www.youtube.com/results?search_query=五月天')
#print(r.text) #列出文字
i=r.text.find("watch?",0)
j=r.text.find("\"",i+1)
print(r.text[i:j])
url = "https://www.youtube.com/"+r.text[i:j]
webbrowser.open(url)
