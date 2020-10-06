import hashlib
import json
import os.path


def hashing():
    with open('daten.json', encoding='utf-8') as file:
        obj = json.loads(file.read())
        for person in obj:
            for key in person.keys():
                person[key] = str(hashlib.sha3_256(bytes(str(person[key]), 'utf-8')).digest())

    if not os.path.exists('datenHash.json'):
        open("datenHash.json", "x")
    file = open('datenHash.json', "w")
    file.write(json.dumps(obj, indent=4, sort_keys=True))
    file.close()


hashing()
