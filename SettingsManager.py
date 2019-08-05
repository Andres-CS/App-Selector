import settings


def numApps():
    return len(settings.MicroServices)

def nameApps():
    names = list()
    for MC in settings.MicroServices:
        names.append(MC["Name_MC"])
    return names

def logoApps():
    logos = list()
    for MC in settings.MicroServices:
        logos.append(MC["Logo_MC"])
    return logos