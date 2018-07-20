import time

f = open("polybiusPhrase.txt", "r")
phrase = f.read()
f.close()

f = open("polybiusKey.txt", "r")
key = f.read()
f.close()

print("")
print('Decrypting: "' + phrase + '"')
print('with Polybius key of: "' + key + '"')

time.sleep(1)
print(".")

phrase = phrase.split(" ")
key = list(key)
output = ""

time.sleep(1)
print(".")

for i in range(0, len(phrase)):
    temp = phrase[i]
    temp = list(temp)
    if(len(temp) == 2):
        output += key[(int(temp[0])-1)*7+int(temp[1])-1]
    if(len(temp) == 1):
        output += key[int(temp[0])-1]

time.sleep(1)
print(".")

print("")
print('Decrypted key is:  "' + output + '"')
print("")

input("Done? ")
