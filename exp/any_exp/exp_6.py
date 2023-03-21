def Get_100():
    n = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    import itertools
    p = itertools.permutations(n)
    for i in list(p):
        expression = ""
        for j in range(8):
            expression += i[j]
            if (j != 7):
                expression += "+" if (eval(expression) <= 100) else "-"
                print(expression)
        if (eval(expression) == 100):
            print(expression + i[8])


Get_100()
