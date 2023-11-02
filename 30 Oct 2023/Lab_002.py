phone_book = {"Batman": 987654321, "Superman": 1234567890, "Wonder": 97876545}

# Dict ?  It is very close to the JSON
print(phone_book)
print(len(phone_book))

print(phone_book["Batman"])
print(phone_book["Wonder"])

# You can access element by Key only - Dict


phone_book2 = dict(Batman=123, Cersei=342, GB=323)
print(phone_book2)
# We can access by single & double quote both
print(phone_book2['GB'])
print(phone_book2["GB"])
print(phone_book2.get('GB'))
print(phone_book2.get("GB"))

sania_details = dict(name="Sania", age=34, isFemale=True, Address="KA")
sania_details2 = {"name": "Sania", "90": 34.34, "isFeMale": True, "Address": "KA"}
print(sania_details)
print(sania_details['age'])
print(sania_details.get('age'))
print(sania_details2['age'])

#print(sania_details2.get(90)) 

print(sania_details)
