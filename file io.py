# write
s = ' User is a good person'

with open('sample1.txt', 'w') as f:
    f.write(s)

fp = open('sample1.txt', 'w')
fp.write(s)
fp.close()

# read

with open('sample1.txt', 'r') as f:
    s = f.read()
    print(s)