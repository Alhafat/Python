n=input('')
temp=0
text=['A','E','I','O','U','L','N','S','T','R']
print(text)
for i in text:
    print(i)
    if i == n:
        temp += 1
        continue
print(temp)