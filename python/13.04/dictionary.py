text = 'Ala ma kota ala ala ala'
counter = {}
for i in text.lower().split():
    if i not in counter:
        counter[i] = 0
    counter[i] +=1
print(counter)