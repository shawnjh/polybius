file = {'first': ['one','uno'], 'second': 'two', 'third': 'three'}

f = open('made.txt', 'w')

f.write(str(file))

f.close()
