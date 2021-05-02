import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request
from bs4 import BeautifulSoup
import re
#Importing dependencies




# this fuction takes in the Url of the book and scraped title,description,awards and genre as a dictionary.
def get_data(url):
    with urllib.request.urlopen(url) as f:
        data = f.read().decode('utf-8')
    d = BeautifulSoup(data)
    try:
        title=d.find(id="bookTitle",itemprop="name").text.replace('\n',"").replace(" ","")
        #get title data
    except:
        title='no title provided'
    try:
        description=d.find("div", id="description").text.split("\n")[2]
        #get description data
    except:
        description="No description provided ."
    genre=[]
    for div in d.findAll('a', {'class': 'actionLinkLite bookPageGenreLink'}):
        genre.append(div.text)
    details=d.find("div", id="details").text
    try:
        awards_uncl=re.findall(r'\(.*?\)', details.split('Literary Awards')[1]) #Getting the list of awards
        for items in awards_uncl:
            if len(items) != 6:
                awards_uncl.remove(items)
        awards=len(awards_uncl) #Getting the list of awards
    except Exception as e:
        print(e)
        awards=0
    context={
        'title':title,
        'description':description,
        'awards':awards,
        'genre':genre
    }
    return context
