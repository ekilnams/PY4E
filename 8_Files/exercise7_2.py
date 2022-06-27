fname = input("Enter file name to load: ")
try:
    fhand = open(fname)
except:
    print("Failed to open file", fname, ".")
    exit()

scCount = 0
scTotal = 0
for line in fhand:
    if line.find("X-DSPAM-Confidence") != -1:
        scCount += 1
        scTotal += float(line[line.rfind(":")+1:].strip())
print("Average spam confidence:", scTotal/scCount)
