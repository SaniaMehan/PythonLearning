products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},
]

print(type(products))
print(type(products[0]))

#products[0] - name, price



def is_affordable(item):
    return item["price"] < 500

# affordable_items = list(filter(is_affordable,products))
# print(affordable_items)
# print(affordable_items[0]["name"]+str(affordable_items[0]["price"]))
# print(affordable_items[1]["name"]+str(affordable_items[1]["price"]))
def is_affordable_name(items):
    return len(items["name"]) > 6

affordable_items_price = list(filter(is_affordable,products))
affordable_items_names = list(filter(is_affordable_name,products))
for i in affordable_items_price:
    print(i["price"],i["name"])


for i in affordable_items_names:
    print(i["price"],i["name"])

i = 10
name = "sania"
print(i)
print(name)
print(name+str(i))
# print(int(name)+i)
