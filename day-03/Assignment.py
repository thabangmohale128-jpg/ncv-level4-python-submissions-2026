"""
Learner Name: THABANG DAVID MOHALE
Student Number: 2003109515
Date: 18 November 2026

Program: Learner Marks Management System

This program demonstrates the use of Python collections,
functions, searching algorithms, sorting algorithms and
interactive learner record management.
"""

# Starter data
learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 55, 72]}
}
# ==============================================================================================================
# Question 1.1

print("QUESTION 1.1")

marks = learners["2024001"]["marks"]

print("All marks:", marks)
print("First mark:", marks[0])
print("Last mark:", marks[-1])
print("First two marks:", marks[:2])

# ==============================================================================================================
# Question 1.2

print("\nQUESTION 1.2")
# Tuple representing classroom coordinate (row, seat)
classroom_coordinate = (3, 8)

row, seat = classroom_coordinate

print("Row:", row)
print("Seat:", seat)

# A tuple is appropriate because classroom coordinates should remain fixed and tuples cannot be changed.
# ===============================================================================================================
# Question 1.3

print("\nQUESTION 1.3")

module_codes = {"PRG101", "DBS101", "PRG101", "NET201", "DBS101"}

print("Unique module codes:", module_codes)
print("Number of unique codes:", len(module_codes))

print("PRG101 exists?", "PRG101" in module_codes)
print("WEB101 exists?", "WEB101" in module_codes)

# =================================================================================================================
# Question 1.4

# A dictionary is suitable because student numbers # are unique keys and allow fast access to learner records.

# A list of marks inside each learner record is suitable because a learner can have multiple marks and lists keep
# the marks together in an ordered collection.
# =================================================================================================================
# Question 2.1
# total_of(values)

def total_of(values):
    total = 0

    for value in values:
        total += value
    return total
# =================================================================================================================
# Question 2.2
# mean_of(values)

def mean_of(values):
    if len(values) == 0:
        return 0
    return total_of(values) / len(values)
# =================================================================================================================
# Question 2.3
# max_of(values) and min_of(values)

def max_of(values):
    if len(values) == 0:
        return None

    maximum = values[0]

    for value in values:
        if value > maximum:
            maximum = value
    return maximum

def min_of(values):
    if len(values) == 0:
        return None

    minimum = values[0]

    for value in values:
        if value < minimum:
            minimum = value
    return minimum
# ==================================================================================================================
# Question 2.4
# range_of(values) and above_mean(values)

def range_of(values):
    if len(values) == 0:
        return 0
    return max_of(values) - min_of(values)

def above_mean(values):
    result = []

    avg = mean_of(values)

    for value in values:
        if value > avg:
            result.append(value)
    return result

# Test data
marks = [65, 72, 58, 90, 55]

print("Total:", total_of(marks))
print("Mean:", mean_of(marks))
print("Maximum:", max_of(marks))
print("Minimum:", min_of(marks))
print("Range:", range_of(marks))
print("Above Mean:", above_mean(marks))
# ==================================================================================================================
# Question 3.1
# find_first(values, target)

