import json
from typing import Union

def loadDefaultTheme():
    df = open('src/modules/themes/default.json')
    dg = json.load(df)

    nf = open('src/modules/themes/current.json', 'w')

    json.dump(dg, nf, indent=4)

    df.close()
    nf.close()

    print('done loading theme')

def modifyTheme(themeId: str, colorMap: dict[str, str] = None, fontMap: dict[str, Union[str, int]] = None, miscMap: dict[str, Union[str, int]] = None):
    nf = open('src/modules/themes/current.json', 'r')

    get = json.load(nf)

    if (not hasattr(get, themeId)):
        get[themeId] = get["defaults"]

    if colorMap:
        idslot = get[themeId]["colours"]

        for key in colorMap:
            value = colorMap[key]

            idslot[key] = value

    if fontMap:
        idslot = get[themeId]["font"]

        for key in fontMap:
            value = fontMap[key]

            idslot[key] = value

    if miscMap:
        idslot = get[themeId]["misc"]

        for key in miscMap:
            value = miscMap[key]

            idslot[key] = value

    nf.close()

    nf = open('src/modules/themes/current.json', 'w')

    json.dump(get, nf, indent=4)

    nf.close()