current_number = raw_input("input number")
current_number = int(current_number)
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter quiet to end the program. "
message = ""
active = True
while active:
    message = raw_input(prompt)
    if active == "quiet":
        active = False
    else:
        print(message)