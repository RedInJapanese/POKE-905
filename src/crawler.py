from pkgutil import get_data
import sys
import bs4
import requests
from random import seed
from random import randint
from PIL import Image

url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/'

file = open('list.txt')
count = 0
db = {}
noise = [0, 32, 255, 82]
for x in file: 
    db[count] = x.strip().lower()
    count+=1

random = randint(0,720)
buffer = db[random]
print("Your key is: ", buffer)
buffer+='.png'

link = url+buffer
lol = requests.get(link)
open(buffer, "wb").write(lol.content)

img = Image.open(buffer, 'r')
l = list(img.getdata())
sys.stdout = open('rgb.txt','w')
for i in l: 
    for x in i: 
        if x not in noise:
            print(x)