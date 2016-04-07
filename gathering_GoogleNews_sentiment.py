from pattern.web import *
g = Google()
raw_results_list = []
for result in g.search('Chipotle news'):
	#print result.url
	raw_results_list.append(plaintext(result.text).encode('utf-8'))
stripped_results_list = []
for result in raw_results_list:
	result = result.strip('...')
	stripped_results_list.append(result.replace('\n', ' '))
print stripped_results_list

