# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 07:00:16 2018

@author: simha
"""

import multiprocessing

def spawn(num,num2):
    for i in range(len(num)):
        print(num[i]*num2[i])
    
if __name__ == '__main__':

    p = multiprocessing.Process(target=spawn,args=(range(10),range(1,11)))
    p.start()
    p.join()
        
        


#from multiprocessing import Pool
#
#def spawn(num):
#    return num*2
#    
#if __name__ == '__main__':
#    
#    p = Pool(processes=20)
#    data = p.map(spawn,range(20))
#    p.close()
#    print data