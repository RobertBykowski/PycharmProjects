# Set of data:
# Call ID, Call_Start, Call_End, Data:YY:MM:DD, Name of week day
import random
import generator_daty
data_call_list = generator_daty.list_dates
call_time_list = generator_daty.list_time

calls = {
    "call_ID" : [],
    "call_time" : call_time_list,
    "data_call" : data_call_list,
    "day_name" : ""
}
for id in range(1,11):
    calls["call_ID"].append(id)
print(calls.values(), end="")

