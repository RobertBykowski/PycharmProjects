# scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
# key, value = scoundrel.popitem()
# print(key)
# print(value)
#
# name = input('What is your name? ')
# if name.endswith('Tom'):
#     print('Hello, Mr. Tom')

people = {
    'Alice': {        'phone': '2341',        'addr': 'Foo drive 23'    },
    'Beth': {        'phone': '9102',        'addr': 'Bar street 42'    },
    'Cecil': {        'phone': '3158',        'addr': 'Baz avenue 90'    }
}
# Descriptive labels for the phone number and address. These will be used # when printing the output.
labels = {    'phone': 'phone number',    'addr': 'address' }
name = input('Name: ')
# Are we looking for a phone number or an address?
request = input('Phone number (p) or address (a)? ')
# Use the correct key:
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
# Only try to print information if the name is a valid key in # our dictionary:
if name in people:
    print("{} {} is {}".format(name, labels[key], people[name][key]))


