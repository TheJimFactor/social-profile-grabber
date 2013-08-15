from lxml.html import *
import re
#http://thenextweb.com/ - https://www.facebook.com/thenextweb
url = "http://thenextweb.com/"

#parse the url
doc = parse(url).getroot()

# social site and its account name regular expression
patterns = {
	'Facebook':r'https://www.facebook.com/([a-zA-Z]*)"',
	'Twitter':r'https://twitter.com/([a-zA-Z]*)"'
	}

for social_site in patterns:
	matches = re.search(patterns[social_site], tostring(doc))
	print "%s Account - %s" % (social_site, matches.group(1))

