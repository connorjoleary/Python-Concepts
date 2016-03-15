# Connor O'Leary
# October 29, 2010
# Pig Latin Translator
import string
def checknumber(p):
    pass
def checkpun(n):
    pun = ",./?':;$%#&()"
    if n in pun:
        return 1
    return 0
def checkcap(m):
    caps = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    for x in m:
        if x in caps:
            return 1
    return 0
    
        
def changeword(word):
    v = "aeiouAEIOU"
    c = 0
    b = 0
    is_cap = 0
    cap_list = []
    for y in word:
        is_cap = checkcap(y)
        if is_cap == 1:
            cap_list.append(b)
        b=b+1
    word = word.lower()
    if len(word) == 1:
        word2 = word+"yay"
    else:
        for x in word:
            if x in v:
                break
            c = c+1
        words2 = word[c:]+word[:c]+"ay"

    if len(cap_list) >= 1:
        for z in cap_list:
            words2 = words2[:z] + words2[z].upper() + words2[z+1:]
    print words2,


print "Welcome to the Pig Latin Translator"

answer = "yes"
while answer == "yes":
    print
    word = raw_input ("What do you want to translate:")
    listwords = words.split()

    for y in listwords:
    print
    answer = raw_input ("Do you want to go again?:")

print "Goodbye!"
