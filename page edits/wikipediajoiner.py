# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:21:49 2016

@author: jaidka
"""

import os
import csv
 
path = 'C:/Users/jaidka/Documents/datasets/andrea wiki/wikipedia2/'
with open('C:/Users/jaidka/Documents/datasets/andrea wiki/edits_file.csv', 'a',) as csvfile:
    writer = csv.writer(csvfile,delimiter=';',quoting=csv.QUOTE_MINIMAL)
    files = 0
    writer.writerow(["id","topic","rev_id","timestamp","parent_rev_id","user_id","user_is_anon","user_comment","article_len","article_diff","is_minor"])
    for infile in os.listdir(path):
        files = files + 1
        print("current file is: " + infile)
        with open(path + infile) as sysomosfile:
            #No.	Source	Host	Link	Date(ET)	Time(ET)	time(GMT)	Category	AuthorId	AuthorName	AuthorUrl	Auth	Followers	Following	Age	Gender	Language	Country	Province	City	Location	Sentiment	Title	Snippet	Description	Tags	Contents	View	Comments	Rating	Favourites	Duration	Bio	UniqueId

            fields = ["id","topic","rev_id","timestamp","parent_rev_id","user_id","user_is_anon","user_comment","article_len","article_diff","is_minor"]
            reader = csv.DictReader(sysomosfile,fieldnames=fields)
            rows = 0
            for row in reader:
                rows = rows+1     
                #if(rows<9):
                #print(line)
                #    continue
                #else:
                try:
                         print(files,":",rows)
                         #if(len(row["Host"])>0):
#                         print("Parsing:",row["AuthorId"],row["AuthorUrl"],row["time(GMT)"],row["Followers"],row["Following"],row["Age"],row["Gender"],row["Contents"],row["Language"],row["Bio"],row["Sentiment"],row["UniqueId"])
                         writer.writerow([row["id"],row["topic"],row["rev_id"],row["timestamp"],row["parent_rev_id"],row["user_id"],row["user_is_anon"],row["user_comment"],row["article_len"],row["article_diff"],row["is_minor"]])
                except:
                         print("Error:")#,row["AuthorId"],row["AuthorUrl"],row["time(GMT)"],row["Followers"],row["Following"],row["Age"],row["Gender"],row["Contents"],row["Bio"],row["Sentiment"],row["UniqueId"])
                         pass