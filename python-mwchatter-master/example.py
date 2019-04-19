import os
import wikichatter as wc
import json
import csv
import re
#talk_samples_base = "./talk_samples/"
talk_samples_base="C:/Users/User/Dropbox/wikipedia_comments/talk_pages"
talk_files = []
talkingfile = open('C:/Users/User/Dropbox/wikipedia_comments/talk_pages.csv','w',newline='',encoding="utf-8")
talkingfilewriter = csv.writer(talkingfile)
for (name, directories, files) in os.walk(talk_samples_base):
    talk_files.extend([name + "/" + f for f in files])
count=0
for f_path in talk_files:
  #if(count==1):  
    with open(f_path, "r",encoding="utf-8") as f:
        count= count+1
        print(str(f_path))
        text = f.read()
        #print(text)
        parsed = wc.parse(text)
        #if (count==1):
        #print(parsed['sections'])
        print(count)
        for section in parsed['sections']:
            for comment in section['comments']:
               if 'author' in comment:
                #print(comment)
                    fullcomment = ' '.join(comment['text_blocks'])
                    fullcomment=fullcomment.split('[')[0].strip()
                    fullcomment=re.sub('<.*?>', '', fullcomment)
                    fullcomment=re.sub('{{.*?}}', '', fullcomment)
                    print(fullcomment)
#                    for block in comment['text_blocks']:
                  #  print(block)
                        #remove stuff in [[]]
                        #remove newlines
                    if (count>0):
                             talkingfilewriter.writerow([comment['author'], str(fullcomment),comment['time_stamp'],str(f_path), section['heading']])
                             count=count+1
                             print(count)
                             print(comment['author'], str(fullcomment),comment['time_stamp'],str(f_path), section['heading'])
                             #count = count+1
               else:
#                    print(comment)
                #print(comment)
                    fullcomment = ' '.join(comment['text_blocks'])
                    fullcomment=fullcomment.split('[')[0].strip()
                    fullcomment=re.sub('<.*?>', '', fullcomment)
                    fullcomment=re.sub('{{.*?}}', '', fullcomment)
                    print(fullcomment)
#                    for block in comment['text_blocks']:
                  #  print(block)
                        #remove stuff in [[]]
                        #remove newlines
                    if (count>0):
                             talkingfilewriter.writerow(["", str(fullcomment),"",str(f_path), ""])
                             count=count+1
                             print(count)
                             print("", str(fullcomment),"",str(f_path), "")
                             #count = count+1
talkingfile.close()
        #if(count==1):
        #    print(json.dumps(parsed))
        
