# Question: Print a decreasing triangle pattern using stars.

# rows = int(input("Enter the number of stars: "))
# count = rows

# for i in range(rows):
#     for j in range(count):
#         print("*", end=" ")
#     print()
#     count = count - 1


#  shop keeper 

def calculate_total(cost, items):
    print("Item Total Price:", cost * items)

amount = int(input("Enter the price: "))
count = int(input("Enter the quantity: "))

calculate_total(amount, count)