# this program will check two number
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 > num2:
    print(num1, " :is greater than: ", num2)
else:
    print(num2, " :is greater than: ", num1)

# this program check the weather
weather = input("Enter the weather (rainy, sunny, snowy): ").lower()
if weather == "sunny":
    print("It's a beautiful day! Go outside and enjoy!")
elif weather == "rainy":
    print("Don't forget your umbrella!")
elif weather == "snowy":
    print("Time for a snowball fight!")
else:
    print("I don't have advice for that kind of weather.")

# lab no 4
# this program will check username and password if your condition is correct so print the login successful and else your user name and password incorrect

user = input("Enter the User Number: ").lower()
password = int(input("Enter Your Password Must be in Number: "))

# print(password)

if user == "admin" and password == 12345:
    print("login successful")
else:
    print("your user name and password incorrect")


# lab no 4
balance = 50000

user_pin = int(input("Enter your pin: "))
if user_pin == 1234:
    print("Your balance is:", balance)

else:
    print("Incorrect PIN...")
