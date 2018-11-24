with open("example.txt", "r") as a:
    b = a.read()
    b = b.replace("\n", ' ')
    b = b.replace("—", ' ')
    b = b.replace("-", ' ')
    b = b.replace(".", ' ')

def alphabetical():
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
