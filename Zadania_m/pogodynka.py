from requests import get
from json import loads
from terminaltables import AsciiTable
CITIES = ["Toruń", "Szczecin"]
def main():
    respons = get("https://danepubliczne.imgw.pl/api/data/synop")
    upload_data = loads(respons.text)
    # slownik = dict(upload_data[0])
    # print(list(list(slownik.keys())))

    rows = [["Miasto", "Data pomiaru", "Temperatura", "Wilgotnosc wzgledna"]]
    for row in upload_data:
        if row["stacja"] in CITIES:
            rows.append([
                row['stacja'],
                row['data_pomiaru'],
                row['temperatura'],
                row['wilgotnosc_wzgledna']
                      ])
    table = AsciiTable(rows)
    print(table.table)

if __name__ == "__main__":

    main()
