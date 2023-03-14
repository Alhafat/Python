# У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке. Вы можете вставлять между ними знаки «+», «-» или ничего.
# У вас будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.
#
numbers = "1+2-3-4-5-6-7-8-9"
plus_sign="+"
minus_sign="-"
array=["0"]
count=0
for n in numbers:
    array.append(numbers[:count])
    for i in numbers[count+1:]:
        if eval("".join(array))<100:
            array.append(plus_sign)
            array.append(i)
        elif eval("".join(array)) == 100:
            print(array)
        else:
            array.append(minus_sign)
            array.append(i)
        del array[1:]
    count-=1








