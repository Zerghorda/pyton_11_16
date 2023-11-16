def fel1(szoveg: str):
    i: int = 0
    db: int = 0
    while i < len(szoveg):
        if szoveg[i] == " ":
            db += 1
        i += 1
    return db


def fel2(szoveg: str):
    ninicsSzokosz: str = szoveg.replace(" ", "")
    return ninicsSzokosz


def fel3(szoveg: str):
    kicsiBetu: str = szoveg.lower()
    szoveg = szoveg.replace("é", "e")
    szoveg = szoveg.replace("á", "a")
    szoveg = szoveg.replace("ő", "o")
    szoveg = szoveg.replace("ó", "o")
    szoveg = szoveg.replace("ö", "o")
    szoveg = szoveg.replace("ű", "u")
    szoveg = szoveg.replace("ü", "u")
    szoveg = szoveg.replace("ú", "u")
    szoveg = szoveg.replace("í", "i")
    ekezetnel: str = szoveg
    forditva: str = ekezetnel[::-1]
    return kicsiBetu, ekezetnel, forditva











