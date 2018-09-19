# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:38:34 2018

@author: jaidka
"""
#Code that uses pywikibot to download the edit history for a set of wikipedia articles
#the default version and language needs to be set in the user-config file.
#Please use and modify as needed. Good Luck!

#SEE THIS ONE https://doc.wikimedia.org/pywikibot/master/api_ref/pywikibot.html#module-pywikibot.page
#import page https://www.mediawiki.org/wiki/API:Revisions
#see https://stackoverflow.com/questions/34411896/how-to-get-full-wikipedia-revision-history-list-from-some-article
#maybe see http://paws-public.wmflabs.org/paws-public/47938337/02%20-%20Intro%20to%20pywikibot.ipynb
import pywikibot
#this is important: https://www.mediawiki.org/wiki/Manual:Pywikibot/user-config.py
import csv

def clean(content):
    content = content.replace('\n','')
    content = content.replace('\t','')
    content = content.replace(',','')
    content = content.replace('\r','')
    return content

with open('C:/Users/jaidka/Documents/datasets/andrea wiki/wikipedia_timestamps.csv') as wikipedia_ts:
    stringfile = 'C:/Users/jaidka/Documents/datasets/andrea wiki/topics_revs_text.csv'
    f = csv.writer(open(stringfile, "w",newline=''))
    f.writerow(["id","topic","start_date","end_date","content"])
    reader = csv.reader(wikipedia_ts)
    count = 0
    for row in reader:
            count = count + 1
#        if(count<10):
            try:
                topic=row[0]
                start_date = row[1]
                end_date = row[2]
                topic2 = topic.split("/")[0]
                print(topic, start_date,end_date)
                site = pywikibot.Site("en", "wikipedia")
                page = pywikibot.Page(site, topic2)
                #revs = list(page.loadrevisions())
                revs = list(page.revisions(starttime=end_date,endtime=start_date,content=True))
#                revs = page.revisions(starttime=end_date,endtime=start_date,content=False)#reverse=False, total=None, content=False, rollback=False, starttime=end_date,endtime=start_date)
                text_of_page = clean(str(revs[0]['text']))
                f.writerow([count,topic,start_date,end_date,text_of_page])
            except:
                pass
    #f.close()