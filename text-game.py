from random import randint

x = randint(1,25)

while True:
    guess = input("Zgadnij liczbę od 1 do 25 (lub wpisz 'poddaje się'): ")

    if guess in ["poddaje się", "poddaje sie"]:
        print(f"Nie udało się zgadnąć, prawidłowa liczba to: {x}")
        break

    try:
        guess = int(guess)
        if guess == x:
            print("Udało się, zgadłeś!")
            break
        else:
            print("Nie udało się, spróbuj ponownie")
    except ValueError:
        print("Coś poszło nie tak. Wpisz liczbę lub 'poddaje się'.")