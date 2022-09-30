import bs4
import requests

url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/'

list = open('list.txt')
buffer = ''
count = 0

for i in list: 
    buffer = str(count)
    buffer+='.png'
    url+=i
    lol = requests.get(url)
    open(buffer, "wb").write(lol.content)
    count+=1