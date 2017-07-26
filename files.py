# file io

# import file

f = open("file.dat", "wb")
s = f.readline()
i = 0
while (s != ""): 
    i = i + 1
    print "This is line number: " + str(i) + "in file"
    print s
    s = f.readline()
