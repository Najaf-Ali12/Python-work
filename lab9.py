sent=input("enter a sentence")
print(sent.split()) #this is direct method
#for is for datailed solution
list=[]
for word in sent.split():
    list.append(word)
print(list)
#lab 9_2
sent=("pakistan is a country")
word=input("which word you want to change: ")
new=input(f"with which word you want to replace {word}")
sent.replace(word,new)
print(sent)
#lab9_3 was difficult
#lab9_4 was not given by sir
#lab9_5
sent=input("enter a sentence:")
new=sent.split()
new.reverse()
print("new modified sentence is ",new)
#below was done by sir omar
sent=input("enter")
split_sen=sent.split()
rev="".join(reversed(split_sen))
print(rev)

