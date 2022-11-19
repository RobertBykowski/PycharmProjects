people = {
    'Alice': {        'phone': '2341',        'addr': 'Foo drive 23'    },
    'Beth': {        'phone': '9102',        'addr': 'Bar street 42'    },
    'Cecil': {        'phone': '3158',        'addr': 'Baz avenue 90'    }
}
key = input("Imie: ")
if key is not people[key]:
    print("Error")
else:
    print("{}, phone: {},addr:{}".format(key, people[ key ][ 'phone' ], people[ key ][ 'addr' ]))