cities = {
    'beijing': {
        'country': 'china',
        'population': 2154.2,
        'fact': 'noe',
        },
    'tokyo': {
        'country': 'japan',
        'population': 379.59,
        'fact': 'noe',
        },
    'paris': {
        'country': 'france',
        'population': 1200,
        'fact': 'noe'
        },
    }
for city, city_info in cities.items():
    print('\ncity:' + city.title())
    print('city message:')
    print('\tcountry: '+ city_info['country'].title())
    print('\tpopulation: ' + str(city_info['population']))
    print('\tfact: ' + city_info['fact'])