
import random
print("")
print("Encryptable values: abcdefghijklmnopqrstuvwxyz0123456789 +-*/=?!@#,&~")

values = "abcdefghijklmnopqrstuvwxyz0123456789+-*/=?!@#,&~ "
values = list(values)
arrange = ""
remainNum = 48
currIndex = 0
inputs = input("Input to Encrypt(polybius):  ")

for x in range(0, 49):
    currIndex = random.randint(0,remainNum)
    arrange = arrange + values[currIndex]
    values.remove(values[currIndex])
    remainNum = remainNum-1

print("")
print("Key:  ")
print(arrange[:7])
print(arrange[7:14])
print(arrange[14:21])
print(arrange[21:28])
print(arrange[28:35])
print(arrange[35:42])
print(arrange[42:])
print("")

outputs = ""
location = 0

for x in range(0, len(inputs)):
    location = arrange.index(inputs[x])
    outputs = outputs + " " + str(int(location/7)+1) + str(location%7+1)

f = open('polybiusKey.txt', 'w')
f.write(arrange)
f.write(arrange)
f.close()
f = open('polybiusPhrase.txt', 'w')
f.write(outputs[1:])
f.close()

print(" Encrypted value:  ")
print(outputs)
print("")
print("The key is saved in -polybiusKey- and output is saved in -polybiusPhrase-")
print("")
input("Done?  ")
