tasks = []

while True:
    print("\nTodo App")
    print("1. Add a task")
    print("2. Delete a task at index")
    print("3. Remove the last task")
    print("4. Sort the list")
    print("5. Print the list")
    print("6. Exit the app")

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            task = input("Enter a task: ")


            if task == "-1":
                break

            tasks.append(task)

    elif choice == "2":
        index = int(input("Enter index: "))
        tasks.pop(index)
        print(tasks)

    elif choice == "3":
        if tasks:
            tasks.pop()
        print(tasks)

    elif choice == "4":
        tasks.sort()
        print(tasks)

    elif choice == "5":
        print(tasks)

    elif choice == "6":
        print("Exiting the app...")
        break