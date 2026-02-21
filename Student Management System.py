import csv
import os

filename = "students.csv"

# Create file with header if not exists
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["RollNo", "Name", "Marks"])

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])
    print("Student Added Successfully!\n")

def view_students():
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

def search_student():
    roll = input("Enter Roll No to Search: ")
    found = False

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll:
                print("Student Found:", row)
                found = True
                break

    if not found:
        print("Student Not Found!\n")

def delete_student():
    roll = input("Enter Roll No to Delete: ")
    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != roll:
                rows.append(row)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Student Deleted (if existed).\n")

while True:
    print("1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("Choose Option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid Choice\n")