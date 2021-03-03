cats = []

while True:
    print ("Enter the name of cat %d or enter nothing to stop." % (len(cats) + 1))
    name = input ("%d) " % (len(cats) + 1))

    if name == "":
        break

    cats = cats + [name]

print ("The cat names are: ")

for names in cats :
    print (" %s" % names)
