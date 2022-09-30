import bs4
import requests

url = 'https://github.com/msikma/pokesprite/blob/master/icons/pokemon/regular/abomasnow-mega.png'
lol = requests.get(url)
open('lol.png', "wb").write(lol.content)