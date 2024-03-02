import requests,json

api='https://api.github.com/users'
getData=requests.get(api)
print(getData)
print(getData.content)
print(getData.headers)

with open('github.json',"w") as file:
    json.dump(getData.json(),file)