"""
These program includes taking content from the  give url and converting data and  stroring in to json file

"""


# #Method 1             ----> includes taking content from the give url and converting data and  stroring in to json file without indentation



import json                                     
from urllib.request import urlopen

f = urlopen("https://jsonplaceholder.typicode.com/posts")
j = json.load(f)
k=j[0:20]
file_c=open("first_20 M-1.json","a")
file_c.write((json.dumps(j[0:20])))
file_c.close()


# # Method 2                             --->includes taking content from the give url and converting data and  stroring in to json file with indetation
import requests
import json

with open("first_20 M-2.json", "a") as file:
    file.close()
    
web_url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(web_url)                             # for pulling data from api we used get() function
data=response.json()

with open("first_20 M-2.json", "w") as file:
    json.dump(data[0:20],file,indent=4)
    file.close()
