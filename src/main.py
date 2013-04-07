#coding=utf-8
'''
put it in the floder of html files,and run it,it will change them into txt files
'''
import os

files=os.listdir(os.getcwd())
#print files

htmlfiles= filter(lambda f:os.path.splitext(f)[1]=='.html',files)

print htmlfiles
#htmlfiles.sort()



import HTMLParser
#txtfile=open('text.txt','w')
class MyHTMLParser(HTMLParser.HTMLParser):
    titled=False

    def handle_starttag(self, tag, attrs):
        if tag=='br':
          self.txtfile.write('\n')

    def handle_endtag(self, tag):
        if tag=='html':
          self.txtfile.close()
        if tag=='title':
            self.titled=True
    def handle_data(self, data):
       # print "Data     :", self.get_starttag_text()
        if self.get_starttag_text()=='<span id="PagePosition1_lab_Current">':
          self.txtfile.write(data)
        if str(self.get_starttag_text()).find('content'):
          self.txtfile.write(data)
        if self.get_starttag_text()=='<br>':
          self.txtfile.write('\n\t'+data)
        if self.get_starttag_text()=='<title>' and not self.titled:
          print '----------------------------'+data+'****'
          print type(data)
          self.txtfile=open(data.decode('utf8')+'.txt','w')
"""
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
        
"""

for hf in htmlfiles:
    print '-----------'+hf.decode('gb2312')
    g=MyHTMLParser()
    fff=open(hf.decode('gb2312'),'r')
    hh=fff.read()
    fff.close()
    #print hh
    g.feed(hh)
