import requests
from bs4 import BeautifulSoup

url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")
text = soup.find("div", attrs = {"class","win_result"}).get_text()

round = text.split("\n")[2]
win_num = text.split("\n")[7:13]
bonus = text.split("\n")[-4]
print(round + str(win_num) + "+보너스:" + str(bonus))

# web = open("websiteSample.txt","w", encoding="utf8")
# web.write(text)
# web.close()

#div class = "win_result"