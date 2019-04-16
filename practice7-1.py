message = raw_input("Tell me something,and i will repeat it pack to you: ")
print(message)
name = raw_input("please enter your name: ")
print("Hello " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\n What is you first name? "
name1 = raw_input(prompt)
print("\nHello, " + name1 + "!")
age = raw_input("How old are you?")
age = int(age)

print(age > 18)
height = raw_input("How Tall are you, in inches?")
height = int(height)
if height > 36:
    print("Your tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little order.")

number = raw_input("Enter a number, and I;ll tell you if it's even or add: ")
number = int(number)
if number%2 == 0:
    print("\n The number " + str(number) + " is even.")
else:
    print("\n The number " + str(number) + " s odd.")

car = raw_input("what car you want ord?")
print("Let's me see if I can find you a " + car)

num = raw_input("How many people whille come?")
num = int(num)
if num > 8:
    print("\nSorry haven't")
else:
    print("\nYou can orde")

num2 = raw_input("Enter any number: ")
num2 = int(num2)
if num2%10 == 0:
    print("\nThe number " + str(num2) + " is 10's mulriole!")
else:
    print("\nThe number " + str(num2) + " not 10's mulriple!")