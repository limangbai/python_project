
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
alien_0['points'] = '10'
print(alien_0)

alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 13
else:
    x_increment = 33
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('new x_position: ' + str(alien_0['x_position']))

del alien_0['y_position']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'zhongyi': 'php',
    'edward': 'ruby',
    'phil': 'python',
    'demi': 'c',
    }
print("Demi's favorite language is " + favorite_languages['demi'].title() + '.')

preson_message = {'first_name': 'zhenglong',
                  'last_name': 'zhong',
                  'age': 31,
                  'city': 'shengzheng'
                  }
print(preson_message)

lucky_number = {'xiaolian': 7,
                'xiaotian': 5,
                'youyou': 8,
                'qiqi': 5,
                'anan': 6,
                'xiaoyan': 9,
                'baibai': 2,
                }
print(lucky_number)
for key, value in lucky_number.items():
    print("\nkey: " + str(key))
    print("value: " + str(value))
for name in lucky_number.keys():
    print(name.title())
print("\n")

friends = ['xiaolian', 'youyou']
for name in lucky_number.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ",I see your lucky number is " +
              str(lucky_number[name]) + '!'
            )
print("\n")

if 'zhongyi' not in lucky_number.keys():
    print("Zhongyi,please take our poll!\n")

for name in sorted(lucky_number.keys()):
    print(name.title() + ",thank you for taking the poll.")
print('\n')

print("The following number have been mentioned:")
#for number in lucky_number.values():
for number in set(lucky_number.values()):
    print(number)
poll_list = ['lizhneg', 'boshou', 'mangnu','youyou']
for name in poll_list:
    if name in lucky_number.keys():
        print(name.title() + ',thank you for the poll.')
    else:
        print(name.title() + ',please take our poll!')
print('\n')

lucky_number['hongyang'] = 1
lucky_number['ahuo'] = 0
print(lucky_number.keys())

river_country = {'lantsang': "Lao People's Republic",
                 'Mekong': "Viet Nam",
                 "yangtze River": "China",
                 }
print('\n')
for river in river_country.keys():
    print("The " + river + " runs through " + river_country[river] + '.')
for river in river_country.keys():
    print(river)
for country in river_country.values():
    print(country)
print('\n')

alien_0 = {'color': 'green', 'point': '5'}
alien_1 = {'color': 'yellow', 'point': '10'}
alien_2 = {'color': 'red', 'point': '15'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[4:7]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['pont'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['pont'] = 15
for alien in aliens[:9]:
    print(alien)
print("...")

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
    }
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "while the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'lucy': ['C', 'c++'],
    'babala': ["python", 'java'],
    'amy': 'c',
    }
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print('\n' + name.title() + "'s favorite languages are:")
        for language in languages:
            print('\t' + language.title())
    else:
        print(name.title() + "'s favorite language is:")
        print('\t' + languages.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print('\nusername:' + username.title())
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\nfull_name: ' + full_name.title())
    print('\tlocation: ' + location.title())

#6-4
people1 = {'ami': ['women', '21', 'shanghai'], }
people2 = {'lariy': ['women', '25', 'shengzheng'], }
people3 = {'tome': ['18', 'man', 'american'], }
peoples = [people1, people2, people3]
for people in peoples:
    print(people)
    for name, messages in people.items():
        print('\nname: ' + name.title())
        print('message:')
        for message in messages:
            print('\t' + message)

cate = {'host': 'babala', 'kind': 'cate'}
bird = {'host': 'tony', 'kind': 'bird'}
dog = {'host': 'amy', 'kind': 'dog'}
pets = [cate, bird, dog]
for pet in pets:
    print(pet)


