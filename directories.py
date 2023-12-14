import requests
from termcolor import colored

#getting informations from user
target_url = input('[*] Enter Target URL: ')
file_name = input('[*] Enter Name Of The File Containing Directories: ')


def request(url):
	"""
	test if the following path exixts 

	Parameters:
	-----------
	url : the link of the route that contains website link (str)

	Versions:
	---------
	specification : Ahmed Adel BEREKSI REGUIG V1.0 (14/12/2023)
	implementation : Ahmed Adel BEREKSI REGUIG V1.0 (14/12/2023)
	"""

	#try if no error
	try:

		#return a response of the corresponding request
		return requests.get("http://" + url)
	
	#if an error occur then 
	except requests.exceptions.ConnectionError:

		#don't do anything
		pass


#read files of routes (also hidden routes)
file = open(file_name, 'r')
#for every route on this file
for line in file:

	#remove white spaces
	directory = line.strip()
	#build a colpete path 
	full_url = target_url + '/' + directory
	#search if this path exixts 
	response = request(full_url)
	#if the path exists
	if response:

		#print a message that we find this path 
		print(colored('[*] Discovered Directory At This Path: ' + full_url , 'green'))
