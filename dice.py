import random

n = 1

kostka1 = [random.randint(1,6) for _ in range(n)]
kostka2 = [random.randint(1,6) for _ in range(n)]

kostka1 = int(''.join(map(str, kostka1))) #zwraca zwykłą liczbę
kostka2 = int(''.join(map(str, kostka2)))

print(f"Pierwsze kostka: {kostka1}, Druga kostka: {kostka2}")
#output: Pierwsze kostka: 2, Druga kostka: 1