
while 1:
    palindrom = input()
    tempstr = ""
    if(int(palindrom) == 0):
        break
    else:
        if(palindrom == tempstr.join(reversed(palindrom))):
            print("yes")
        else:
            print("no")
