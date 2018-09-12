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
with open('C:/Users/jaidka/Documents/datasets/andrea wiki/wikipedia_timestamps.csv') as wikipedia_ts:
    reader = csv.reader(wikipedia_ts)
    count = 0
    stringfile = 'C:/Users/jaidka/Documents/datasets/andrea wiki/aug 28/page_categories.csv'
    f = csv.writer(open(stringfile, "w",newline=''))
    f.writerow(["id","page","category"])
    stringfile2 = 'C:/Users/jaidka/Documents/datasets/andrea wiki/aug 28/page_contribs.csv'
    f2 = csv.writer(open(stringfile2, "w",newline=''))
    f2.writerow(["id","page","number_contributors"])
    for row in reader:
            count = count + 1
#        if(count<10):
            try:
                topic=row[0]
                start_date = row[10]
                end_date = row[11]
                topic2 = topic.split("/")[0]
                print(topic, start_date,end_date)
                site = pywikibot.Site("en", "wikipedia")
                page = pywikibot.Page(site, topic2)
                #revs = list(page.loadrevisions())
                cats = page.categories()
                contribs = page.contributors(starttime=end_date,endtime=start_date)
#                revs = page.revisions(starttime=end_date,endtime=start_date,content=False)#reverse=False, total=None, content=False, rollback=False, starttime=end_date,endtime=start_date)
                prevrevlength = 0
#                print(cats)
#                print(contribs)
                for cat in cats:
                    #print(cat)
                    cat = str(cat).replace("[[en:Category:","")
                    cat = cat.replace("]]","")
                    #print(cat)
                    f.writerow([count,topic,str(cat)])
                f2.writerow([count,topic,str(len(contribs))])
#                    textlength = len(str(rev['text']))
#                    textlengthdiff = textlength-prevrevlength
#                    prevrevlength=textlength
#                    f.writerow([count,topic,str(rev['revid']),str(rev['timestamp']),str(rev['_parent_id']),str(rev['user']),str(rev['anon']),str(rev['comment']),textlength,textlengthdiff,str(rev['minor'])])
#                f.close()
            except:
                pass