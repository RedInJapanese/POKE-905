import bs4
import requests

url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/'

list = open('list.txt')
buffer = ''
count = 0
test = ''

for i in list: 
    buffer = str(count)
    buffer+='.png'
    url+=str(i)
    url+='.png'
    print(url)
    url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/'
    lol = requests.get(url)
    open(buffer, "wb").write(lol.content)
    count+=1