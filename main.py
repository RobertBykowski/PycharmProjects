import datetime
day_of_birth = input("Podaj date urodzin: ")
day, month, year = day_of_birth.split("-")
day_of_birth = datetime.datetime(int(year), int(month), int(day))
print ("To był", day_of_birth.weekday(), "tydzien roku")