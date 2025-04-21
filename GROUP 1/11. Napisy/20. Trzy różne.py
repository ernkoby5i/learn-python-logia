s = input()

odp="NIE"

for i in range(0,len(s)-2):
    #print("szukam od "+s[i])
    if (s[i]!=s[i+1]) and (s[i]!=s[i+2]) and (s[i+1]!=s[i+2]):
    #if s[i]!=s[i+1]!=s[i+2]:
        odp="TAK"
        break

print(odp)