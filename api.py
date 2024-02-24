# API = Application Programming Interface

# key values pairs : JSON : Javascript Object Notation
import requests,json

api='https://api.github.com/users'
getData=requests.get(api)
print(getData)
# print(getData.json())
print(getData.headers)