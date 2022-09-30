import bs4
import requests

url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/icons/pokemon/regular/'

file = open('list.txt')
count = 0
for i in file:
    mon = str(i).strip()
    print("Retrieving ", mon, "...")
    mon+='.png'
    link = url+mon
    lol = requests.get(url)
    open(mon, "wb").write(lol.content)