one = raw_input("Enter file:")
two = open(one)
th = {}
for i in two:
    if i.startswith("From") and len(i.split()) > 2:
        line = i.split()
        if not th.has_key(line[5][:2]):
            th[line[5][:2]] = 1
        else:
            th[line[5][:2]] += 1

key = sorted(th)
for i in key:
    print i, th[i]
