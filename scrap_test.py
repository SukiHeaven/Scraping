import urllib
import bs4

url_ligue_1 = "https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020"
    
from urllib import request

request_text = request.urlopen(url_ligue_1).read()
print(request_text[:1000])