# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:55:54 2018

@author: simha
"""

from bs4 import BeautifulSoup as soup
import requests,re,json

class LinkFinder():
    def __init__(self,base_url):
        self.base_url = base_url
        #self.page_url = page_url
        self.links = set()
         
       
        
    def handle_links(self):
        r = requests.get(self.base_url)
        content = r.content
        #print r
        if content!=0:
            try:
                #news_open = urllib.urlopen(r).read()
                news_soup = soup(content, "html.parser")
                #all_tags = [tag.name for tag in news_soup.find_all()]
                a_tags = news_soup.find_all('div',{'class':'article-links-wrapper list-view'})
                for text in a_tags:
                    download = text.find_all('a', href = re.compile("^https://"))
                    for text in download:
                        hrefText = (text['href'])
                        self.links.add(hrefText)
                
            except:
                print('message: No content found')
                
    
                
    def page_links(self):
        return self.links
    
    def error(self,message):
        pass
    
    

