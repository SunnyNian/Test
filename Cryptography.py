def Caesar(someString, shift):
    """
    This function works by taking the index of every character in the string someString and finding its index in
    variable a, the alphabet, and increasing it by the parameter shift, modulo'ing it by 26 and then returning the value
    of alphabet variable a in the position of the final result.
    :param someString: String to be encrypted, as a string.
    :param shift: Integer value of desired forward shift, as an integer.
    :return: Shifted/encrypted string, as a string.
    """
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = ""
    for i in someString:
        if i.upper() in a:
            final += a[(a.index(i.upper()) + shift) % 26]
        else:
            final += i
    return final

def unCaesar(someString, shift):
    """
    This function works by taking the index of every character in the string someString and finding its index in
    variable a, the alphabet and decreasing it by the parameter shift, modulo'ing it by 26 and then returning the value
    of alphabet variable a in the position of the final result.
    :param someString: String to be encrypted, as a string.
    :param shift: Integer value of desired forward shift, as an integer.
    :return: Shifted/encrypted string, as a string.
    """
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = ""
    for i in someString:
        if i.upper() in a:
            final += a[(a.index(i.upper()) - shift) % 26]
        else:
            final += i
    return final


def Viginere(someString, someKey):
    """
    This function starts by taking parameter someKey and multiplying it until it has equal or greater length to
    parameter someKey. Then, for each character in someString, it takes the index of this character of variable a, the
    alphabet, and increasing it by the index of its corresponding character to the finalShift, the variable of the
    expanded parameter someKey.
    :param someString: String to encrypted, as a string.
    :param someKey: Viginere key, as a string.
    :return: Shifted/encrypted string, as a string.
    """
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
    """
    This function starts by taking parameter someKey and multiplying it until it has equal or greater length to
    parameter someKey. Then, for each character in someString, it takes the index of this character of variable a, the
    alphabet, and decreasing it by the index of its corresponding character to the finalShift, the variable of the
    expanded parameter someKey.
    :param someString: String to encrypted, as a string.
    :param someKey: Viginere key, as a string.
    :return: Shifted/encrypted string, as a string.
    """
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
