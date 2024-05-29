names = []


for i in range(5):
    name = input("Please enter a name: ")
    names.append(name)


print("The first three names entered are:")
print(names[:3])