fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
mlist = list()
for line in fh:
	if line.startswith("From") and not line.startswith("From:"):
		print (line.split()[1])
		count += 1
print ("There were", count, "lines in the file with From as the first word")
