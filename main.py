# Moduły import
import datetime
import calendar
# switch - nowa funkcja

def translate_to_polish(day_name):
    match day_name:
        case 'Monday':
            return "Ponidzialek"
        case "Tuesday":
            return "Wtorek"
        case "Wednesday":
            return "Sroda"
        case "Thursday":
            return "Czwartek"
        case "Friday":
            return "Piatek"
        case "Saturday":
            return "Sobota"
        case "Sunday":
            return "Niedziela"

day_of_birth = input("Podaj date urodzin: ")
day, month, year = day_of_birth.split("-")
day_of_birth = datetime.datetime(int(year), int(month), int(day))
print ("To był", day_of_birth.weekday(), "dzień tygodnia")
day_name = calendar.day_name[day_of_birth.weekday()]
print("To była", translate_to_polish(day_name))
