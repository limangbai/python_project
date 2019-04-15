favorite_places = {
    'xianglian': ['xian', 'anhui', 'taiguo'],
    'xiaoyan': ['hunang', 'changsha', 'zhangjiajie'],
    'qiqi': ['congqing', 'xiameng', 'daocheng']
    }
for name, places in favorite_places.items():
    print('\nname: ' + name.title())
    print('favorite place:')
    for place in places:
        print('\t' + place)

favorite_numbers = {
    'xiaoliang': [1, 2, 3],
    'xiaobai': [4, 5, 6],
    'youyou': [7, 8, 9],
    }
for name, numbers in favorite_numbers.items():
    print('\nname:' + name.title())
    print('favorite numbers:')
    for number in numbers:
        print('\t' + str(number))



