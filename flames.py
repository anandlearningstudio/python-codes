f_list = list("FLAMES")
name1 = input("Enter the first person name: ").lower()
name2 = input("Enter the second person name: ").lower()

temp2 = name2

for char in name1:
    if char in name2:
        temp2 = temp2.replace(char, "")
for char in name2:
    if char in name1:
        name1 = name1.replace(char, "")

final = len(temp2)+len(name1)
relation = f_list[(final % 6) -1]
print("Relationship between both are: ", relation)
