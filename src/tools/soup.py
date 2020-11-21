from bs4 import BeautifulSoup
import requests
import re
import pprint

class soup:
	def __init__(self, debug=False):
		if debug:
			print("[soup.py] debug=True")

	def getContent(self, url):
		raw = requests.get(url)
		html = BeautifulSoup(raw.text, 'html.parser')
		
		content = html.find("td", {"class": "leftblock"})
		return content.text

	def getArticle(self, url):
		raw = requests.get(url)
		html = BeautifulSoup(raw.text, 'html.parser')
		data = []
		
		title = html.findAll("td", {"class": "title"})
		date = html.findAll("td", text=re.compile("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"))
		url = ["http://news.fcu.edu.tw/wSite/"+i.findChildren("a", recursive=False)[0]["href"] for i in title]
		
		for i in range(45):
			data.append({
				"title": title[i].text,
				"date": date[i].text,
				"url": url[i],
			})
		return data
