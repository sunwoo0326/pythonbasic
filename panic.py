phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


for in range(4):
    plist.pop()
plist.pop(0)
plist.remove(" ")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))