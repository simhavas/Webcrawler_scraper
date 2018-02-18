# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:52:41 2018

@author: simha
"""

from link_finder import LinkFinder
import re

PROJECT_NAME = 'fakenews'

start_link = "https://www.snopes.com/tag/fake-news/"



for j in range(29):
    x = []
    y = []
    finder = LinkFinder(start_link)
    finder.handle_links()
    x = [i for i in finder.page_links()]
    
    
    
    for i in x:
        if re.search(r"\page", i):
#            if j == 0:
#                temp = i
            
            y.append(i)
    print ('y :',y)
    x = list(set(x).difference(set(y)))
    
    if j == 0:
        
        f1 = open(PROJECT_NAME + '/crawled.txt','w+')
        f1.write("%s\n" %start_link)
        f1.close()
        
        
        f = open(PROJECT_NAME + '/queue.txt','w+')
        for line in x:
          f.write("%s\n" %line)    
        f.close()
        
    
    else:
        f1 = open(PROJECT_NAME + '/crawled.txt','a+')
        f1.write("%s\n" %start_link)
        f1.close()
        
        
        f = open(PROJECT_NAME + '/queue.txt','a+')
        for line in x:
          f.write("%s\n" %line)    
        f.close()
        
    if len(y)>1:
        if int(y[0].split('/')[-2]) < int(y[1].split('/')[-2]):
            start_link = y[1]
        else:
            start_link = y[0]
        print start_link
    else:
         start_link = y[0]            
         print start_link
    if j == 28:
        break

    
    
    
#finder = LinkFinder(start_link)
#finder.handle_links()
#x = [i for i in finder.page_links()]





