# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:56:31 2019

@author: Saksham
"""

from html.parser import HTMLParser

class MyHTMLPraser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        if(attrs):
            for i in attrs:
                if not None in i:
                    print('-> ' + ' > '.join(i))
                else:
                    print('-> ' + i[0] + ' > None')
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if(attrs):
            for i in attrs:
                if not None in i:
                    print('-> ' + ' > '.join(i))
                else:
                    print('-> ' + i[0] + ' > None')
praser=MyHTMLPraser()
res=""
for i in range(int(input())):
    res=res+ " " + input()
praser.feed(res)