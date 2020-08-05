import requests
import sys

url = sys.argv[1]
caption = input("Enter caption: ")
category = input("Enter category to select tags: ")
payload = {'url': url, 'caption': caption, 'category': category}
server_addr = "http://192.168.0.198:5000/"
response = requests.get(server_addr, params=payload)
