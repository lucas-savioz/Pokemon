import json
from os import path

filename = 'users.json'
listObj = []

# Check if file exists

if path.isfile(filename) is False:
    raise Exception("File not found")

# Read json file
with open(filename) as fp:
    listObj = json.load(fp)
    
# Verify existing list
print(listObj)
print(type(listObj))

listObj.append({
    "Name": "Person 3",
    "Age": 33,
    "Email": "33@gmail.com"
})

# Verify updated list
print(listObj)

with open(filename, 'w') as json_file:
    json.dump(listObj, json_file,
              indent=4,
              separators=(',',':'))
    
print('Succesfully appended to the JSON file')