
import numpy as np

db = np.loadtxt("australian.txt")
db_type = np.loadtxt("australian-type.txt", dtype=str)

#3

#dostępne klasy decyzyjne
print("Dostępne klasy decyzyjne:", np.unique(db[:, 14]))

#b
print(len(db))

#c
#minimalne i maksymalne wartości poszczególnych atrybutów(dotyczy atrybutów numerycznych
for i in range(14):
    print(f"{i} - min: {np.min(db[:, i])}, max: {np.max(db[:, i])}")

#d
#dla każdego atrybutu wypisujemy liczbę różnych dostępnych wartości
for i in range (0,14):
    print(f"{i} - liczba różnych wartości: {len(np.unique(db[:, i]))}")

#e
#dla każdego atrybutu wypisujemy listę wszystkich różnych dostępnych wartości

for i in range (0,14):
    print(f"{i} - lista różnych wartości: {np.unique(db[:, i])}")

#f
#odchylenie standardowe dla poszczególnych atrybutów w całym systemie i w kla-
#sach decyzyjnych

for i in range(0, 15):
    print(f"{i} - odchylenie standardowe: {np.std(db[:, i])}")

