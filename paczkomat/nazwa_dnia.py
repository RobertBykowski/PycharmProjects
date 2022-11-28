# import calendar
#
# # calendar.weekday(year, month, day)
# a= calendar.weekday(2022, 11, 25)
# calendar.day_name[a]

from calendar import weekday, day_name

dayNumber = weekday(2022, 11, 25)

dayName = day_name[dayNumber]
print(dayName)