def find_first(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1
# =================================================================================================================
# Question 3.2
# find_all(values, target)

def find_all(values, target):
    positions = []

    for index in range(len(values)):
        if values[index] == target:
            positions.append(index)
    return positions
# ===================================================================================================================
# Question 3.3
# count_of(values, target)

def count_of(values, target):
    count = 0

    for value in values:
        if value == target:
            count += 1
    return count
# ====================================================================================================================
# Question 3.4
# mode_of(values)

def mode_of(values):

    if len(values) == 0:
        return []

    frequency = {}

    for value in values:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    highest_frequency = max(frequency.values())

    modes = []

    for key, value in frequency.items():
        if value == highest_frequency:
            modes.append(key)
    return modes

# Test data showing a tie
numbers = [10, 20, 20, 30, 30, 40]

print("First occurrence of 20:", find_first(numbers, 20))
print("All occurrences of 20:", find_all(numbers, 20))
print("Count of 20:", count_of(numbers, 20))
print("Modes:", mode_of(numbers))

# ====================================================================================================================
# Question 4.1
# Bubble sort(values)

def bubble_sort(values):
    sorted_list = values[:]   # make a copy

    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list

# ====================================================================================================================
# Question 4.2
# Selection sort(values)

def selection_sort(values):
    sorted_list = values[:]   # make a copy

    n = len(sorted_list)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j

        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    return sorted_list

# ====================================================================================================================
# Question 4.3
# Test both sorts

test_data = [65, 72, 48, 90, 55, 72, 48, 72]

print("Original:", test_data)

print("Bubble Sort:", bubble_sort(test_data))

print("Selection Sort:", selection_sort(test_data))

print("Original after sorting:", test_data)

# ====================================================================================================================
# Question 5.1
# Bubble sort(values)


#Stater data
learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 55, 72]}
}
#Functions
def total_of(values):
    total = 0

    for value in values:
        total += value
    return total

def mean_of(values):
    if len(values) == 0:
        return 0
    return total_of(values) / len(values)

def bubble_sort(values):
    sorted_list = values[:]

    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - 1 - i):
            if sorted_list[j][0] < sorted_list[j + 1][0]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list
#==========================================================================================================
#Question 5.2 Add

def add_learner():
    student_number = input("Student Number: ")

    if student_number in learners:
        print("Student number already exists.")
        return

    name = input("Learner Name: ")

    marks_input = input("Enter marks separated by spaces: ")

    marks = []

    for mark in marks_input.split():
        mark = int(mark)

        if 0 <= mark <= 100:
            marks.append(mark)

    learners[student_number] = {
        "name": name,
        "marks": marks
    }

    print("Learner added successfully.")
#========================================================================================================
#Question 5.3 Search

def search_learner():
    student_number = input("Enter student number: ")

    if student_number in learners:
        print("Name:", learners[student_number]["name"])
        print("Marks:", learners[student_number]["marks"])
    else:
        print("Learner not found.")
#=========================================================================================================       
#Question 5.4 Update & Delete

def update_learner():
    student_number = input("Student Number: ")

    if student_number not in learners:
        print("Learner not found.")
        return

    print("1. Update Name")
    print("2. Add Mark")

    choice = input("Choice: ")

    if choice == "1":
        new_name = input("New Name: ")
        learners[student_number]["name"] = new_name
        print("Name updated.")

    elif choice == "2":
        mark = int(input("New Mark: "))

        if 0 <= mark <= 100:
            learners[student_number]["marks"].append(mark)
            print("Mark added.")
        else:
            print("Invalid mark.")

def delete_learner():
    student_number = input("Student Number: ")

    if student_number in learners:
        confirm = input("Delete learner? (Y/N): ")

        if confirm.upper() == "Y":
            del learners[student_number]
            print("Learner deleted.")
    else:
        print("Learner not found.")
#==========================================================================================================       
def display_ranking():
    ranking = []

    for student_number, details in learners.items():
        average = mean_of(details["marks"])
        ranking.append((average, student_number))

    ranking = bubble_sort(ranking)

    print("\nLEARNER RANKING")

    for average, student_number in ranking:
        print(
            student_number,
            learners[student_number]["name"],
            round(average, 2)
        )
#===========================================================================================================
#Question 5.1    
#main menu
        
while True:

    print("\n===== LEARNER MANAGEMENT SYSTEM =====")
    print("1. Add Learner")
    print("2. Search Learner")
    print("3. Update Learner")
    print("4. Delete Learner")
    print("5. Display Ranking")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_learner()

    elif choice == "2":
        search_learner()

    elif choice == "3":
        update_learner()

    elif choice == "4":
        delete_learner()

    elif choice == "5":
        display_ranking()

    elif choice == "6":
        print("Program Ended.")
        break

    else:
        print("Invalid choice. Please try again.")

