print("Hello programmers, It's the fizz_buzz application which performs to show 'fizz' when you enter a number that divisable by 3 and 'buzz' when your input is divisable by 5. And finally, 'fizz_buzz' will be appeared when your input number is divisable by 3 and 5 both. Let's check it out !!")
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
