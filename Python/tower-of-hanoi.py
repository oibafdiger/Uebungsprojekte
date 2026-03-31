def hanoi_solver(number) :
    string = ''
    rod_1 = []
    rod_2 = []
    rod_3 = []
    numbers = range(number, 0, -1)
    for n in numbers :
        rod_1.append(n)

    def move(n, start, help, end) :
        nonlocal string
        if n == 1 :
            end.append(start.pop())
            string += str(rod_1) + ' ' + str(rod_2) + ' ' +str(rod_3 )+ '\n'
        else :
            move(n - 1, start, end, help)
            end.append(start.pop())
            string += str(rod_1) + ' ' +str(rod_2) + ' ' +str(rod_3 ) + '\n'
            move(n - 1, help, start, end)
    
    string += str(rod_1) + ' ' +str(rod_2) + ' ' +str(rod_3 ) + '\n'
    move(number, rod_1, rod_2, rod_3)     
    return string.strip('\n')

print(hanoi_solver(2))


