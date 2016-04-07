from pattern.web import *
g = Google()
for result in g.search('Chipotle news'):
	#print result.url
	print plaintext(result.text).encode('utf-8')