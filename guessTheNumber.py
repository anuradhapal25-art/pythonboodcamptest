import random

computer_number = random.randint(1, 5)
print(computer_number)

while True:
    guess = int(input("Guess the number (1-5): "))

    if guess == computer_number:
        print("You win, congrats!!")
        break
    else:
        print("Wrong guess, attempt again")





     

marks = [45, -1, 78, 90, -1, 60]

total = 0
count = 0

for i in marks:
    if i == -1:
        continue
    total += i
    count += 1

print("Total =", total)
print("Students present =", count)





marks = [10, 50, -5, 75]
count = 0
total = 0

for i in marks:
    if i > 0:
        total += i
        count += 1

print(count)
print(total)

