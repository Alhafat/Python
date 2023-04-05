from os import remove
from re import sub

# s= "aaaxbbbbyyhwawiwjjjwwm"
# print(s)
# # count=sum([int(1) for i in s if i >'m'])
# print(f"{sum([1 for i in s if i >'m'])}/{len(s)}")


# number=9119
# # number=int(''.join([str(int(i)**2) for i in str(number)]))
# number=int(''.join((map(lambda x: str(int(x)**2), str(number)))))
# print(number)
#
# text = "Should count all vowels"
# print(len(text) - len(sub("[a,e,i,o,u]", '', text)))
# # print(len(re.findall('[aeiou]', str, re.IGNORECASE)))


# bus_stops = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
# # bus_stops=tuple(bus_stops),
# # bus_stops+=(sum(bus_stops[0][i][0] for i in range(len(bus_stops[0]))) - sum(
# #     bus_stops[0][i][1] for i in range(len(bus_stops[0])))),
# bus_stops.append(sum(i[0] for i in bus_stops) - sum(i[1] for i in bus_stops))
# print(bus_stops)

#
# a1="aretheyhere"
# a2="yestheyarehere"
# text=a1+a2
# text=''.join(sorted(set(text)))
# print(text)


# haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
# # print(f'found the needle at position {haystack.index("needle")}' if 'needle' in haystack else None)
# print('found the needle at position %d' % haystack.index('needle'))

# s='a'
# # print(s[len(s)//2:len(s)//2+1] if len(s)%2 else s[len(s)//2-1:len(s)//2+1])
# print(s[(len(s)-1)//2:len(s)//2+1])

# greet = lambda: "hello world!"
# print(greet())


# arr = [0,1,1, 0]
# value = '0b' + ''.join([str(i) for i in arr])
# print(int(''.join([str(i) for i in arr]), 2))
# print(int(''.join(map(str, arr)), 2))

# # создадим число в десятичной системе
# d = 2
#
# # переведем в двоичную (binary)
# bin_d = bin(d)
# print(bin_d)
# print(type(bin_d))
#
# # переведем обратно в десятичную
# print(int(bin_d, 2))
#
# print(value==bin_d)


# l = [1, "a", "b", 0, 15]
# s=list(filter(lambda x: type(x)==int, l))
# print(s)


# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"


# arr = [i for i in range(20, 241)]
# test=[1 if i % 20 == 0 else 0 for i in arr if i % 20 == 0 or i % 21 == 0]
# print(f'делится на 20 -> {test.count(1)}, делится на 21 -> {test.count(0)}')


# print(len([i for i in range(len(arr)) if i % 20 == 0 or i % 21 == 0]))
