# marks = [72, 35, 88, 29, 60]
# passed_marks = [m for m in marks if m >= 40]
# print(passed_marks)
# tags = ["Pass" if m >= 40 else "Fail" for m in marks]
# print(tags)


# Q1: Filter numbers greater than 50

numbers = [20, 60, 45, 80, 30, 90]

result = [n for n in numbers if n > 50]

print("Numbers greater than 50:", result)


# Q2: Double every price using Dictionary Comprehension

prices = {"tea": 10, "coffee": 20, "juice": 30}

doubled = {k: v * 2 for k, v in prices.items()}

print("Doubled prices:", doubled)



report = {
    "asha": 72,
    "kabir": 35,
    "meera": 88
}
passed = {}

for name, marks in report.items():
    if marks >= 40:
        passed[name] = marks

print("Passed Students:", passed)
bonus = {}

for name, marks in report.items():
    bonus[name] = marks + 5
print("Bonus Marks:", bonus)
swapped = {}

for name, marks in report.items():
    swapped[marks] = name

print("Swapped Dictionary:", swapped)



# 1. Create countdown function

def countdown(n):
    while n > 0:
        yield n
        n = n - 1


# 2. Call countdown(3) and use next() three times

numbers = countdown(3)

print(next(numbers))
print(next(numbers))
print(next(numbers))


# 3. Print list(countdown(3))

print(list(countdown(3)))
