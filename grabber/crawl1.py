from lxml.html import *
import re
#http://thenextweb.com/ - https://www.facebook.com/thenextweb
url = "http://thenextweb.com/"


#parse the url
doc = parse(url).getroot()

#spit out the html

#make a regex to grab the facebook username
pattern = r'https://www.facebook.com/([a-zA-Z]*)"'
# matches = re.match(pattern, tostring(doc))
matches = re.search(pattern, tostring(doc))
print "Facebook Account - %s" % (matches.group(1))



#http://thenextweb.com/ - https://www.facebook.com/thenextweb
