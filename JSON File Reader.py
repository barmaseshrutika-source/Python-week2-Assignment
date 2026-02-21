import json

try:
    with open("data.json", "r") as file:
        data = json.load(file)
        print("Formatted Output:")
        print("Name:", data["name"])
        print("Course:", data["course"])
        print("Marks:", data["marks"])

except FileNotFoundError:
    print("JSON File Not Found!")