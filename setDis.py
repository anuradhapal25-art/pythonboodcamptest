# students = {"Anu", "ruby", "sikha", "Sneha"}
# print("Anu" in students)
# if "Rohan" not in students:
#     students.add("Rohan")
# print(students)


# inventory = {"Rice": 10, "Soap": 20, "Oil": 15, "Sugar": 12}
# print(inventory)
# inventory["Rice"] = inventory["Rice"] - 2
# print(inventory)
# item = "Soap"
# if item in inventory:
#     inventory[item] = inventory[item] + 1
# else:
#     inventory[item] = 10
# print(inventory)



prices = {
    "eat": 20,
    "apple": 30,
    "banana": 70,
    "milk": 50,
    "rice": 60
}

out_of_stock = {"banana", "rice"}

orders = [
    ["apple", "milk"],
    ["banana", "rice"],
    ["eat", "apple"]
]

total = 0

for order in orders:
    for item in order:
        if item in out_of_stock:
            print(item, "unavailable")
        else:
            total += prices[item]

print("Final order value:", total)
