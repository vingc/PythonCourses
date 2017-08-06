#! python

number = 30

while True:
    guess = int(input("Enter a number:"))

    if guess == number:
        print("Congratulations, hit the number")
        break; #don't exec the else of while
    elif guess < number:
        print("No, the nunber is bigger")
    else:
        print("No, the number is lower")
else:
    print("Guess Done")

print("Game Over")

for i in [1,2,3,4]:
    print(i)
