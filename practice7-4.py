# 7-4
list_pizza = "\nPlease enter minue:"
list_pizza += "\n Enter 'quiet' when you are finished"
while True:
    minue = raw_input(list_pizza)
    if minue == 'quiet':
        break
    else:
        print("I will aad " + minue + ' to pizza!')
# 7-5
message = "\nHow old are you? "
message += "\n Enter 'quiet' to finished"
active = True
while active:
    age = raw_input(message)
    if age == 'quiet':
        active = False
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age >= 3  and  age <  12:
            price = 10
        else:
            price = 15
        print('\nYou sould pay: $' + str(price))

num = 3
while num < 15:
    print(num)
    num += 1