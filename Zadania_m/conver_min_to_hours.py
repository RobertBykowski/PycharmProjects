minutes_to_conver = 123
hours_decimal = minutes_to_conver/60
hours_part = int(hours_decimal)

minutes_decimal  = hours_decimal - hours_part
minutes_part  = round(minutes_decimal*60)
print("Hours: ", hours_part)
print("Minutes: ", minutes_part)
