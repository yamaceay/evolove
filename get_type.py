import json

with open("users.json", "r") as file:
    jsonified = file.read()

users = json.loads(jsonified)

for user in users:
    for label in user['labels']:
        types = ["ENTP", "ENTJ", "ENFP", "ENFJ", "ESTP", "ESTJ", "ESFP", "ESFJ",
                 "ISFJ", "ISFP", "ISTJ", "ISTP", "INFJ", "INFP", "INTJ", "INTP"]
        type = label[:4]
        if type in types:
            user['forum'] = label

jsonified = json.dumps(users, indent=4)

with open("users.json", "w") as file:
    file.write(jsonified)

