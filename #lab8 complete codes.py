#lab8_1
sth=input("enter sth")
print(len(sth))
#lab8_2
list=[]
for i in range(3):
    num=int(input("enter a number"))
    list.append(num)
print(max(list))
print(min(list))
#lab8_3
list2=[2,3,4,5,6,7,8,9,12,33,44,55,555] 
print(sum(list2))
#lab8_4 
list3=[]
for i in range(6):
    number=int(input("enter a number"))  
    list3.append(number)
list3.sort()
print(list3)
#lab8_5
print(abs(int(input("enter a number"))))
#lab8_6
print(type(input("enter anything")))
#lab8_7
from datetime import date
specific_date = date(2024, 2, 12)
formatted_date = specific_date.strftime("%Y-%m-%d")
print(formatted_date)

