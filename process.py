import pandas as pd
import re
import json

with open("users.json", "r") as file:
    jsonified = file.read()

users = json.loads(jsonified)

df = pd.DataFrame(users)

df.to_csv("users.csv")