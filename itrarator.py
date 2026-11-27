# fruits = ["apple", "banana", "papaya"]

# for fruit in fruits:
#     print(fruit)

# fruits = ["apple", "banana", "papaya"]

# my_it = iter(fruits)

# print(next(my_it))
# print(next(my_it))
# print(next(my_it))

class Countdown:

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):

        if self.start == 0:
            raise StopIteration

        number = self.start
        self.start = self.start - 1

        return number


for num in Countdown(3):
    print(num)

print(list(Countdown(3)))

