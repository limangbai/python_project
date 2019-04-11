#print part
players = ['charles', 'martina', 'michael', 'florebce', 'eli']
#print(players[:4])
print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())

#memcopy list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print('The first three iteams in the list are:')
print(my_foods[:3])
print('Three items from the middle of the list are:')
print(my_foods[1:4])
print('The last three iems in the list are:')
print(my_foods[-3:])