
with open("example.txt","r") as a:
    b = a.read()

allowed = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
item = ''.join(filter(allowed.__contains__, b))

c = item.split()

for i in