def spr_h (h):
    if h <= 1 or h >= 9:
        return "Invalis w"

def spr_sz (sz):
    if sz <= 9 or sz >= 20:
        return "Invalis w"

h_paczka = int(input("Podaj h: "))


if spr_h(h_paczka):
    if spr_sz(h_paczka):
        print(h_paczka,"Paczka rozmiar B")
    else:
        print("Paczka C")
else:
    print(h_paczka, "paczka rozmiar A")
