#! python

number = 30
guess = int(input("Enter a number:"))

if guess == number:
    print("Congratulations, hit the number")
elif guess < number:
    print("No, the nunber is bigger")
else:
    print("No, the number is lower")

print("Guess Done")