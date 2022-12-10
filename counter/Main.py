import json
from Methods import User as u


def load():
    with open("data.json", "r") as f:
        data = json.load(f)
        return data


def dump(data):
    with open("data.json", "w") as f:
        json.dump(data, f)


def ask_name():
    name = input("enter name:")
    data = load()
    if name in data:
        n = u(name, data[name])
    else:
        n = u(name, 0)
        print(data[name])
    return name


Name = ask_name()


# asks the user for name:
# look for the name on the database
# gets the number associated with the name
# continues counting game
