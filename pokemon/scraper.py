import bs4
import requests
from random import seed

url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/'

file = open('list.txt')


for i in file:
    mon = str(i).strip().lower()
    print("Retrieving ", mon)
    mon+='.png'
    link = url+mon
    lol = requests.get(link)
    open(mon, "wb").write(lol.content)