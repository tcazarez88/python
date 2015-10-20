import requests 


url = input("Input a ticker: ")


def openwebsite(url):
	request_data = requests.get("https://www.google.com/finance?q=" +url)
	print (request_data.text)



openwebsite(url)

