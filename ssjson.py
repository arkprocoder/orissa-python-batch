import json

# data={
#     "name":"Guvi",
#     "location":"IIT",
#     "city":"chennai",
#     "year":2024
# }

# json_string=json.dumps(data)
# print(type(json_string))
# print(json_string)
# with open('data.json',"w") as file:
#     json.dump(data,file)

with open("data.json","r") as file:
    loaddata=json.load(file)
    print(loaddata)