# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:38:34 2018

@author: jaidka
"""

#https://en.wikipedia.org/wiki/Category:Politics_of_the_United_States


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
with open('C:/Users/User/Dropbox/wikipedia_comments/page_content/congressmembers_pages.txt',encoding="utf-8") as wikipedia_pols:
    reader = csv.reader(wikipedia_pols)
    count = 0
    revsfile = open('C:/Users/User/Dropbox/wikipedia_comments/page_content/pol_revisions.csv','a',newline='',encoding="utf-8")
    f_revs = csv.writer(revsfile)
   # f_revs.writerow(["id","topic","rev_id","timestamp","parent_rev_id","user_id","user_is_anon","user_comment","article_len","article_diff","is_minor"])
    for row in reader:
#        count = count + 1
#        if(count<5):
            try:
                topic=row[0]
                start_date = "2017-01-01T00:00:00Z"
                end_date = "2018-04-01T00:00:00Z"
                print(topic, start_date,end_date)
                site = pywikibot.Site("en", "wikipedia")
                page = pywikibot.Page(site, topic)
                #revs = list(page.loadrevisions())
                revs = list(page.revisions(starttime=end_date,endtime=start_date,content=True))
#                revs = page.revisions(starttime=end_date,endtime=start_date,content=False)#reverse=False, total=None, content=False, rollback=False, starttime=end_date,endtime=start_date)
                prevrevlength = 0
                for rev in revs:
 #                   print(rev)
                    textlength = len(str(rev['text']))
                    textlengthdiff = textlength-prevrevlength
                    prevrevlength=textlength
                    f_revs.writerow([count,str(topic),str(rev['revid']),str(rev['timestamp']),str(rev['_parent_id']),str(rev['user']),str(rev['anon']),str(rev['comment']),textlength,textlengthdiff,str(rev['minor'])])
              #for talk pages: https://stackoverflow.com/questions/54527376/how-to-get-the-content-in-talk-pages-of-wikipedia-in-python
                talkpage = page.toggleTalkPage()
                talkfile = open('C:/Users/User/Dropbox/wikipedia_comments/talk_pages/'+topic+'.txt','w',newline='',encoding="utf-8")
                text = talkpage.get()
                #print(count, str(ob['text']))
                talkfile.write(text)
                talkfile.close()
#                print(text)
            except:
                pass
    revsfile.close()
 