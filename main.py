from random import seed
from random import randint
import sys

attempt = 0
number = randint(1, 100)

print("Zgadnij liczbę z zakresu 1-100")

while True:
    guess = int(input())
    attempt += 1

    if guess > number:
        print("Za duża liczba")

    elif guess < number:
        print("Za mała liczba")

    else:
        print("Brawo, mój przyjacielu, udało Ci się zgadnąć w %d próbie." % attempt)
        sys.exit()
