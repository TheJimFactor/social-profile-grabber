from lxml.html import *
import re
import sqlite3
#http://thenextweb.com/ - https://www.facebook.com/thenextweb
url = "http://thenextweb.com/"
url = "http://bestoftheweb.com/"

url = "http://moz.com/"
url = "http://thenextweb.com/"
#parse the url
doc = parse(url).getroot()

# create sqlite connection
conn = sqlite3.connect('social.db')
c = conn.cursor()

#check if table existing, if it does not create it
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'social_accounts\'')
if c.fetchone():
	print 'Using the existing database'
else:
	print "First run, creating table"
	c.execute('''CREATE TABLE social_accounts
		(social_site text, account_name text)''')

# social site and its account name regular expression
patterns = {
	'Facebook':r'https?://www.facebook.com/([a-zA-Z]+)/?',
	'Twitter':r'https?://twitter.com/([a-zA-Z]+)/?"',
	'Google Plus':r'https?://plus.google.com/\+?([a-zA-Z]+|[0-9]+)/?',
	'Flickr':r'https?://www.flickr.com/photos/([a-zA-Z]+)/?',
	'Pinterest':r'https?://pinterest.com/([a-zA-Z]+)/?',
	'Tumblr':r'https?://([a-zA-Z]+).tumblr.com/?',
	'LinkedIn':r'https?://www.linkedin.com/company/([a-zA-Z-]+)/?',
	'Feed Burner':r'https?://feeds2.feedburner.com/([a-zA-Z]+)/?',
	}

# matchestest = re.search(patterns['Google Plus'], tostring(doc))
# print "%s Account - %s" % ('Google Plus', matchestest)
# print "%s Account - %s" % ('Google Plus', matchestest.group(1))

for social_site in patterns:
	matches = re.search(patterns[social_site], tostring(doc))
	try:
		print "%s Account - %s" % (social_site, matches.group(1))
		# store into database
		c.execute("INSERT INTO social_accounts VALUES ('%s', '%s')" % (social_site, matches.group(1)))
		conn.commit()
	except (AttributeError):
		print "No %s Account Found" % (social_site)

conn.close()
