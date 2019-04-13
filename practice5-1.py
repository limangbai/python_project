cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        print(car == 'bwm')
car = 'Bwm'
print(car.lower() == 'bwm')
print(car == 'bwm')

age = 28
age1 = 31
print(age >= 38 and age1 >= 18)
print(age >= 38 or age1 >= 18)

print('bwm' in car)
print('bwm' not in car)
print("Is car == 'bwm'? I predict True.")
print(car == 'Bwm')
print("\n Is car == 'bwmm'? Ipredict False.")
print(car == 'bwmm')

age = 23
if age >=18:
    print("You are old enough to vote!")
    print("Have you regidtered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your addmission cost is $10.")

if age < 4:
    price = 5
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) +'.')

alien_color = 'red'
if alien_color == 'green':
    point = 5
    #print("Great, you get 5 point power!")
elif alien_color == 'yellow':
    point = 10
    #print("Great,you get 10 point power!")
elif alien_color == 'red':
    point = 15
    #print('Great,you get 15 point power!')
else:
    point = 0;
if point != 0:
    print('Great,you get ' + str(point) +' point power!')
else:
    print('Sorry,you not get point power,try again')

users = ['tony', 'hunger', 'demi', 'aimy', 'tiner','admin']
for user in users:
    #print('hello!' + user)
    if user != 'admin':
        print("hello Erick,thank for logging in again")
    else:
        print("Heelo admin,would you like to see a status report")
#del users
if users:
    print('find some users!')
else:
    print('We need to find some users!')
new_user = ['tony', 'tt', 'pegone', 'afujiny', 'demi']
for user in new_user:
    if(user in users):
        print('the name ' + user + ' be used')
    else:
        print('the name ' + user + ' not use')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if(number == 2):
        print(str(number) + 'nd')
    elif(number == 3):
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')