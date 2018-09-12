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
with open('C:/Users/jaidka/Downloads/wikipedia_timestamps.csv') as wikipedia_ts:
    reader = csv.reader(wikipedia_ts)
    count = 0
    for row in reader:
            count = count + 1
#        if(count<10):
            try:
                topic=row[0]
                start_date = row[10]
                end_date = row[11]
                topic2 = topic.split("/")[0]
                stringfile = 'C:/Users/jaidka/Downloads/wikipedia_revisions/'+topic2+'.csv'
                f = csv.writer(open(stringfile, "w",newline=''))
                f.writerow(["id","topic","rev_id","timestamp","parent_rev_id","user_id","user_is_anon","user_comment","article_len","article_diff","is_minor"])
                print(topic, start_date,end_date)
                site = pywikibot.Site("en", "wikipedia")
                page = pywikibot.Page(site, topic2)
                #revs = list(page.loadrevisions())
                revs = list(page.revisions(starttime=end_date,endtime=start_date,content=True))
#                revs = page.revisions(starttime=end_date,endtime=start_date,content=False)#reverse=False, total=None, content=False, rollback=False, starttime=end_date,endtime=start_date)
                prevrevlength = 0
                for rev in revs:
                    #print(rev)
                    textlength = len(str(rev['text']))
                    textlengthdiff = textlength-prevrevlength
                    prevrevlength=textlength
                    f.writerow([count,topic,str(rev['revid']),str(rev['timestamp']),str(rev['_parent_id']),str(rev['user']),str(rev['anon']),str(rev['comment']),textlength,textlengthdiff,str(rev['minor'])])
                f.close()
            except:
                pass