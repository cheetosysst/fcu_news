from tools.soup import soup
import requests as req
from pprint import pprint

soup = soup()
url = "http://news.fcu.edu.tw/wSite/lp?ctNode=14980&mp=9000&nowPage=1&pagesize=45"

# soup.getHTML()
pprint(soup.getArticle(url))
# s = soup.getArticle(url)