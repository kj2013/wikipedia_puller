import os
import wikichatter as wc
import json
import csv
import re
def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for result in find(key, d):
                        yield result

#example = {'app_url': '', 'models': [{'perms': {'add': True, 'change': True, 'delete': True}, 'add_url': '/admin/cms/news/add/', 'admin_url': '/admin/cms/news/', 'name': ''}], 'has_module_perms': True, 'name': u'CMS'}

#print(list(find('admin_url', example)))

#talk_samples_base = "./talk_samples/"
talk_samples_base="C:/Users/User/Dropbox/wikipedia_comments/talk_pages"
talk_files = []
talkingfile = open('C:/Users/User/Dropbox/wikipedia_comments/talk_pages.csv','w',newline='',encoding="utf-8")
talkingfilewriter = csv.writer(talkingfile)
for (name, directories, files) in os.walk(talk_samples_base):
    talk_files.extend([name + "/" + f for f in files])
count=1
for f_path in talk_files:
    with open(f_path, "r",encoding="utf-8") as f:
    #  print(str(f_path))
        text = f.read()
    #    if(count==1):
        try:
            parsed = wc.parse(text)
            for section in parsed['sections']:
                #NESTED???
                for comment in section['comments']:
                    if 'author' in comment:
                #print(comment)
                        fullcomment = ' '.join(comment['text_blocks'])
                        fullcomment=fullcomment.split('[')[0].strip()
                        fullcomment=re.sub('<.*?>', '', fullcomment)
                        fullcomment=re.sub('{{.*?}}', '', fullcomment)
                        #print(fullcomment)
#                    for block in comment['text_blocks']:
                  #  print(block)
                        #remove stuff in [[]]
                        #remove newlines
                        if (len(str(fullcomment))>2):
                             talkingfilewriter.writerow([comment['author'], str(fullcomment),comment['time_stamp'],str(f_path)])
            for section in section['subsections']:
                print("nested")
                for comment in section['comments']:
                    if 'author' in comment:
                #print(comment)
                        fullcomment = ' '.join(comment['text_blocks'])
                        fullcomment=fullcomment.split('[')[0].strip()
                        fullcomment=re.sub('<.*?>', '', fullcomment)
                        fullcomment=re.sub('{{.*?}}', '', fullcomment)
                        #print(fullcomment)
#                    for block in comment['text_blocks']:
                  #  print(block)
                        #remove stuff in [[]]
                        #remove newlines
                        if (len(str(fullcomment))>2):
                             talkingfilewriter.writerow([comment['author'], str(fullcomment),comment['time_stamp'],str(f_path)])
                for section2 in section['subsections']:
                    print("nested2")            
        except:
                pass
    #  count=count+1
        #if(count==1):
        #    print(json.dumps(parsed))
        #count=count+1
