__author__ = 'prism'
import requests , json

param = {'s' : "True Grit"}
r = requests.get("http://www.omdbapi.com/", params = param)

print str(json.loads(r.text))