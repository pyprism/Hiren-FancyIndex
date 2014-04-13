__author__ = 'prism'
# Details info http://www.omdbapi.com/

import requests
from  yaml import load



#Seach all movies
def search(name):
    name = { 's' : name }
    return requests.get("http://www.omdbapi.com/", params = name)


# Just search movie title
def searchByTitle(title):
    name = { 't' : title }
    data = load(requests.get("http://www.omdbapi.com/", params = name).text)
    if not 'Error' in data:
        print "sd" #now extract dictionary
    else:
        print "ASaa"



#search title with year
def titleAndYear(title,year):
    name = { 't' : title , 'y' : year }
    return requests.get("http://www.omdbapi.com/", params = name)

print searchByTitle('Captain America: The Winter Soldier')