# aeiouy
ciag_znak = input("Podaj dowolny ciąg znaków: ")
patern = ["a", "e", "i", "u", "y"]
for znak in patern:
    if znak in ciag_znak:
        print("ciąg zawiera samogłoski")
        break
    elif ciag_znak[-1] == "z" and ciag_znak[0] == "a":
        print("Zawiera alfabet ")
        break
else:
        print("Nie zawiera samogłosek <aeiouy> ")

# if znak in ciag_znak and "e" in ciag_znak and "i" in ciag_znak and "u" in ciag_znak and "y" in ciag_znak:
