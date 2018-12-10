fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    line=line.split()
    for a in line:
        if a not in lst:
            lst.append(a)
lst.sort()
print(lst)
