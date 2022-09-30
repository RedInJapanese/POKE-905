import bs4
import requests

url = 'https://raw.githubusercontent.com/msikma/pokesprite/master/icons/pokemon/regular/abomasnow-mega.png'
lol = requests.get(url)
open('lol.png', "wb").write(lol.content)