sandwich_orders = ['pastrami', 'huotui', 'age', 'peigeng', 'mush', 'pastrami', 'pastrami']
finished_sandwiches = []
print('\n before remove: ')
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(sandwich + " is finished!")
print("There are sandwiches that have been made: ")
print(finished_sandwiches)
print('\nafter remove')
print(sandwich_orders)

print("If you could visit a place in the world ,where would you go?enter the place of name: ")
print('enter quiet to finished!')
while True:
    place = raw_input()
    if place == 'quiet':
        break
    else:
        print(place)

