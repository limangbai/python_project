#number
for value in range(1,5):
    print(value)
number = list(range(1,6))
print(number)

even_number = list(range(2, 12, 3))
print(even_number)

#square
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

#/* 4-4 4-5*/
#print 1 to 1000000
#number_list = list(range(1, 1000001))
#print(number_list)
#print(min(number_list))
#print(max(number_list))
#print(sum(number_list))
#/* 4-6*/
for even_number in range(1,21,2):
    print(even_number)
#/* 4-7*/
for number3 in range(0, 31, 3):
    print(number3)

#/**4-8/
squares3 = []
for square3 in range(1, 11):
    value3 = square3**3
    squares3.append(value3)
    #squares3.append(square3**2)
print(squares3)

#1-9
square = [value**3 for value in range(1,11)]
print(square)