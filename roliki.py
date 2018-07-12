import io
import json
JSON_FILE = "roliki.json"


def getRoliki():
    roliki = {}
    with io.open(JSON_FILE, 'r', encoding='utf8') as file:
        roliki = json.load(file)
    return roliki


def addRolik(name, videoFile, singles, title, fontSize, fontTracking):
    roliki = getRoliki()
    listRolik = []
    listRolik.append(videoFile)
    listRolik.append(singles)
    listRolik.append(title)
    listRolik.append(fontSize)
    listRolik.append(fontTracking)
    roliki.update({name:listRolik})
    with io.open(JSON_FILE, 'w', encoding='utf8') as file:
        json.dump(roliki, file, ensure_ascii=False)


def changeRolik(name, videoFile, singles, title, fontSize, fontTracking):
    roliki = getRoliki()
    rolik = roliki.get(name)
    if videoFile is not None:
        rolik[0] = videoFile
    if singles is not None:
        rolik[1] = singles
    if title is not None:
        rolik[2] = title
    if fontSize is not None:
        rolik[3] = fontSize
    if fontTracking is not None:
        rolik[4] = fontTracking
    addRolik(name, rolik[0], rolik[1], rolik[2], rolik[3], rolik[4])


def removeRolik(name):
    roliki = getRoliki()
    roliki.pop(name)
    with io.open(JSON_FILE, 'w', encoding='utf8') as file:
        json.dump(roliki, file, ensure_ascii=False)


def listRoliki():
    roliki = getRoliki()
    listRolik = []
    for item in roliki:
        listRolik.append(item)
    listRolik.sort()
    for item in listRolik:
        print(item)
