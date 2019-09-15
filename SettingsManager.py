import json

#Load settings
settings = json.load( open("settings.json", "r") )

def numApps():
    return len(settings["MicroServices"])

def MSinfo(metadata):
    data = list()
    for MC in settings["MicroServices"]:
        for obj in settings["MicroServices"][MC]:
            if obj == metadata:
                data.append(settings["MicroServices"][MC][metadata])
    return data