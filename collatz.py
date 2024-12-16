def collatz(number):
    if number % 2 == 0:
        return 2
    elif number % 2 != 0:
        return ((3 * number) + 1)
    else:
        print("You dont even input a number")    
i = 0
while i != 1:
    print('Please input a number, we will test it! :')
    test = input()
    try:
        i = collatz(int(test))
        print('The output of collatz function is :' + str(i))
    except:
        print('Cmon Bro., you dont even put a number')