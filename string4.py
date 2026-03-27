string = "perpendicular"

while True:
    substring = input("What are you looking for? ")
    index = string.find(substring)
    if index >= 0:
        print(f"Found it at the index {index}")
    elif substring == " ":
        break
    else:
        print("Not found")


