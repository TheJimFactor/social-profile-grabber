from lxml.html import *
import re
#http://thenextweb.com/ - https://www.facebook.com/thenextweb
url = "http://thenextweb.com/"

#parse the url
doc = parse(url).getroot()

# social site and its account name regular expression
patterns = {
	'Facebook':r'https://www.facebook.com/([a-zA-Z]+)"',
	'Twitter':r'https://twitter.com/([a-zA-Z]+)"',
	'Google Plus':r'https://plus.google.com/%s([a-zA-Z]+)/"' % re.escape('+')
	}

# matchestest = re.search(patterns['Google Plus'], tostring(doc))
# print "%s Account - %s" % ('Google Plus', matchestest)
# print "%s Account - %s" % ('Google Plus', matchestest.group(1))

for social_site in patterns:
	matches = re.search(patterns[social_site], tostring(doc))
	try:
		print "%s Account - %s" % (social_site, matches.group(1))
	except (AttributeError):
		print "No %s Account Found" % (social_site)
