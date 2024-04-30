def countdown_positive(n):
    while n > 0:
        print(n)
        n -= 1
    print("Go! Go!")

def countdown_negative(n):
    while n < 0:
        print(n)
        n += 1
    print("Go! Go!")

n = int(input("What do you want to count down from?: "))

if n > 0:
    countdown_positive(n)
elif n < 0:
    countdown_negative(n)
else:
    print("The number given is 0 so Go!")
