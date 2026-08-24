import json

# add harmonics to file 
def add_harmonics(harmonics, key, path):
    data = {}
    with open(path, "r") as file:
        data = json.loads(file.read())
        data[key] = harmonics.tolist()

    with open(path, "w") as file:
        json.dump(data, file)

def load_harmonics(path):
    with open(path, "r") as file:
       return json.loads(file.read())
