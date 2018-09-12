# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:48:49 2018

@author: jaidka
"""
#https://www.mediawiki.org/wiki/Manual:Revision_table
import requests
import urllib2
import re

def get_wikipedia_basic_info(titles):      
    atts = {'prop': 'revisions', 'action': 'query', 'format': 'json',
      'rvprop': 'timestamp|user|size|tags|flags|comment|ids', 
      'titles': titles
    }
    resp = requests.get('http://en.wikipedia.org/w/api.php', params = atts)
    
    return resp.json()



#get_wikipedia_basic_info("Stanford")
#data = resp.json()
#print(data)

def GetRevisions(pageTitle):
    url = "https://en.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvlimit=500&titles=" + pageTitle
    revisions = []                                        #list of all accumulated revisions
    next = ''                                             #information for the next request
    while True:
        response = urllib2.urlopen(url + next).read()     #web request
        revisions += re.findall('<rev [^>]*>', response)  #adds all revisions from the current request to the list

        cont = re.search('<continue rvcontinue="([^"]+)"', response)
        if not cont:                                      #break the loop if 'continue' element missing
            break

        next = "&rvcontinue=" + cont.group(1)             #gets the revision Id from which to start the next request

    return revisions;


revisions = GetRevisions("Coffee")

print(len(revisions))
#10418