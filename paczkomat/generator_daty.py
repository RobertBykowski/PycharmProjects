import datetime
import random
def generator():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

list_dates =[]

for i in range(10):
    date_ = generator()
    list_dates.append(str(date_))

list_time = []
for ii in range(10):
    a = round(random.uniform(33.33, 66.66), 2)
    list_time.append(a)