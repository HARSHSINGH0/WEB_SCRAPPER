from bs4 import BeautifulSoup
import requests
search=(input("Search for:"))
params={"?&q=":search}
r=requests.get("http://www.google.com/search",params=params)
soup=BeautifulSoup(r.text,"html.parser")
results=soup.find("ol",{"id":"srp"})
links=results.findALL("li",{"class":"csi"})

for item in links:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]

    if item_href and item_text:
        print(item_href)
        print(item_text)