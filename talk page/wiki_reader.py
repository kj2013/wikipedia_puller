#############
#Created by Andrea Ceolin - May 2018
#############


from collections import defaultdict
import os


#extract all the folders of the corpus in a folder named 'wikimedia'
directories= os.listdir('wikimedia')



#create a .tsv file that contains only the lines we are interested in
with open('filtered_wiki.tsv', 'w', encoding='utf-8') as output:
    for directory in directories:
        print(directory)
        for file in os.listdir('wikimedia/' + directory):
            d = defaultdict(list)
            for line in open('wikimedia/' + directory + '/' + file, encoding='utf-8'):
                row = line.split('\t')
                #If data is not annotated, skip
                if len(row)>7:
                    #0 the comment id
                    #1 the comment
                    #2 the raw comment,
                    #3 the timestamp
                    #4 the page id
                    #5 the page name
                    #6 the user id
                    #7 user name
                    #Format is: dictionary(page:[(time, user, topic, comment), (time, user, topic, comment)....])
                    comment = row[1].replace('"', ' ')
                    comment = comment.replace('NEWLINE', ' ')
                    d[row[5]].append((row[3], row[7], row[5], comment))
            for key in d:
                #skip if less than three posts, since we are interested in A-B-A interactions
                if len(d[key]) > 2:
                    #sort list by time of the post
                    sorted_t = sorted(d[key])
                    #retrieve instances in which the author of the first and the third post is the same
                    if sorted_t[0][1] == sorted_t[2][1] and sorted_t[0][1] != sorted_t[1][1]:
                        #write first post, second post, third post
                        output.write('\t'.join(sorted_t[0]))
                        output.write('\n')
                        output.write('\t'.join(sorted_t[1]))
                        output.write('\n')
                        output.write('\t'.join(sorted_t[2]))
                        output.write('\n')
