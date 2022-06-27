try:
    fhand = open("mbox-short.txt")
except:
    print("Failed to open file \'mbox-short.txt\'")
    exit()
for line in fhand:
    print(line.upper())
