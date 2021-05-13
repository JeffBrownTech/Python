def collatz(number):
    if number % 2 == 0:
        output = number // 2
        print(str(output))
        return output
    else:
        output = 3 * number + 1
        print(str(output))
        return output

while True:
    try:
        print('Input a positive, whole number:')
        userNumber = int(input())
        if userNumber <= 0:
            print('Error: Number must be greater than 0. Please try again.')
        else:
            break
    except ValueError:
        print('That isn\'t an integer. Please try again.')

while True:
    userNumber = collatz(userNumber)
    if userNumber == 1:
        break