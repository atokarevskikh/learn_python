phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_plist = plist[1:3:]
new_plist.extend(plist[5:3:-1])
new_plist.extend(plist[7:5:-1])

new_phrase = "".join(new_plist)
print(new_plist)
print(new_phrase)
