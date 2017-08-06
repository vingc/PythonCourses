#! python

while True:
    s = input("Enger something:")
    if s == "quit":
        break;

    if len(s) < 3:
        print("too short")
        continue

    print("U have entered suffiecient something")

print("Done")