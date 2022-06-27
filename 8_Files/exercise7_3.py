fname = input("Enter file name to load: ")

if fname == "na na boo boo":
    print("This is the greatest easter egg of all time.")
    exit()

try:
    fhand = open(fname)
except:
    print("Failed to open file", fname, ".")
    exit()


count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count += 1

try:
    fout = open("output.txt", "w")
except:
    print("Failed to open output file.")
    exit()
output = "Number of subject lines: " + str(count)
fout.write(output)
fout.write("\nExtra line")
fout.close()
