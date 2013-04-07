
#coding=utf-8
import os

files=os.listdir(os.getcwd())
#print files

htmlfiles= filter(lambda f:os.path.splitext(f)[1]=='.html',files)

print htmlfiles
#htmlfiles.sort()

for hf in htmlfiles:
  print hf.__class__

import HTMLParser
txtfile=open('text.txt','w')
class MyHTMLParser(HTMLParser.HTMLParser):
    towrite=False
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        if tag=='br':
          txtfile.write('\n')
        for attr in attrs:
            print "     attr:", attr
            if attr==('id','content'):
              self.towrite=True
    def handle_endtag(self, tag):
        print "End tag  :", tag
        if tag=='html':
          txtfile.close()
        
    def handle_data(self, data):
        print "Data     :", self.get_starttag_text()
        if self.get_starttag_text()=='<span id="PagePosition1_lab_Current">':
          txtfile.write(data)
        if self.get_starttag_text()=='<div id="content" style="font-size: 14px;">':
          txtfile.write(data)
        if self.get_starttag_text()=='<br>':
          txtfile.write('\n  '+data)
        if self.get_starttag_text()=='<title>':
         # txtfile=open(unicode(data+'.txt',utf8),'w')
          print '----------------------------'+data
    def handle_comment(self, data):
        print "Comment  :", data
 
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c
    def handle_decl(self, data):
        print "Decl     :", data
        

#import codecs

g=MyHTMLParser()
fff=open('1062438.html','r')
hh=fff.read()
fff.close()
print type(hh)
#g.feed(hh)
