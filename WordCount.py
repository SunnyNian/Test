with open("example.txt", "r") as a:
    """
    Read the file and replace all characters than may be substituted as spaces to spaces.
    """
    b = a.read()
    b = b.replace("\n", ' ')
    b = b.replace("—", ' ')
    b = b.replace("-", ' ')
    b = b.replace(".", ' ')


def alphabetical():
    """
    This function starts by creating an empty dictionary, stripping the text file of all non-alphabetical characters
    along with the apostrophe (" ' "), and then splitting the read text by spaces into individual words. Each word is
    then read and assigned into the empty dictionary; if a key with the same name as the word does not exist, it is
    initialized with key as integer 1, and if it is already present in the list, increase its value by 1. Then, for
    all keys sorted alphabetically, each key and its value is printed.
    :return: None, as NoneType.
    """
    count = {}
    c = b
    allowed = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
    c = ''.join(filter(allowed.__contains__, c))
    c = c.split()

    for i in c:
        i = i.lower()
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for key in sorted(count):
        print("%s: %s" % (key, count[key]))


def number():
    """
    This function starts by creating an empty dictionary, stripping the text file of all non-alphabetical characters
    along with the apostrophe (" ' "), and then splitting the read text by spaces into individual words. Each word is
    then read and assigned into the empty dictionary; if a key with the same name as the word does not exist, it is
    initialized with key as integer 1, and if it is already present in the list, increase its value by 1. It then
    iterates through every key, and as a tuple, swaps the position of the key and the value, and then sorts all
    previously iterated values. After the final value is sorted, the list is then reversed, and then converted back into
    a dictionary. Each key and its corresponding value is then printed.
    :return: None, as NoneType.
    """
    count = {}
    c = b
    allowed = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
    c = ''.join(filter(allowed.__contains__, c))
    c = c.split()

    for i in c:
        i = i.lower()
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    sortedCount = dict(sorted(count.items(), key=lambda kv: kv[1])[::-1])

    for key in sortedCount:
        print("{}: {}".format(key, sortedCount[key]))
