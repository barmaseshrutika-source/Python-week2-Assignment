
filename = "sample.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        lines = content.splitlines()
        characters = len(content)

        print("Lines:", len(lines))
        print("Words:", len(words))
        print("Characters:", characters)

except FileNotFoundError:
    print("File Not Found!")