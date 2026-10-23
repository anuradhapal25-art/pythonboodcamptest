import csv

with open("contacts.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Phone"])
    writer.writerow(["Anuradha", "9876543210"])
    writer.writerow(["Aman", "9876543211"])
    writer.writerow(["Priya", "9876543212"])
    writer.writerow(["Aditi", "9876543213"])
    writer.writerow(["Rahul", "9876543214"])
    writer.writerow(["Ankit", "9876543215"])

with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    for contact in reader:
        if contact["Name"].startswith("A"):
            print(contact["Name"], contact["Phone"])