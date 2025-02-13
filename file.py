file = open("numbers.txt", 'r')
#print(file.read())
#text = file.read()
#print(text)

#to read a line
#print(file.readline())


#to seek for the record instead of going thru every record

#file.seek()
total = 0
text =  file.readlines()
for i in range (len(text)):
    total = total + int(text[i])
print(total)


name = "      james      "
print(name.rstrip())

for line in file:
    print(line.rstrip())

numberarr = []
for line in file:
    numberarr.append(int(line.rstrip()))

print(numberarr)

file.close()