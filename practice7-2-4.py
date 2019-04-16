prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quiet' when you are finished.)"

while True:
    City = raw_input(prompt)
    if City == 'quiet':
        break
    else:
        print("I'd love to go to " + City.title() + "!")

current_number = 0
while current_number < 10:
    current_number += 12
    if current_number % 2 == 0:
        continue
    print(current_number)


