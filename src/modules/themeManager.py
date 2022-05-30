import json

def loadDefaultTheme():
    df = open('src/modules/themes/default.json')
    dg = json.load(df)

    nf = open('src/modules/themes/current.json', 'w')

    json.dump(dg, nf, indent=4)

    df.close()
    nf.close()

    print('done loading theme')

def modifyThemeColors(themeId: str, colorMap: dict[str, str]):
    nf = open('src/modules/themes/current.json', 'r')

    get = json.load(nf)

    if (not hasattr(get, themeId)):
        get[themeId] = get["defaults"]

    idslot = get[themeId]["colours"]

    for key in colorMap:
        value = colorMap[key]

        idslot[key] = value

    nf.close()

    nf = open('src/modules/themes/current.json', 'w')

    json.dump(get, nf, indent=4)

    nf.close()