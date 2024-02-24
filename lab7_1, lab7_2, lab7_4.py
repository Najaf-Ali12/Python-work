#lab7_1
student_dict={}
for i in range(2):
    student=input(f"enter the name of student {i+1}:")
    if student in student_dict.keys():
        print(student,"already in list")
    else:
        marks=int(input(f"enter the obtained marks of {student}:"))
        student_dict[student]=marks
print(student_dict)
#lab7_2
item_dict={"item1":45.50,"item2":35,"item3":41.30,
           "item4":55,"item5":24}
greatest=0
for num in item_dict.values():
    if num>greatest:
        greatest=num
print(" the highest price is",greatest)
smallest=1000
for number in item_dict.values():
    if number<smallest:
        smallest=number
print("the smallest price is",smallest)
#lab7_4
login_system={
    "najaf":"7865uv",
    "meer":"123ty",
    "aftab":"456yt"
}
username=input("enter the username" )
code=input(f"enter the password of {username}")
if username in login_system.keys():
    if login_system[username]==code:
        print("login succesfully")
    else:
        print("incorrect password")
else:
    print("incorrect username")



