import json

#load json
with open("ex1.json", "r") as f:
    data = json.load(f)

#function to check number of students, should be less than 100
def shouldtakeschool(data):
    if data["Strength"] >= 100:
        return "Yes"
    return "No"