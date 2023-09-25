import sys
'''Display the contents of a file on the screen, the equivalent of the 'cat' command for Linux.
    @AdrianSzklarski, 09.2023'''

print('sys.argv: ', sys.argv)
path = sys.argv[0]

f = open(path, 'r')
text = f.read()
print(text)
f.close()