s1 = input()
words = s1.split()
words_len = []
c = 0
for word in words:
    words_len.append(len(word))

for word in words_len:
    if word >= 5:
        c = c+1
print(c)
