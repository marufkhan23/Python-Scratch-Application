num = int(input("Enter the number --->>  "))


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizz-BUZZ"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    return number


print(fizz_buzz(num))