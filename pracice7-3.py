unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been cinfirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = { }
polling_active = True
while polling_active:
    name = raw_input("\nWhat is your name? ")
    response = raw_input("Which mountain would you like to climbsomeday? ")
    responses[name] = response

    repeat = raw_input("Would you like to let another person respond? (yes/ no)")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")



