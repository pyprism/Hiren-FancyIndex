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
    return requests.get("http://www.omdbapi.com/", params = name)


#search title with year
def titleAndYear(title,year):
    name = { 't' : title , 'y' : year }
    return requests.get("http://www.omdbapi.com/", params = name)