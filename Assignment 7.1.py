# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
a = fh.read()
b=a.upper()
print(b.strip())
