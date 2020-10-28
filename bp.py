f=open("C:\\Users\\english\\Documents\\bplist.txt")
wordlist=f.read()
wordlist=wordlist.splitlines()
wordlist.sort()
for word in wordlist:
    if "kdo" in word:
    #if word.startswith(""):
        
        #if "" in word and "" in word and "" in word:
        #if len(word) ==30:
            print(word)
