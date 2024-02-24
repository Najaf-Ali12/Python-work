sent=input("enter the sentence")
letter_counter={}
for word in sent.lower():
    count=1
    if word.isalpha():
        if word in letter_counter :
            letter_counter[word]+=1 
        elif word not in letter_counter:
            letter_counter[word]=1
print(letter_counter)
