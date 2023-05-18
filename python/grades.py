bathmos=float(input("Δώσε τον βαθμό: "))
if bathmos>8.5 and bathmos<=10:
    print(f"{bathmos} - ΑΡΙΣΤΑ")
elif bathmos>6.5 and bathmos<8.5:
    print(f"{bathmos} - ΠΟΛΥ ΚΑΛΑ")
elif bathmos>=5 and bathmos<6.5:
    print(f"{bathmos} - ΚΑΛΑ")
elif bathmos<5:
    print(f"{bathmos} - ΑΠΕΤΥΧΕΣ")
else:
    print("ERROR")

