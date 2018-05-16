slist = raw_input("input string to be reversed: ")
newlist = []
revlist = []
for i in slist:
    newlist.append(i)

print(newlist)

length = len(newlist)

reword = ""
while length > 0:
    revlist.append(newlist[length-1])
    length -= 1

for item in revlist:
    reword = reword+item

print(revlist)
print (reword)


