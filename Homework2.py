#Yunus Emre Yalın  

user=[]
user_firstname=input("Please enter your user first name: ")
user_lastname=input("Please enter your last name: ")
user_age=int(input("Please enter your age: "))
user_birthofyear=int(input("Please enter your birth year: "))
user.append(user_firstname)
user.append(user_lastname)
user.append(user_age)
user.append(user_birthofyear)

for i in user:
    print(i)

if user_age<=18:
        print("You can't go out because it's too dangerous.")
else:
        print("You can go out to the street.")