with open("example.txt", "r") as a:
    # This block replaces all letters that may be substituted as spaces with spaces.
    b = a.read()
    b = b.replace("\n", ' ')
    b = b.replace("—", ' ')
    b = b.replace("-", ' ')
    b = b.replace(".", ' ')

def alphabetical():
    # This block filters all non alphabetical characters. It then splits all words by the instance of spaces and
    # then sorts it alphabetically.
    count = {}
    c = b
    allowed = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
    c = ''.join(filter(allowed.__contains__, c))
    c = c.split()

    # This block assigns each letter to a key in a dictionary, initialized at 0. If the key in the dictionary already
    # exists, it instead increases the value of that key by 1.
    for i in c:
        i = i.lower()
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    # For every key in the dictionary, print the key followed by its value.
    for key in sorted(count):
        print("%s: %s" % (key, count[key]))


def number():
    # This block filters all non alphabetical characters. It then splits all words by the instance of spaces and
    # then sorts it alphabetically.
    count = {}
    c = b
    allowed = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
    c = ''.join(filter(allowed.__contains__, c))
    c = c.split()

    # This block assigns each letter to a key in a dictionary, initialized at 0. If the key in the dictionary already
    # exists, it instead increases the value of that key by 1.
    for i in c:
        i = i.lower()
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # This turns the dictionary into a tuple, then, line by line, swaps the value and the key, and then sorts it.
    # As the most efficient way to sort a dictionary by key, after it finishes by converting the tuple to a dictionary.
    sortedCount = dict(sorted(count.items(), key=lambda kv: kv[1])[::-1])

    # For every key in the dictionary, print the key followed by its value.
    for key in sortedCount:
        print("{}: {}".format(key, sortedCount[key]))
