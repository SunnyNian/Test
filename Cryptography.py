def Caesar(someString, shift):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = ""
    for i in someString:
        if i.upper() in a:
            final += a[(a.index(i.upper()) + shift) % 26]
        else:
            final += i
    return final


def unCaesar(someString, shift):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = ""
    for i in someString:
        if i.upper() in a:
            final += a[(a.index(i.upper()) - shift) % 26]
        else:
            final += i
    return final


def Viginere(someString, someKey):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = 0
    finalShift = ""
    final = ""
    while len(finalShift) < len(someString):
        for j in someKey:
            if j.upper() in a:
                finalShift += j.upper()

    for i in someString:
        if i.upper() in a:
            final += a[((a.index(i.upper())) + a.index(finalShift[b])) % 26]
            b += 1

    return final


def unViginere(someString, someKey):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = 0
    finalShift = ""
    final = ""
    while len(finalShift) < len(someString):
        for j in someKey:
            if j.upper() in a:
                finalShift += j.upper()

    for i in someString:
        if i.upper() in a:
            final += a[((a.index(i.upper())) - a.index(finalShift[b])) % 26]
            b += 1

    return final


