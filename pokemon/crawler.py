import bs4
import requests
from random import seed
from random import randint
import cv

url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/icons/pokemon/regular/'

file = open('list.txt')
count = 0
db = {}
for x in file: 
    db[count] = x.strip()
    count+=1

random = randint(0,720)
buffer = db[random]
buffer+='.png'
print("Retrieving",buffer)

link = url+buffer
lol = requests.get(link)
open(buffer, "wb").write(lol.content)

img = cv.imread('/home/cloud/POKE-905/pokemon/sigilyph.png', 1)
print(img)

'''
import bs4
import requests
from random import seed

url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/icons/pokemon/regular/'

file = open('list.txt')
count = 0
db = {}
for x in file: 
    db[count] = x.strip()
    count+=1
print(db)

random = randint(0,720)

file = open('list.txt')
count = 0
for i in file:
    mon = str(i).strip()
    print("Retrieving ", mon)
    mon+='.png'

    buffer = str(count)
    buffer += '.png'
    link = url+mon
    lol = requests.get(link)
    open(buffer, "wb").write(lol.content)
    count+=1
'''