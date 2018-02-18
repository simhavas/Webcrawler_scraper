# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 01:46:34 2018

@author: simha
"""

from bs4 import BeautifulSoup as soup
import requests,os
from urlparse import urlparse
from dateutil.parser import parse
import multiprocessing

# create directory to save all articles
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project '+ directory)
        os.makedirs(directory)
        
# Get domain name (exmple.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
    except:
        return ''

# Get sub domain name(name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
    

# To remove the links which are not annotated
def is_date(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False
    
    


  
def create_text_files_with_news(directory,url):
    
    create_project_dir(directory)
    
    #url = 'https://www.snopes.com/sandra-bullock-trump-clinton/'
    filename = url.split('/')[-2]
    r = requests.get(url)
    content = r.content
    proc_text = []
    news_para = []

    news_soup = soup(content, "html.parser")
    
    quote_tags = news_soup.find_all('blockquote')
    #a_tags = news_soup.find_all('div',{'class':'article-links-wrapper list-view'})
    for i in quote_tags:
        news_para.append(i.find_all('p'))
    for j in news_para:
        for m in j:
            proc_text.append(m.text.encode("ascii", 'ignore'))
            
    proc_text = " ".join(proc_text)
    
    f1 = open(directory+'/'+filename+'.txt','w+')
    f1.write("%s\n" %proc_text)
    f1.close()
    

if __name__ == '__main__':
    # get all links from the queue file in fakenews directory
    z = []
    f = open('fakenews/queue.txt','r')
    for i in f.readlines():
        z.append(i)
    f.close()
        
    z1 = []
    for i in z:
        temp = i.split('//'+get_domain_name(i)+'/')
        if is_date(temp[1][0:10]):
            z1.append(i)
    # remove links which are not annotated as fake        
    z = list(set(z).difference(set(z1)))
    for i in range(len(z)):
        p = multiprocessing.Process(target=create_text_files_with_news,args=('snopes_fakenews_articles',z[i]))
        p.start()
        p.join()
