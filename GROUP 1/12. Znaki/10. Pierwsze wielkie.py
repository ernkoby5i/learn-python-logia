#text = input()
text = "Hello, how are you?"
words = text.split()
for word in words:
    #print(word)
    word1 = word[0]
    #print(word1)
    if ord(word1) >= 97 and ord(word1) <= 122:
        #print("MALA")
        v = ord(word1)-32
        c = chr(v)
        #print(c)
        word1 = c
    print(word1+word[1:],end='')
